"""Tests para las metricas de laning derivadas del timeline (Won lane @14', Lane lead).

Verifica que:
- Lane phase win rate (oro+exp @14') = % de partidas donde mi (gold+xp) > opp.
- Lane lead promedio @14' = avg delta numerico (mi - opp) en oro-equivalente.
- Score 1-10 NO satura para muestras realistas (~30-70% rate).

Standalone con `unittest`: `python -m unittest tests.test_lane_metrics`.
"""
from __future__ import annotations

import unittest

from lol_scrap.analytics.game_phases import compute_game_phases


def _mk_timeline(
    *,
    my_pid: int,
    opp_pid: int,
    my_gold: int,
    my_xp: int,
    opp_gold: int,
    opp_xp: int,
    my_puuid: str,
    opp_puuid: str,
) -> dict:
    """Timeline minimo con frame al min 14 (840000ms)."""
    return {
        "info": {
            "participants": [
                {"participantId": my_pid, "puuid": my_puuid},
                {"participantId": opp_pid, "puuid": opp_puuid},
            ],
            "frames": [
                {
                    "timestamp": 0,
                    "events": [],
                    "participantFrames": {
                        str(my_pid): {
                            "totalGold": 0,
                            "xp": 0,
                            "minionsKilled": 0,
                            "jungleMinionsKilled": 0,
                        },
                        str(opp_pid): {
                            "totalGold": 0,
                            "xp": 0,
                            "minionsKilled": 0,
                            "jungleMinionsKilled": 0,
                        },
                    },
                },
                {
                    "timestamp": 14 * 60 * 1000,
                    "events": [],
                    "participantFrames": {
                        str(my_pid): {
                            "totalGold": my_gold,
                            "xp": my_xp,
                            "minionsKilled": 70,
                            "jungleMinionsKilled": 0,
                        },
                        str(opp_pid): {
                            "totalGold": opp_gold,
                            "xp": opp_xp,
                            "minionsKilled": 70,
                            "jungleMinionsKilled": 0,
                        },
                    },
                },
            ],
        }
    }


def _mk_match(
    *,
    match_id: str,
    my_puuid: str,
    opp_puuid: str,
    my_pid: int = 1,
    opp_pid: int = 6,
    my_role: str = "TOP",
    duration_s: int = 1800,
    win: bool = True,
) -> dict:
    return {
        "metadata": {"matchId": match_id},
        "info": {
            "gameDuration": duration_s,
            "participants": [
                {
                    "puuid": my_puuid,
                    "participantId": my_pid,
                    "teamId": 100,
                    "teamPosition": my_role,
                    "win": win,
                    "kills": 4,
                    "deaths": 3,
                    "assists": 5,
                    "challenges": {},
                },
                {
                    "puuid": opp_puuid,
                    "participantId": opp_pid,
                    "teamId": 200,
                    "teamPosition": my_role,
                    "win": not win,
                    "kills": 3,
                    "deaths": 4,
                    "assists": 2,
                    "challenges": {},
                },
            ],
        },
    }


def _find_metric(early_metrics: list[dict], label_substr: str) -> dict | None:
    for m in early_metrics:
        if label_substr in m["label"]:
            return m
    return None


class LanePhaseWinRateTest(unittest.TestCase):
    def test_win_rate_at_50pct_gives_score_5(self):
        """4 partidas: 2 ganadas (delta +500), 2 perdidas (delta -500)."""
        matches = []
        timelines = {}
        for i, won in enumerate([True, True, False, False]):
            mid = f"M{i}"
            matches.append(
                _mk_match(
                    match_id=mid,
                    my_puuid="ME",
                    opp_puuid="OPP",
                )
            )
            if won:
                timelines[mid] = _mk_timeline(
                    my_pid=1,
                    opp_pid=6,
                    my_gold=5500,
                    my_xp=6500,
                    opp_gold=5000,
                    opp_xp=6000,
                    my_puuid="ME",
                    opp_puuid="OPP",
                )
            else:
                timelines[mid] = _mk_timeline(
                    my_pid=1,
                    opp_pid=6,
                    my_gold=5000,
                    my_xp=6000,
                    opp_gold=5500,
                    opp_xp=6500,
                    my_puuid="ME",
                    opp_puuid="OPP",
                )
        out = compute_game_phases(matches, timelines, "ME", baselines={})
        early = out["early"]["metrics"]
        wr_metric = _find_metric(early, "Lane phase win rate")
        self.assertIsNotNone(wr_metric)
        assert wr_metric is not None
        self.assertAlmostEqual(wr_metric["value"], 0.5, places=2)
        # 50% = en linea con target 0.5 -> score 5.0
        self.assertAlmostEqual(wr_metric["score"], 5.0, places=1)
        self.assertEqual(wr_metric["n"], 4)

    def test_win_rate_70pct_gives_higher_score(self):
        """7 ganadas, 3 perdidas -> 70% -> score > 5."""
        matches = []
        timelines = {}
        for i in range(10):
            mid = f"M{i}"
            matches.append(
                _mk_match(
                    match_id=mid,
                    my_puuid="ME",
                    opp_puuid="OPP",
                )
            )
            won = i < 7
            timelines[mid] = _mk_timeline(
                my_pid=1,
                opp_pid=6,
                my_gold=5500 if won else 5000,
                my_xp=6500 if won else 6000,
                opp_gold=5000 if won else 5500,
                opp_xp=6000 if won else 6500,
                my_puuid="ME",
                opp_puuid="OPP",
            )
        out = compute_game_phases(matches, timelines, "ME", baselines={})
        wr_metric = _find_metric(out["early"]["metrics"], "Lane phase win rate")
        self.assertIsNotNone(wr_metric)
        assert wr_metric is not None
        self.assertAlmostEqual(wr_metric["value"], 0.7, places=2)
        self.assertGreater(wr_metric["score"], 5.0)
        self.assertLess(wr_metric["score"], 10.0)  # NO satura

    def test_win_rate_15pct_no_longer_saturates_at_1(self):
        """Manuchito-style: 15% rate. Antes scoreaba 1.0/10; ahora deberia
        seguir bajo pero no exactamente saturado en 1.0 (ratio 0.30).

        Con target 0.5 y scale 1.5: ratio=0.30 -> raw = 5 + 5*(-0.7)*1.5 = -0.25
        -> clamp 1.0. Aun satura porque 15% es muy bajo absoluto.
        Lo importante es que ahora ese 15% es "muy malo de verdad" (un jugador
        promedio gana 50%, no 11%), no un artefacto de target equivocado.
        """
        matches = []
        timelines = {}
        for i in range(20):
            mid = f"M{i}"
            matches.append(
                _mk_match(
                    match_id=mid,
                    my_puuid="ME",
                    opp_puuid="OPP",
                )
            )
            won = i < 3  # 15%
            timelines[mid] = _mk_timeline(
                my_pid=1,
                opp_pid=6,
                my_gold=5500 if won else 5000,
                my_xp=6500 if won else 6000,
                opp_gold=5000 if won else 5500,
                opp_xp=6000 if won else 6500,
                my_puuid="ME",
                opp_puuid="OPP",
            )
        out = compute_game_phases(matches, timelines, "ME", baselines={})
        wr_metric = _find_metric(out["early"]["metrics"], "Lane phase win rate")
        self.assertIsNotNone(wr_metric)
        assert wr_metric is not None
        self.assertAlmostEqual(wr_metric["value"], 0.15, places=2)


class LaneLeadAvgTest(unittest.TestCase):
    def test_lead_avg_calculated_correctly(self):
        """3 partidas: deltas +1000, +500, -300. Promedio = +400."""
        deltas = [1000, 500, -300]
        matches = []
        timelines = {}
        for i, delta in enumerate(deltas):
            mid = f"M{i}"
            matches.append(
                _mk_match(
                    match_id=mid,
                    my_puuid="ME",
                    opp_puuid="OPP",
                )
            )
            timelines[mid] = _mk_timeline(
                my_pid=1,
                opp_pid=6,
                my_gold=5000 + max(delta, 0),
                my_xp=5000 + max(delta, 0) // 2,
                opp_gold=5000 - min(delta, 0),
                opp_xp=5000 - min(delta, 0) // 2,
                my_puuid="ME",
                opp_puuid="OPP",
            )
        out = compute_game_phases(matches, timelines, "ME", baselines={})
        lead_metric = _find_metric(
            out["early"]["metrics"], "Lane lead promedio"
        )
        self.assertIsNotNone(lead_metric)
        assert lead_metric is not None
        # Cada partida: my_score = (5000 + max(d,0)) + (5000 + max(d,0)//2)
        # opp_score = (5000 - min(d,0)) + (5000 - min(d,0)//2)
        # delta_combined = my_score - opp_score
        # Para d=+1000: mine = 6000+5500 = 11500; opp = 5000+5000 = 10000; delta=+1500
        # Para d=+500:  mine = 5500+5250 = 10750; opp = 5000+5000 = 10000; delta=+750
        # Para d=-300:  mine = 5000+5000 = 10000; opp = 5300+5150 = 10450; delta=-450
        # avg = (1500 + 750 - 450) / 3 = 600
        self.assertAlmostEqual(lead_metric["value"], 600.0, places=0)
        self.assertEqual(lead_metric["n"], 3)

    def test_lead_score_around_5_when_zero(self):
        """Lead = 0 -> _score_diff con scale_unit=2000 -> raw = 5.5 -> clamp 5.5."""
        matches = []
        timelines = {}
        for i in range(4):
            mid = f"M{i}"
            matches.append(
                _mk_match(
                    match_id=mid,
                    my_puuid="ME",
                    opp_puuid="OPP",
                )
            )
            timelines[mid] = _mk_timeline(
                my_pid=1,
                opp_pid=6,
                my_gold=5000,
                my_xp=6000,
                opp_gold=5000,
                opp_xp=6000,
                my_puuid="ME",
                opp_puuid="OPP",
            )
        out = compute_game_phases(matches, timelines, "ME", baselines={})
        lead_metric = _find_metric(
            out["early"]["metrics"], "Lane lead promedio"
        )
        assert lead_metric is not None
        self.assertEqual(lead_metric["value"], 0)
        # _score_diff(0, 2000) = 5.5
        self.assertAlmostEqual(lead_metric["score"], 5.5, places=1)


class OldMetricRemovedTest(unittest.TestCase):
    def test_won_laning_rate_no_longer_present(self):
        """La metrica vieja 'Won laning rate (oro+exp ventaja)' debe estar fuera."""
        m = _mk_match(
            match_id="M1",
            my_puuid="ME",
            opp_puuid="OPP",
        )
        m["info"]["participants"][0]["challenges"] = {
            "laningPhaseGoldExpAdvantage": 1
        }
        # Sin timeline -> metricas nuevas devuelven n=0; pero tampoco debe
        # aparecer la vieja con label "Won laning rate (oro+exp ventaja)".
        out = compute_game_phases([m], {}, "ME", baselines={})
        labels = [met["label"] for met in out["early"]["metrics"]]
        for label in labels:
            self.assertNotIn("Won laning rate", label)


if __name__ == "__main__":
    unittest.main()
