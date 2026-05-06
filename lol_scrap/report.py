"""Ensambla el reporte Markdown final pensado para ser interpretado por Cursor."""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from .config import QUEUE_NAMES
from .fetcher import PlayerData


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
) -> str:
    """Construye el reporte completo en Markdown."""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    queue_labels = ", ".join(QUEUE_NAMES.get(q, str(q)) for q in queues)

    parts: list[str] = []

    parts.append(f"# Reporte LoL — {player.riot_id}")
    parts.append("")
    parts.append(f"_Generado: {now}_")
    parts.append(f"_Colas: {queue_labels} | Partidas pedidas por cola: {count}_")
    parts.append("")

    parts.append("## 1. Resumen")
    parts.append("")
    parts.append(_rank_line(player.league_entries))
    parts.append("")
    parts.append(
        f"- **Partidas analizadas:** {overall['games']} "
        f"({overall['wins']}W / {overall['losses']}L)"
    )
    parts.append(f"- **Winrate global:** {_fmt_pct(overall['winrate'])}")
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
    if not roles:
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

    parts.append("## 5. Fortalezas detectadas")
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

    parts.append("## 6. Debilidades detectadas")
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

    parts.append("## 7. Matchups vs campeones (top 5 best / top 5 worst)")
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

    parts.append("## 8. Aliados frecuentes (campeones en mi equipo)")
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

    parts.append("## 9. Composiciones de equipo (drafts repetidos)")
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

    parts.append("## 10. Sinergias con personas (duo partners)")
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

    parts.append("## 11. Sinergias de campeones (mi champ + aliado)")
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

    parts.append("## 12. Conclusión rápida (5 preguntas para el LLM)")
    parts.append("")
    parts.append(
        "Este reporte está optimizado para que un LLM lo interprete. "
        "Abrí este archivo en Cursor y pegá el siguiente prompt en el chat:"
    )
    parts.append("")
    parts.append("> Actuá como coach senior de League of Legends. Basándote ")
    parts.append("> **exclusivamente** en los datos de este reporte, respondé ")
    parts.append("> con **una oración muy breve cada uno**:")
    parts.append("> ")
    parts.append("> 1. **¿Juega bien su línea?** (citar CS@10/15, gold diff @10/15, ")
    parts.append("> CS diff @15 de la sección 4 — Playstyle).")
    parts.append("> 2. **¿Hace lo que tiene que hacer en su rol?** (citar KP, DPM, ")
    parts.append("> Vision/min vs baseline de la sección 4).")
    parts.append("> 3. **Mejores 3 y peores 3 campeones** (de la sección 2 — ")
    parts.append("> Champion pool, mín. 5 games).")
    parts.append("> 4. **Mejor duo** (sección 10 — Duo partners, mayor WR con ")
    parts.append("> muestra suficiente).")
    parts.append("> 5. **Mejor DuoChamp** (sección 11 — Sinergias de campeones, ")
    parts.append("> mayor WR del par yo+aliado).")
    parts.append("> ")
    parts.append("> Después agregá:")
    parts.append("> - **% victoria y stats vs champs**: resumir top 5 mejores y ")
    parts.append("> peores matchups de la sección 7.")
    parts.append("> - **Mejor champ en conjunto**: top 5 y bottom 5 aliados de ")
    parts.append("> la sección 8.")
    parts.append("> - **Mejor draft**: best y worst de la sección 9 (si hay).")
    parts.append("> - **Conclusión general**: 1 oración muy breve sintetizando ")
    parts.append("> las 5 preguntas anteriores.")
    parts.append("> ")
    parts.append(
        "> No inventes datos: si algo no está en el reporte, decí "
        "**\"insuficientes datos\"**."
    )
    parts.append("")

    return "\n".join(parts) + "\n"


__all__ = ["build_report"]
