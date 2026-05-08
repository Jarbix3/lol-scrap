"""Smoke tests del pipeline de reporte completo.

Inyecta datos sinteticos en build_report y valida que:
1. El reporte se genera sin errores.
2. La sub-seccion 'Analisis cruzado' aparece cuando hay tier_a.
3. El prompt LLM rol-especifico se inserta cuando hay --role.

Standalone con `unittest`: corre con `python -m unittest tests.test_report_smoke`.
"""
from __future__ import annotations

import unittest

from lol_scrap.fetcher import PlayerData
from lol_scrap.report import build_report


def _mk_player() -> PlayerData:
    return PlayerData(
        riot_id="Manuchito#LAS",
        puuid="PUUID_X",
        summoner={},
        league_entries=[],
        matches=[],
        timelines={},
    )


def _mk_overall() -> dict:
    return {
        "games": 50,
        "wins": 28,
        "losses": 22,
        "winrate": 0.56,
        "kda": 2.3,
        "kills_avg": 5.2,
        "deaths_avg": 4.8,
        "assists_avg": 6.1,
        "cs_per_min": 7.2,
        "dmg_per_min": 580.0,
        "vision_avg": 22.5,
        "minutes_played": 1500.0,
    }


def _mk_minimal_inputs() -> dict:
    return {
        "player": _mk_player(),
        "overall": _mk_overall(),
        "champion_pool": [],
        "roles": [],
        "playstyle": {"by_role": []},
        "duo_partners": [],
        "champion_synergies": [],
        "matchups": {"best": [], "worst": []},
        "weaknesses": {"metric_deficits": [], "loss_patterns": {}},
        "queues": [420, 440],
        "count": 100,
    }


class ReportSmokeTest(unittest.TestCase):
    def test_report_with_role_filter_and_tier_a(self):
        role_advanced = [
            {
                "label": "Positioning Index",
                "key": "derived.positioning_index",
                "display": "decimal",
                "hint": "Dano hecho / Dano recibido",
                "mean": 1.05,
                "total": 21.0,
                "min": 0.5,
                "max": 1.8,
                "n": 20,
            },
            {
                "label": "Muertes antes del 25' (avg)",
                "key": "derived.early_death_rate_25",
                "display": "decimal",
                "hint": None,
                "mean": 2.5,
                "total": 50.0,
                "min": 0,
                "max": 6,
                "n": 20,
            },
        ]
        tier_a = {
            "role": "BOTTOM",
            "blocks": [
                {
                    "label": "Scaling Score",
                    "summary": "KDA largas: 3.1 (n=12) | KDA cortas: 1.8 (n=8)",
                    "rows": [
                        {
                            "label": "Partidas largas (>=30')",
                            "wr": 0.66,
                            "kda": 3.1,
                            "n": 12,
                        },
                        {
                            "label": "Partidas cortas (<25')",
                            "wr": 0.50,
                            "kda": 1.8,
                            "n": 8,
                        },
                    ],
                    "interpretation": "Te beneficia el late game.",
                    "metric_value": 1.72,
                    "metric_label": "KDA ratio (largas / cortas)",
                },
            ],
        }
        game_phases = {
            "early": {"label": "Early game (0-15')", "score": 6.5, "metrics": []},
            "mid": {"label": "Mid game (15-25')", "score": 5.0, "metrics": []},
            "late": {"label": "Late game (25'+)", "score": 7.2, "metrics": []},
            "total_games": 50,
            "long_games_n": 20,
        }
        md = build_report(
            **_mk_minimal_inputs(),
            role_filter="BOTTOM",
            global_overall=_mk_overall(),
            global_role_stats=[],
            role_advanced=role_advanced,
            tier_a=tier_a,
            game_phases=game_phases,
            rank_key="diamond",
            rank_source="explicit",
            rank_source_label="--rank diamond",
        )
        # Reporte se genero sin errores.
        self.assertGreater(len(md), 1000)
        # Sub-seccion Analisis cruzado aparece.
        self.assertIn("Análisis cruzado", md)
        self.assertIn("Scaling Score", md)
        self.assertIn("KDA ratio (largas / cortas)", md)
        # Prompt rol-especifico (BOTTOM/ADC) aparece.
        self.assertIn("BOTTOM/ADC", md)
        self.assertIn("Positioning Index", md)
        # No deberia aparecer el prompt generico ("¿Juega bien su línea?").
        self.assertNotIn("¿Juega bien su línea?", md)

    def test_report_without_role_keeps_generic_prompt(self):
        md = build_report(
            **_mk_minimal_inputs(),
            role_filter=None,
            role_advanced=None,
            tier_a=None,
            game_phases=None,
            rank_key="diamond",
            rank_source="explicit",
            rank_source_label="--rank diamond",
        )
        self.assertGreater(len(md), 500)
        # Prompt generico aparece.
        self.assertIn("¿Juega bien su línea?", md)
        # Prompt rol-especifico NO aparece.
        self.assertNotIn("dimensiones críticas", md)

    def test_report_with_role_but_no_tier_a(self):
        # Edge case: --role activo pero compute_tier_a devolvio None.
        # El prompt rol-especifico debe seguir saliendo (sin referenciar
        # cross_section_n.1).
        role_advanced = [
            {
                "label": "Positioning Index",
                "key": "derived.positioning_index",
                "display": "decimal",
                "hint": None,
                "mean": 1.05,
                "total": 21.0,
                "min": 0.5,
                "max": 1.8,
                "n": 20,
            },
        ]
        md = build_report(
            **_mk_minimal_inputs(),
            role_filter="BOTTOM",
            global_overall=_mk_overall(),
            global_role_stats=[],
            role_advanced=role_advanced,
            tier_a=None,
            game_phases={
                "early": {
                    "label": "Early game (0-15')", "score": 5.0, "metrics": []
                },
                "mid": {
                    "label": "Mid game (15-25')", "score": 5.0, "metrics": []
                },
                "late": {
                    "label": "Late game (25'+)", "score": 5.0, "metrics": []
                },
                "total_games": 20,
                "long_games_n": 10,
            },
            rank_key="diamond",
            rank_source="explicit",
            rank_source_label="--rank diamond",
        )
        # No deberia haber sub-seccion Analisis cruzado renderizada
        # (el header "### X.1 Análisis cruzado" no aparece).
        self.assertNotIn("### 6.1 Análisis cruzado", md)
        self.assertNotIn(
            "_Métricas que cruzan dos sub-grupos de partidas",
            md,
        )
        # Pero el prompt rol-especifico SI deberia salir.
        self.assertIn("BOTTOM/ADC", md)


if __name__ == "__main__":
    unittest.main()
