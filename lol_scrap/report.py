"""Ensambla el reporte Markdown final pensado para ser interpretado por Cursor."""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from .config import QUEUE_NAMES, ROLE_DISPLAY, rank_display
from .fetcher import PlayerData
from .prompts import render_role_prompt


def _fmt_pct(x: float | None) -> str:
    if x is None:
        return "—"
    return f"{x * 100:.1f}%"


def _fmt_num(x: float | None, decimals: int = 1) -> str:
    if x is None:
        return "—"
    return f"{x:.{decimals}f}"


def _fmt_int(x: float | None) -> str:
    if x is None:
        return "—"
    return f"{int(x)}"


def _fmt_signed(x: float | None) -> str:
    if x is None:
        return "—"
    return f"{x:+.0f}"


def _rank_line(entries: list[dict[str, Any]]) -> str:
    if not entries:
        return "Sin datos de ranked."
    parts: list[str] = []
    for e in entries:
        qtype = e.get("queueType", "")
        tier = e.get("tier", "?")
        rank = e.get("rank", "")
        lp = e.get("leaguePoints", 0)
        wins = e.get("wins", 0)
        losses = e.get("losses", 0)
        total = wins + losses
        wr = (wins / total) if total else 0.0
        label = (
            "Solo/Duo"
            if qtype == "RANKED_SOLO_5x5"
            else "Flex" if qtype == "RANKED_FLEX_SR" else qtype
        )
        parts.append(
            f"- **{label}**: {tier} {rank} ({lp} LP) — "
            f"{wins}W/{losses}L ({wr * 100:.1f}% WR)"
        )
    return "\n".join(parts)


def build_report(
    player: PlayerData,
    overall: dict[str, Any],
    champion_pool: list[dict[str, Any]],
    roles: list[dict[str, Any]],
    playstyle: dict[str, Any],
    duo_partners: list[dict[str, Any]],
    champion_synergies: list[dict[str, Any]],
    matchups: dict[str, Any],
    weaknesses: dict[str, Any],
    *,
    ally_champions: dict[str, Any] | None = None,
    team_comps: dict[str, Any] | None = None,
    queues: list[int],
    count: int,
    role_filter: str | None = None,
    global_overall: dict[str, Any] | None = None,
    global_role_stats: list[dict[str, Any]] | None = None,
    role_advanced: list[dict[str, Any]] | None = None,
    tier_a: dict[str, Any] | None = None,
    game_phases: dict[str, Any] | None = None,
    rank_key: str | None = None,
    rank_source: str | None = None,
    rank_source_label: str | None = None,
) -> str:
    """Construye el reporte completo en Markdown.

    Si `role_filter` esta seteado, los analytics deberian venir calculados
    sobre el subset filtrado a ese rol; `global_overall` y `global_role_stats`
    aportan la comparativa contra el set completo, y `role_advanced` agrega
    una seccion adicional con las metricas pre-calculadas de Riot especificas
    del rol.

    `game_phases` (siempre presente cuando se llama desde main.py) trae los
    scores 1-10 para early / mid / late game y se renderiza como seccion 5.
    """
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    queue_labels = ", ".join(QUEUE_NAMES.get(q, str(q)) for q in queues)
    role_label = ROLE_DISPLAY.get(role_filter or "", role_filter or "")

    show_phases = game_phases is not None
    show_advanced = bool(role_advanced)
    # Las secciones 5-12 originales se desplazan por cada seccion insertada.
    inserted = (1 if show_phases else 0) + (1 if show_advanced else 0)

    def _n(num: int) -> int:
        """Numero de seccion ajustado: las secciones 5+ del set original
        se desplazan por las secciones insertadas (phases siempre, advanced
        cuando hay role_filter)."""
        return num if num < 5 else num + inserted

    # Numeros para las secciones insertadas (cuando aplican).
    phases_section_n = 5
    advanced_section_n = 5 + (1 if show_phases else 0)

    parts: list[str] = []

    title = f"# Reporte LoL — {player.riot_id}"
    if role_filter:
        title += f" (rol: {role_label})"
    parts.append(title)
    parts.append("")
    parts.append(f"_Generado: {now}_")
    parts.append(f"_Colas: {queue_labels} | Partidas pedidas por cola: {count}_")
    if rank_key:
        rank_label = rank_display(rank_key)
        if rank_source_label:
            parts.append(
                f"_Baselines: comparado vs **{rank_label}** "
                f"({rank_source_label}). "
                f"Editables en `data/baselines.json`._"
            )
        else:
            parts.append(
                f"_Baselines: comparado vs **{rank_label}**. "
                f"Editables en `data/baselines.json`._"
            )
    if role_filter:
        last_section = _n(12)
        parts.append(
            f"_Filtrado a partidas como **{role_label}** ({role_filter}). "
            f"Todos los analytics de las secciones 2-{last_section} estan "
            f"calculados solo sobre ese subset._"
        )
    parts.append("")

    parts.append("## 1. Resumen")
    parts.append("")
    parts.append(_rank_line(player.league_entries))
    parts.append("")

    if role_filter and global_overall is not None:
        gn = int(global_overall.get("games", 0))
        rn = int(overall.get("games", 0))
        share = (rn / gn) if gn else 0.0
        parts.append(
            f"### Comparativa: en **{role_label}** vs **Global** (todos los roles)"
        )
        parts.append("")
        parts.append(
            f"_En {role_label} jugaste **{rn}** de **{gn}** partidas "
            f"({share * 100:.1f}% de tu pool)._"
        )
        parts.append("")
        parts.append(
            f"| Métrica | En {role_label} (n={rn}) | "
            f"Global (n={gn}) | Δ |"
        )
        parts.append("|---|---:|---:|---:|")
        rows = [
            ("Winrate", overall.get("winrate"), global_overall.get("winrate"), "pct"),
            ("KDA", overall.get("kda"), global_overall.get("kda"), 2),
            (
                "Kills (avg)",
                overall.get("kills_avg"),
                global_overall.get("kills_avg"),
                1,
            ),
            (
                "Deaths (avg)",
                overall.get("deaths_avg"),
                global_overall.get("deaths_avg"),
                1,
            ),
            (
                "Assists (avg)",
                overall.get("assists_avg"),
                global_overall.get("assists_avg"),
                1,
            ),
            (
                "CS/min",
                overall.get("cs_per_min"),
                global_overall.get("cs_per_min"),
                2,
            ),
            (
                "Daño/min",
                overall.get("dmg_per_min"),
                global_overall.get("dmg_per_min"),
                0,
            ),
            (
                "Vision avg",
                overall.get("vision_avg"),
                global_overall.get("vision_avg"),
                1,
            ),
        ]
        for label, role_v, glob_v, fmt in rows:
            if fmt == "pct":
                rs, gs = _fmt_pct(role_v), _fmt_pct(glob_v)
                if role_v is not None and glob_v is not None:
                    delta_s = f"{(role_v - glob_v) * 100:+.1f}pp"
                else:
                    delta_s = "—"
            else:
                rs = _fmt_num(role_v, fmt)
                gs = _fmt_num(glob_v, fmt)
                if role_v is not None and glob_v is not None:
                    delta = role_v - glob_v
                    if fmt == 0:
                        delta_s = f"{delta:+.0f}"
                    else:
                        delta_s = f"{delta:+.{fmt}f}"
                else:
                    delta_s = "—"
            parts.append(f"| {label} | {rs} | {gs} | {delta_s} |")
        parts.append("")

        if global_role_stats:
            parts.append("### Distribución entre tus roles (set completo)")
            parts.append("")
            parts.append("| Rol | Games | WR | KDA | CS/m | DPM |")
            parts.append("|---|---:|---:|---:|---:|---:|")
            for r in global_role_stats:
                marker = " (filtrado)" if r["role"] == role_filter else ""
                parts.append(
                    f"| {r['role_display']}{marker} | {r['games']} | "
                    f"{_fmt_pct(r['winrate'])} | {_fmt_num(r['kda'], 2)} | "
                    f"{_fmt_num(r['cs_per_min'], 2)} | "
                    f"{_fmt_num(r['dmg_per_min'], 0)} |"
                )
            parts.append("")

    parts.append(
        f"- **Partidas analizadas:** {overall['games']} "
        f"({overall['wins']}W / {overall['losses']}L)"
    )
    parts.append(f"- **Winrate:** {_fmt_pct(overall['winrate'])}")
    parts.append(
        f"- **KDA promedio:** {_fmt_num(overall['kda'], 2)} "
        f"({_fmt_num(overall['kills_avg'])}/"
        f"{_fmt_num(overall['deaths_avg'])}/"
        f"{_fmt_num(overall['assists_avg'])})"
    )
    parts.append(f"- **CS/min:** {_fmt_num(overall['cs_per_min'], 2)}")
    parts.append(f"- **Daño a campeones / min:** {_fmt_num(overall['dmg_per_min'], 0)}")
    parts.append(f"- **Vision score promedio:** {_fmt_num(overall['vision_avg'])}")
    parts.append("")

    parts.append("## 2. Champion pool (top 12 por partidas)")
    parts.append("")
    if not champion_pool:
        parts.append("_Sin datos._")
    else:
        parts.append(
            "| Campeón | Games | W-L | WR | KDA | CS/m | DPM | Dmg share | Vision |"
        )
        parts.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|")
        for r in champion_pool[:12]:
            parts.append(
                f"| {r['champion']} | {r['games']} | "
                f"{r['wins']}-{r['losses']} | {_fmt_pct(r['winrate'])} | "
                f"{_fmt_num(r['kda'], 2)} | {_fmt_num(r['cs_per_min'], 2)} | "
                f"{_fmt_num(r['dmg_per_min'], 0)} | "
                f"{_fmt_pct(r['dmg_share'])} | {_fmt_num(r['vision_avg'])} |"
            )
    parts.append("")

    parts.append("## 3. Distribución y rendimiento por rol")
    parts.append("")
    if role_filter:
        parts.append(
            f"_Reporte filtrado al rol **{role_label}** — la distribución "
            f"completa de roles está en la mini-tabla de la sección 1._"
        )
        parts.append("")
    elif not roles:
        parts.append("_Sin datos._")
    else:
        parts.append("| Rol | Games | WR | KDA | CS/m | DPM | Vision |")
        parts.append("|---|---:|---:|---:|---:|---:|---:|")
        for r in roles:
            parts.append(
                f"| {r['role_display']} | {r['games']} | "
                f"{_fmt_pct(r['winrate'])} | {_fmt_num(r['kda'], 2)} | "
                f"{_fmt_num(r['cs_per_min'], 2)} | "
                f"{_fmt_num(r['dmg_per_min'], 0)} | "
                f"{_fmt_num(r['vision_avg'])} |"
            )
    parts.append("")

    parts.append("## 4. Playstyle (timeline) vs baseline")
    parts.append("")
    by_role = playstyle.get("by_role", [])
    if not by_role:
        parts.append("_Sin timelines disponibles._")
    else:
        for row in by_role:
            base = row.get("baseline") or {}
            parts.append(f"### {row['role_display']} (n={row['sample_size']})")
            parts.append("")
            parts.append("| Métrica | Real | Baseline | Δ |")
            parts.append("|---|---:|---:|---:|")

            def _delta(actual: float | None, target: float | None) -> str:
                if actual is None or target is None or target == 0:
                    return "—"
                ratio = (actual / target) - 1.0
                return f"{ratio * 100:+.1f}%"

            metrics_rows = [
                ("CS@10", row.get("cs10"), base.get("cs10"), 1),
                ("CS@15", row.get("cs15"), base.get("cs15"), 1),
                ("Gold@15", row.get("gold15"), None, 0),
                ("Gold diff @10", row.get("gold_diff10"), None, 0),
                ("Gold diff @15", row.get("gold_diff15"), None, 0),
                ("CS diff @15", row.get("cs_diff15"), None, 1),
                ("KP", row.get("kp"), base.get("kp"), 2),
                ("DPM", row.get("dpm"), base.get("dpm"), 0),
                ("Vision/min", row.get("vspm"), base.get("vspm"), 2),
            ]
            for label, actual, target, dec in metrics_rows:
                if "diff" in label.lower():
                    actual_s = _fmt_signed(actual)
                elif label == "KP":
                    actual_s = _fmt_pct(actual)
                else:
                    actual_s = _fmt_num(actual, dec)
                if target is None:
                    target_s = "—"
                elif label == "KP":
                    target_s = _fmt_pct(target)
                else:
                    target_s = _fmt_num(target, dec)
                parts.append(
                    f"| {label} | {actual_s} | {target_s} | "
                    f"{_delta(actual, target)} |"
                )
            parts.append("")

    if show_phases:
        gp = game_phases or {}
        parts.append(
            f"## {phases_section_n}. Análisis por fase del juego "
            f"(early / mid / late)"
        )
        parts.append("")
        parts.append(
            "_Cada fase se puntúa de **1 a 10** promediando varias métricas "
            "clave vs sus baselines (ajustadas al rol del jugador en cada "
            "partida). Score **5** = en línea con el baseline (jugador "
            "promedio); **>7** = sobre la media; **<3** = por debajo. "
            "**N** = partidas que aportaron a esa métrica._"
        )
        parts.append("")
        parts.append("**Definiciones de fase:**")
        parts.append("")
        parts.append("- **Early** = 0-15' (laning phase).")
        parts.append("- **Mid** = 15-25' (objetivos, primeras peleas grandes).")
        parts.append("- **Late** = 25'+ (baron / soul / cierre).")
        parts.append("")

        long_n = int(gp.get("long_games_n", 0))
        total_n = int(gp.get("total_games", 0))

        def _fmt_score(s: float | None) -> str:
            return "—" if s is None else f"**{s:.1f} / 10**"

        parts.append("### Resumen")
        parts.append("")
        parts.append("| Fase | Score | Métricas |")
        parts.append("|---|---:|---:|")
        for key in ("early", "mid", "late"):
            phase = gp.get(key) or {}
            mcount = len(phase.get("metrics") or [])
            parts.append(
                f"| {phase.get('label', key)} | "
                f"{_fmt_score(phase.get('score'))} | {mcount} |"
            )
        parts.append("")
        if total_n > 0:
            long_share = (long_n / total_n) if total_n else 0.0
            parts.append(
                f"_Partidas analizadas: **{total_n}** — de las cuales "
                f"**{long_n}** llegaron a 25'+ ({long_share * 100:.1f}%). "
                f"Los scores de **late game** se calculan solo sobre ese "
                f"subset._"
            )
            parts.append("")

        for key in ("early", "mid", "late"):
            phase = gp.get(key) or {}
            phase_label = phase.get("label", key)
            phase_score = phase.get("score")
            phase_metrics = phase.get("metrics") or []
            parts.append(
                f"### {phase_label} — Score: {_fmt_score(phase_score)}"
            )
            parts.append("")
            if not phase_metrics:
                parts.append(
                    "_Sin datos suficientes en la muestra para puntuar "
                    "esta fase._"
                )
                parts.append("")
                continue

            parts.append("| Métrica | Valor | Target | Score | N |")
            parts.append("|---|---:|---:|---:|---:|")
            for m in phase_metrics:
                fmt = m.get("fmt", "decimal")
                v = m.get("value")
                t = m.get("target")
                if fmt == "pct":
                    v_s = _fmt_pct(v)
                    t_s = _fmt_pct(t)
                elif fmt == "int":
                    v_s = _fmt_int(v)
                    t_s = _fmt_int(t)
                elif fmt == "signed":
                    v_s = _fmt_signed(v)
                    t_s = _fmt_signed(t) if t is not None else "0"
                else:  # decimal
                    v_s = _fmt_num(v, 2)
                    t_s = _fmt_num(t, 2)
                score = m.get("score")
                score_s = "—" if score is None else f"{score:.1f}"
                parts.append(
                    f"| {m['label']} | {v_s} | {t_s} | {score_s} | "
                    f"{m.get('n', 0)} |"
                )
            parts.append("")

    if show_advanced:
        parts.append(
            f"## {advanced_section_n}. Stats avanzadas para {role_label} "
            f"(Riot challenges)"
        )
        parts.append("")
        parts.append(
            "_Metricas pre-calculadas por Riot en el campo "
            "`participants[i].challenges` y top-level del match. Especificas "
            f"para **{role_label}**: lo que un coach de este rol mira primero. "
            "**N** = partidas donde la metrica esta presente (puede ser menor "
            "al total si depende del campeon o de condiciones especificas)._"
        )
        parts.append("")
        if not role_advanced:
            parts.append("_Sin datos disponibles._")
            parts.append("")
        else:
            parts.append("| Metrica | Promedio | Total | Min | Max | N |")
            parts.append("|---|---:|---:|---:|---:|---:|")
            for m in role_advanced:
                disp = m.get("display", "decimal")
                if m["n"] == 0:
                    parts.append(
                        f"| {m['label']} | — | — | — | — | 0 |"
                    )
                    continue

                def _fmt(v: float | None) -> str:
                    if v is None:
                        return "—"
                    if disp == "pct":
                        return f"{v * 100:.1f}%"
                    if disp == "int":
                        return f"{v:.0f}"
                    if disp == "signed":
                        return f"{v:+.1f}"
                    return f"{v:.2f}"

                parts.append(
                    f"| {m['label']} | {_fmt(m['mean'])} | "
                    f"{_fmt(m['total'])} | {_fmt(m['min'])} | "
                    f"{_fmt(m['max'])} | {m['n']} |"
                )
            parts.append("")

            hints_with_text = [m for m in role_advanced if m.get("hint")]
            if hints_with_text:
                parts.append("**Notas sobre las metricas:**")
                parts.append("")
                for m in hints_with_text:
                    parts.append(f"- _{m['label']}_: {m['hint']}")
                parts.append("")

        # === Tier A: Analisis cruzado (sub-seccion del rol) ===
        if tier_a and tier_a.get("blocks"):
            parts.append(
                f"### {advanced_section_n}.1 Análisis cruzado "
                f"(splits y synergies de {role_label})"
            )
            parts.append("")
            parts.append(
                "_Métricas que cruzan dos sub-grupos de partidas para revelar "
                "patrones que el promedio agregado oculta (ej. WR cuando "
                "roameas vs cuando no, KDA en partidas largas vs cortas)._"
            )
            parts.append("")
            for block in tier_a["blocks"]:
                parts.append(f"**{block['label']}** — {block['summary']}")
                parts.append("")
                rows = block.get("rows") or []
                if rows:
                    parts.append("| Sub-grupo | WR | KDA | N |")
                    parts.append("|---|---:|---:|---:|")
                    for r in rows:
                        wr_s = _fmt_pct(r.get("wr"))
                        kda_v = r.get("kda")
                        kda_s = (
                            f"{kda_v:.2f}"
                            if isinstance(kda_v, (int, float))
                            else "—"
                        )
                        parts.append(
                            f"| {r.get('label', '')} | {wr_s} | "
                            f"{kda_s} | {r.get('n', 0)} |"
                        )
                    parts.append("")
                metric_value = block.get("metric_value")
                metric_label = block.get("metric_label")
                if metric_value is not None and metric_label:
                    if isinstance(metric_value, (int, float)):
                        parts.append(
                            f"_{metric_label}_: **{metric_value:.2f}**"
                        )
                    else:
                        parts.append(f"_{metric_label}_: **{metric_value}**")
                    parts.append("")
                interp = block.get("interpretation")
                if interp:
                    parts.append(f"_Interpretación_: {interp}")
                    parts.append("")

    parts.append(f"## {_n(5)}. Fortalezas detectadas")
    parts.append("")
    strong_champs = [
        r for r in champion_pool if r["games"] >= 5 and r["winrate"] >= 0.55
    ]
    if strong_champs:
        parts.append("**Campeones con >= 55% WR (mín. 5 partidas):**")
        parts.append("")
        for r in strong_champs[:10]:
            parts.append(
                f"- **{r['champion']}** — {r['games']} games, "
                f"{_fmt_pct(r['winrate'])} WR, KDA {_fmt_num(r['kda'], 2)}"
            )
        parts.append("")
    else:
        parts.append("_Sin campeones con >= 55% WR y muestra mínima de 5._")
        parts.append("")

    parts.append(f"## {_n(6)}. Debilidades detectadas")
    parts.append("")
    low_champs = [
        r for r in champion_pool if r["games"] >= 5 and r["winrate"] < 0.40
    ]
    if low_champs:
        parts.append("**Campeones con WR < 40% (mín. 5 partidas):**")
        parts.append("")
        for r in low_champs[:10]:
            parts.append(
                f"- **{r['champion']}** — {r['games']} games, "
                f"{_fmt_pct(r['winrate'])} WR, KDA {_fmt_num(r['kda'], 2)}"
            )
        parts.append("")
    metric_deficits = weaknesses.get("metric_deficits", [])
    if metric_deficits:
        parts.append("**Métricas bajo baseline:**")
        parts.append("")
        for row in metric_deficits:
            for d in row["deficits"]:
                parts.append(
                    f"- {row['role_display']} | {d['metric']}: "
                    f"{_fmt_num(d['actual'], 2)} vs baseline "
                    f"{_fmt_num(d['target'], 2)} ({(d['ratio'] - 1) * 100:+.1f}%)"
                )
        parts.append("")
    loss_patterns = weaknesses.get("loss_patterns", {})
    if loss_patterns.get("losses", 0) > 0 and loss_patterns.get("wins", 0) > 0:
        win_p = loss_patterns["in_wins"]
        loss_p = loss_patterns["in_losses"]
        parts.append("**Diferencias entre wins y losses (promedio por partida):**")
        parts.append("")
        parts.append("| Métrica | En victorias | En derrotas | Δ |")
        parts.append("|---|---:|---:|---:|")
        for label, key in [
            ("Kills", "kills_avg"),
            ("Deaths", "deaths_avg"),
            ("Assists", "assists_avg"),
            ("KP", "kp_avg"),
            ("Vision", "vision_avg"),
            ("Dmg a champs", "dmg_avg"),
            ("Dmg recibido", "dmg_taken_avg"),
        ]:
            w = win_p.get(key, 0)
            l = loss_p.get(key, 0)
            if key == "kp_avg":
                ws, ls = _fmt_pct(w), _fmt_pct(l)
            elif key in ("dmg_avg", "dmg_taken_avg"):
                ws, ls = _fmt_num(w, 0), _fmt_num(l, 0)
            else:
                ws, ls = _fmt_num(w, 2), _fmt_num(l, 2)
            delta = w - l
            if key in ("dmg_avg", "dmg_taken_avg"):
                delta_s = f"{delta:+.0f}"
            elif key == "kp_avg":
                delta_s = f"{delta * 100:+.1f}pp"
            else:
                delta_s = f"{delta:+.2f}"
            parts.append(f"| {label} | {ws} | {ls} | {delta_s} |")
        parts.append("")
    if (
        not low_champs
        and not metric_deficits
    ):
        parts.append("_No se detectaron debilidades claras con la muestra actual._")
        parts.append("")

    parts.append(
        f"## {_n(7)}. Matchups vs campeones (top 5 best / top 5 worst)"
    )
    parts.append("")
    best_mu = matchups.get("best") or []
    worst_mu = matchups.get("worst") or []
    if not best_mu and not worst_mu:
        parts.append(
            "_Sin matchups con muestra suficiente (mín. 3 enfrentamientos)._"
        )
        parts.append("")
    if best_mu:
        parts.append("### Top 5 mejor WR vs oponente")
        parts.append("")
        parts.append(
            "| Yo | vs | Games | WR | KDA | K/D/A | DPM | CS/m |"
        )
        parts.append("|---|---|---:|---:|---:|---:|---:|---:|")
        for r in best_mu:
            parts.append(
                f"| {r['my_champion']} | {r['opponent']} | {r['games']} | "
                f"{_fmt_pct(r['winrate'])} | {_fmt_num(r['kda'], 2)} | "
                f"{_fmt_num(r['kills_avg'])}/{_fmt_num(r['deaths_avg'])}/"
                f"{_fmt_num(r['assists_avg'])} | "
                f"{_fmt_num(r['dpm'], 0)} | {_fmt_num(r['cs_per_min'], 2)} |"
            )
        parts.append("")
    if worst_mu:
        parts.append("### Top 5 peor WR vs oponente")
        parts.append("")
        parts.append(
            "| Yo | vs | Games | WR | KDA | K/D/A | DPM | CS/m |"
        )
        parts.append("|---|---|---:|---:|---:|---:|---:|---:|")
        for r in worst_mu:
            parts.append(
                f"| {r['my_champion']} | {r['opponent']} | {r['games']} | "
                f"{_fmt_pct(r['winrate'])} | {_fmt_num(r['kda'], 2)} | "
                f"{_fmt_num(r['kills_avg'])}/{_fmt_num(r['deaths_avg'])}/"
                f"{_fmt_num(r['assists_avg'])} | "
                f"{_fmt_num(r['dpm'], 0)} | {_fmt_num(r['cs_per_min'], 2)} |"
            )
        parts.append("")

    parts.append(f"## {_n(8)}. Aliados frecuentes (campeones en mi equipo)")
    parts.append("")
    parts.append(
        "_Cuando el campeón **X** estuvo en mi equipo (sin importar quién lo "
        "jugaba), ¿gané?_ Mín. 5 partidas. KDA mostrado es el **mío** en esas "
        "partidas."
    )
    parts.append("")
    ac = ally_champions or {}
    best_ac = ac.get("best") or []
    worst_ac = ac.get("worst") or []
    if not best_ac and not worst_ac:
        parts.append("_Sin aliados con muestra suficiente._")
        parts.append("")
    if best_ac:
        parts.append("### Top 5 aliados con mejor WR conmigo")
        parts.append("")
        parts.append("| Aliado | Games | WR | Mi KDA | Mi K/D/A |")
        parts.append("|---|---:|---:|---:|---:|")
        for r in best_ac:
            parts.append(
                f"| {r['ally_champion']} | {r['games']} | "
                f"{_fmt_pct(r['winrate'])} | {_fmt_num(r['my_kda'], 2)} | "
                f"{_fmt_num(r['my_kills_avg'])}/"
                f"{_fmt_num(r['my_deaths_avg'])}/"
                f"{_fmt_num(r['my_assists_avg'])} |"
            )
        parts.append("")
    if worst_ac:
        parts.append("### Top 5 aliados con peor WR conmigo")
        parts.append("")
        parts.append("| Aliado | Games | WR | Mi KDA | Mi K/D/A |")
        parts.append("|---|---:|---:|---:|---:|")
        for r in worst_ac:
            parts.append(
                f"| {r['ally_champion']} | {r['games']} | "
                f"{_fmt_pct(r['winrate'])} | {_fmt_num(r['my_kda'], 2)} | "
                f"{_fmt_num(r['my_kills_avg'])}/"
                f"{_fmt_num(r['my_deaths_avg'])}/"
                f"{_fmt_num(r['my_assists_avg'])} |"
            )
        parts.append("")

    parts.append(f"## {_n(9)}. Composiciones de equipo (drafts repetidos)")
    parts.append("")
    tc = team_comps or {}
    tc_min = tc.get("min_games", 4)
    parts.append(
        f"_Mismo set exacto de 5 campeones aliados (incluyéndome) repetido "
        f"≥{tc_min} veces. Total de comps únicas: {tc.get('total_unique', 0)}._"
    )
    parts.append("")
    best_tc = tc.get("best") or []
    worst_tc = tc.get("worst") or []
    if not best_tc and not worst_tc:
        parts.append(
            "_No hubo composiciones de 5 campeones repetidas el mínimo de "
            f"{tc_min} veces. Es esperable con muestras chicas o pool diverso._"
        )
        parts.append("")
    if best_tc:
        parts.append("### Mejor draft (top 5 por WR)")
        parts.append("")
        parts.append("| Composición (5 campeones) | Games | WR |")
        parts.append("|---|---:|---:|")
        for r in best_tc:
            parts.append(
                f"| {', '.join(r['champions'])} | {r['games']} | "
                f"{_fmt_pct(r['winrate'])} |"
            )
        parts.append("")
    if worst_tc:
        parts.append("### Peor draft (top 5 por menor WR)")
        parts.append("")
        parts.append("| Composición (5 campeones) | Games | WR |")
        parts.append("|---|---:|---:|")
        for r in worst_tc:
            parts.append(
                f"| {', '.join(r['champions'])} | {r['games']} | "
                f"{_fmt_pct(r['winrate'])} |"
            )
        parts.append("")

    parts.append(f"## {_n(10)}. Sinergias con personas (duo partners)")
    parts.append("")
    if not duo_partners:
        parts.append(
            "_No hay aliados con >= 5 partidas en común. "
            "Aumentá `--count` o jugá más en duo._"
        )
    else:
        parts.append("| Aliado | Games | WR | Top campeones |")
        parts.append("|---|---:|---:|---|")
        for d in duo_partners[:15]:
            champs = ", ".join(
                f"{c['champion']} ({c['games']})" for c in d["top_champs"]
            )
            parts.append(
                f"| {d['display_name']} | {d['games']} | "
                f"{_fmt_pct(d['winrate'])} | {champs} |"
            )
    parts.append("")

    parts.append(f"## {_n(11)}. Sinergias de campeones (mi champ + aliado)")
    parts.append("")
    parts.append(
        "_Pares (yo juego X, aliado juega Y) con muestra suficiente. "
        "Se diferencia de la sección 8: acá los pares son específicos a "
        "mi pick + aliado._"
    )
    parts.append("")
    if not champion_synergies:
        parts.append("_Sin combos con muestra suficiente._")
    else:
        top_synergies = champion_synergies[:15]
        parts.append("| Yo juego | Aliado juega | Games | WR |")
        parts.append("|---|---|---:|---:|")
        for r in top_synergies:
            parts.append(
                f"| {r['my_champion']} | {r['ally_champion']} | "
                f"{r['games']} | {_fmt_pct(r['winrate'])} |"
            )
    parts.append("")

    parts.append(f"## {_n(12)}. Conclusión rápida (5 preguntas para el LLM)")
    parts.append("")
    parts.append(
        "Este reporte está optimizado para que un LLM lo interprete. "
        "Abrí este archivo en Cursor y pegá el siguiente prompt en el chat:"
    )
    parts.append("")

    # Cuando hay --role, usamos el prompt rol-especifico de prompts.py.
    # Sin --role, mantenemos el prompt generico inline (5 preguntas).
    if role_filter:
        # cross_section_n: si hay tier_a, las metricas Tier A viven en la
        # sub-seccion {advanced_section_n}.1; si no, los prompts referencian
        # {advanced_section_n} a secas y el LLM dira "no medido aun".
        cross_section_n = (
            f"{advanced_section_n}.1" if (tier_a and tier_a.get("blocks"))
            else str(advanced_section_n)
        )
        role_prompt = render_role_prompt(
            role_filter,
            role_label=role_label,
            advanced_section_n=advanced_section_n,
            phases_section_n=phases_section_n,
            cross_section_n=cross_section_n,
            matchups_section_n=_n(7),
            duo_section_n=_n(10),
        )
        if role_prompt is not None:
            parts.append(role_prompt.rstrip("\n"))
            parts.append("")
            return "\n".join(parts) + "\n"
        # Fallback: si por algun motivo no se renderiza el rol-especifico,
        # caemos al generico (mantiene el comportamiento previo).
        parts.append(
            f"> Este reporte está **filtrado al rol {role_label} ({role_filter})**. "
            f"Todas las stats reflejan solo las partidas del jugador en ese rol; "
            f"la sección 1 trae además una comparativa contra el global y la "
            f"distribución entre todos los roles. Tu coaching debe estar "
            f"contextualizado al rol {role_label}."
        )
        parts.append("> ")
    parts.append("> Actuá como coach senior de League of Legends. Basándote ")
    parts.append("> **exclusivamente** en los datos de este reporte, respondé ")
    parts.append("> con **una oración muy breve cada uno**:")
    parts.append("> ")
    parts.append(
        "> 1. **¿Juega bien su línea?** (citar CS@10/15, gold diff @10/15, "
        "CS diff @15 de la sección 4 — Playstyle, **y el score de Early "
        f"game de la sección {phases_section_n}**"
        + (
            f", y Lane phase win rate + Lane lead promedio @14' de la "
            f"sección {phases_section_n} (Early), y max CS lead vs rival "
            f"de la sección {advanced_section_n} — Stats avanzadas para "
            f"{role_label}"
            if show_advanced
            else (
                f", y Lane phase win rate + Lane lead promedio @14' de la "
                f"sección {phases_section_n} (Early)"
            )
        )
        + ")."
    )
    parts.append(
        "> 2. **¿Hace lo que tiene que hacer en su rol?** (citar KP, DPM, "
        "Vision/min vs baseline de la sección 4, **y los scores de Mid y "
        f"Late de la sección {phases_section_n}**"
        + (
            f", y las metricas especificas de {role_label} de la sección "
            f"{advanced_section_n}"
            if show_advanced
            else ""
        )
        + ")."
    )
    parts.append(
        "> 3. **Mejores 3 y peores 3 campeones** (de la sección 2 — "
        "Champion pool, mín. 5 games)."
    )
    parts.append(
        f"> 4. **Mejor duo** (sección {_n(10)} — Duo partners, mayor WR "
        "con muestra suficiente)."
    )
    parts.append(
        f"> 5. **Mejor DuoChamp** (sección {_n(11)} — Sinergias de "
        "campeones, mayor WR del par yo+aliado)."
    )
    parts.append("> ")
    parts.append("> Después agregá:")
    if show_phases:
        parts.append(
            f"> - **Fase del juego más fuerte y más débil**: leer los 3 scores "
            f"(early/mid/late) de la sección {phases_section_n} y decir cuál "
            f"es la mejor y cuál la peor del jugador, citando el score y la "
            f"métrica que más arrastra para abajo en la peor fase."
        )
    parts.append(
        f"> - **% victoria y stats vs champs**: resumir top 5 mejores y "
        f"peores matchups de la sección {_n(7)}."
    )
    parts.append(
        f"> - **Mejor champ en conjunto**: top 5 y bottom 5 aliados de "
        f"la sección {_n(8)}."
    )
    parts.append(
        f"> - **Mejor draft**: best y worst de la sección {_n(9)} (si hay)."
    )
    if show_advanced:
        parts.append(
            f"> - **Stats avanzadas de {role_label}**: leer la sección "
            f"{advanced_section_n} y senalar las 3 metricas mas fuertes y las "
            f"3 mas debiles, con interpretacion contextual al rol."
        )
    parts.append(
        "> - **Conclusión general**: 1 oración muy breve sintetizando "
        "las 5 preguntas anteriores."
    )
    parts.append("> ")
    parts.append(
        "> No inventes datos: si algo no está en el reporte, decí "
        "**\"insuficientes datos\"**."
    )
    parts.append("")

    return "\n".join(parts) + "\n"


__all__ = ["build_report"]
