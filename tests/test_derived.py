"""Tests para los modulos de stats derivadas y prompts rol-especificos.

Standalone con `unittest`: corre con `python -m unittest tests/test_derived.py`.
"""
from __future__ import annotations

import unittest

from lol_scrap.analytics.derived_aggregations import compute_tier_a
from lol_scrap.analytics.derived_metrics import compute_tier_b, compute_tier_s
from lol_scrap.analytics.timeline_events import (
    player_deaths,
    player_id_for_puuid,
    player_level_ups,
)
from lol_scrap.prompts import ROLE_PROMPTS, render_role_prompt


# ============================================================
# Helpers para construir matches y timelines sinteticos
# ============================================================


def _mk_participant(
    *,
    puuid: str = "PUUID_X",
    pid: int = 1,
    team_id: int = 100,
    team_position: str = "BOTTOM",
    win: bool = True,
    dmg_to_champs: float = 18000,
    dmg_taken: float = 15000,
    dmg_to_turrets: float = 1500,
    vision_score: int = 24,
    kills: int = 5,
    deaths: int = 3,
    assists: int = 7,
    challenges: dict | None = None,
) -> dict:
    return {
        "puuid": puuid,
        "participantId": pid,
        "teamId": team_id,
        "teamPosition": team_position,
        "win": win,
        "totalDamageDealtToChampions": dmg_to_champs,
        "totalDamageTaken": dmg_taken,
        "damageDealtToTurrets": dmg_to_turrets,
        "visionScore": vision_score,
        "kills": kills,
        "deaths": deaths,
        "assists": assists,
        "championName": "Jinx",
        "challenges": challenges or {},
    }


def _mk_match(
    *,
    match_id: str = "M1",
    duration_s: int = 1800,
    me: dict | None = None,
    other_participants: list[dict] | None = None,
) -> dict:
    me = me or _mk_participant()
    other_participants = other_participants or []
    return {
        "metadata": {"matchId": match_id},
        "info": {
            "gameDuration": duration_s,
            "participants": [me] + other_participants,
        },
    }


def _mk_timeline(
    *,
    puuid: str = "PUUID_X",
    pid: int = 1,
    death_timestamps_ms: list[int] | None = None,
    level_up_events: list[tuple[int, int]] | None = None,
) -> dict:
    """Crea un timeline minimo con eventos de muerte y level-up."""
    events: list[dict] = []
    for ts in death_timestamps_ms or []:
        events.append(
            {
                "type": "CHAMPION_KILL",
                "timestamp": ts,
                "victimId": pid,
                "killerId": 99,
            }
        )
    for level, ts in level_up_events or []:
        events.append(
            {
                "type": "LEVEL_UP",
                "timestamp": ts,
                "participantId": pid,
                "level": level,
            }
        )
    return {
        "info": {
            "participants": [{"participantId": pid, "puuid": puuid}],
            "frames": [{"timestamp": 0, "events": events, "participantFrames": {}}],
        }
    }


# ============================================================
# Tests
# ============================================================


class TimelineEventsTest(unittest.TestCase):
    def test_player_id_for_puuid(self):
        tl = _mk_timeline(puuid="P1", pid=3)
        self.assertEqual(player_id_for_puuid(tl, "P1"), 3)
        self.assertIsNone(player_id_for_puuid(tl, "missing"))

    def test_player_deaths(self):
        tl = _mk_timeline(
            pid=1, death_timestamps_ms=[300_000, 1_200_000, 540_000]
        )
        deaths = player_deaths(tl, 1)
        self.assertEqual(deaths, [300_000, 540_000, 1_200_000])

        # otro pid no devuelve nada
        self.assertEqual(player_deaths(tl, 5), [])

    def test_player_level_ups(self):
        tl = _mk_timeline(
            pid=2,
            level_up_events=[(2, 60_000), (6, 480_000), (4, 240_000)],
        )
        ups = player_level_ups(tl, 2)
        # ordenados por timestamp
        self.assertEqual(ups, [(2, 60_000), (4, 240_000), (6, 480_000)])


class TierSTest(unittest.TestCase):
    def test_positioning_index_bottom(self):
        # 18000 / max(15000, 1) = 1.2
        m = _mk_match(
            me=_mk_participant(
                team_position="BOTTOM",
                dmg_to_champs=18000,
                dmg_taken=15000,
            )
        )
        out = compute_tier_s([m], "PUUID_X", "BOTTOM")
        self.assertEqual(len(out), 1)
        self.assertEqual(out[0]["key"], "derived.positioning_index")
        self.assertAlmostEqual(out[0]["mean"], 1.2, places=3)
        self.assertEqual(out[0]["n"], 1)

    def test_splitpush_index_top(self):
        # 1500 / max(15000, 1) = 0.1
        m = _mk_match(
            me=_mk_participant(
                team_position="TOP",
                dmg_to_champs=15000,
                dmg_to_turrets=1500,
            )
        )
        out = compute_tier_s([m], "PUUID_X", "TOP")
        self.assertEqual(out[0]["key"], "derived.splitpush_index")
        self.assertAlmostEqual(out[0]["mean"], 0.1, places=3)

    def test_counter_jungle_ratio(self):
        m = _mk_match(
            me=_mk_participant(
                team_position="JUNGLE",
                challenges={
                    "enemyJungleMonsterKills": 30,
                    "alliedJungleMonsterKills": 60,
                },
            )
        )
        out = compute_tier_s([m], "PUUID_X", "JUNGLE")
        self.assertAlmostEqual(out[0]["mean"], 0.5, places=3)

    def test_vision_dominance_ratio(self):
        me = _mk_participant(
            puuid="ME",
            pid=1,
            team_id=100,
            team_position="UTILITY",
            vision_score=80,
        )
        opp_sup = _mk_participant(
            puuid="OPP",
            pid=10,
            team_id=200,
            team_position="UTILITY",
            vision_score=40,
        )
        m = _mk_match(me=me, other_participants=[opp_sup])
        out = compute_tier_s([m], "ME", "UTILITY")
        self.assertEqual(out[0]["key"], "derived.vision_dominance_ratio")
        self.assertAlmostEqual(out[0]["mean"], 2.0, places=3)

    def test_role_without_tier_s_returns_empty(self):
        m = _mk_match()
        out = compute_tier_s([m], "PUUID_X", "MIDDLE")
        # MIDDLE no tiene Tier S registrado
        self.assertEqual(out, [])


class TierBTest(unittest.TestCase):
    def test_early_death_rate_25_bottom(self):
        # match con 2 muertes antes del 25' (1.5M ms) y 1 despues
        match = _mk_match(
            match_id="M1",
            me=_mk_participant(team_position="BOTTOM"),
        )
        timeline = _mk_timeline(
            puuid="PUUID_X",
            pid=1,
            death_timestamps_ms=[300_000, 1_200_000, 1_800_000],
        )
        out = compute_tier_b(
            [match], {"M1": timeline}, "PUUID_X", "BOTTOM"
        )
        self.assertEqual(len(out), 1)
        self.assertEqual(out[0]["key"], "derived.early_death_rate_25")
        self.assertEqual(out[0]["mean"], 2.0)

    def test_tempo_index_jungle_lvl6(self):
        match = _mk_match(
            match_id="MJ",
            me=_mk_participant(team_position="JUNGLE"),
        )
        # level 6 a los 480_000 ms (8 minutos)
        timeline = _mk_timeline(
            puuid="PUUID_X",
            pid=1,
            level_up_events=[(2, 60_000), (6, 480_000)],
        )
        out = compute_tier_b(
            [match], {"MJ": timeline}, "PUUID_X", "JUNGLE"
        )
        # esperamos al menos tempo_index_lvl6 + gank_to_death_ratio
        keys = [m["key"] for m in out]
        self.assertIn("derived.tempo_index_lvl6", keys)
        tempo = next(m for m in out if m["key"] == "derived.tempo_index_lvl6")
        self.assertEqual(tempo["mean"], 480.0)  # segundos

    def test_tier_b_no_timeline_returns_n0(self):
        match = _mk_match(me=_mk_participant(team_position="BOTTOM"))
        out = compute_tier_b([match], {}, "PUUID_X", "BOTTOM")
        # debe devolver la metrica con n=0, no crashear
        self.assertEqual(out[0]["n"], 0)
        self.assertIsNone(out[0]["mean"])


class TierATest(unittest.TestCase):
    def test_scaling_score_bottom(self):
        # 2 partidas largas (>=30min) con KDA alto, 2 cortas (<25min) con KDA bajo
        long_p = _mk_participant(
            kills=10, deaths=2, assists=10, win=True
        )  # KDA = 10
        short_p = _mk_participant(
            kills=3, deaths=5, assists=2, win=False
        )  # KDA = 1
        matches = [
            _mk_match(match_id=f"L{i}", duration_s=2000, me=long_p)
            for i in range(2)
        ] + [
            _mk_match(match_id=f"S{i}", duration_s=1200, me=short_p)
            for i in range(2)
        ]
        out = compute_tier_a(matches, "PUUID_X", "BOTTOM", duo_partners=None)
        self.assertIsNotNone(out)
        labels = [b["label"] for b in out["blocks"]]
        self.assertIn("Scaling Score", labels)
        scaling = next(b for b in out["blocks"] if b["label"] == "Scaling Score")
        # KDA largas / KDA cortas = 10 / 1 = 10
        self.assertAlmostEqual(scaling["metric_value"], 10.0, places=2)

    def test_roam_conversion_middle(self):
        # 2 partidas con >=2 roams y win, 2 partidas con 0 roams y loss
        roam_p = _mk_participant(
            team_position="MIDDLE",
            win=True,
            challenges={"killsOnOtherLanesEarlyJungleAsLaner": 3},
        )
        no_roam_p = _mk_participant(
            team_position="MIDDLE",
            win=False,
            challenges={"killsOnOtherLanesEarlyJungleAsLaner": 0},
        )
        matches = [
            _mk_match(match_id=f"R{i}", me=roam_p) for i in range(2)
        ] + [
            _mk_match(match_id=f"N{i}", me=no_roam_p) for i in range(2)
        ]
        out = compute_tier_a(matches, "PUUID_X", "MIDDLE", duo_partners=None)
        self.assertIsNotNone(out)
        roam = next(
            b for b in out["blocks"] if b["label"] == "Roam Conversion Rate"
        )
        # WR con roams = 100%, sin = 0%, delta = 100 pp
        self.assertEqual(roam["metric_value"], 100.0)

    def test_soul_rate_jungle(self):
        # 3 partidas largas, 2 con dragonTakedowns >= 4
        with_soul = _mk_participant(
            team_position="JUNGLE",
            challenges={"dragonTakedowns": 4},
        )
        no_soul = _mk_participant(
            team_position="JUNGLE",
            challenges={"dragonTakedowns": 2},
        )
        matches = [
            _mk_match(match_id="L1", duration_s=1800, me=with_soul),
            _mk_match(match_id="L2", duration_s=1800, me=with_soul),
            _mk_match(match_id="L3", duration_s=1800, me=no_soul),
        ]
        out = compute_tier_a(matches, "PUUID_X", "JUNGLE", duo_partners=None)
        self.assertIsNotNone(out)
        soul = next(b for b in out["blocks"] if b["label"] == "Soul Rate")
        # 2/3 = 0.666...
        self.assertAlmostEqual(soul["metric_value"], 2 / 3, places=3)

    def test_tier_a_empty_role_returns_none(self):
        m = _mk_match()
        out = compute_tier_a([m], "PUUID_X", "TOP", duo_partners=None)
        # TOP no tiene Tier A registrado
        self.assertIsNone(out)


class PromptsTest(unittest.TestCase):
    def test_all_roles_have_prompts(self):
        for role in ("TOP", "JUNGLE", "MIDDLE", "BOTTOM", "UTILITY"):
            self.assertIn(role, ROLE_PROMPTS)

    def test_render_role_prompt_top_full_keys(self):
        out = render_role_prompt(
            "TOP",
            role_label="Top",
            advanced_section_n=6,
            phases_section_n=5,
            cross_section_n="6.1",
            matchups_section_n=8,
            duo_section_n=11,
        )
        self.assertIsNotNone(out)
        assert out is not None  # narrowing for type checker
        self.assertIn("TOP", out)
        self.assertIn("Splitpush Index", out)
        self.assertIn("> ", out)  # blockquote
        # placeholders interpolados (no quedan llaves)
        self.assertNotIn("{role_label}", out)
        self.assertNotIn("{advanced_section_n}", out)

    def test_render_role_prompt_unknown_returns_none(self):
        out = render_role_prompt("INVALID", role_label="X")
        self.assertIsNone(out)


if __name__ == "__main__":
    unittest.main()
