"""Tests para build_master_prompt en lol_scrap.prompts.

Valida que:
1. La seccion final de Ranking + Plan de accion se inserta cuando hay
   roles_with_md (n>=1).
2. El sections_outline del header lista la seccion de ranking con el
   numero correcto.
3. El bloque ## Cierre menciona la seccion de ranking.
4. Las tablas (Ranking de roles y Top 5 acciones) aparecen en el output
   con sus columnas obligatorias.
5. Edge case: sin roles_with_md, el bloque de ranking NO se renderiza.

Standalone con unittest: corre con `python -m unittest tests.test_master_prompt`.
"""
from __future__ import annotations

import unittest

from lol_scrap.prompts import build_master_prompt


def _mk_prompt(
    *,
    has_global: bool = True,
    roles: list[tuple[str, str, int]] | None = None,
) -> str:
    if roles is None:
        roles = [
            ("MIDDLE", "Mid", 268),
            ("TOP", "Top", 245),
            ("JUNGLE", "Jungla", 126),
            ("BOTTOM", "ADC", 38),
            ("UTILITY", "Support", 28),
        ]
    return build_master_prompt(
        player_riot_id="Manuchito#LAS",
        player_dir_relpath="reports/Manuchito-LAS",
        roles_with_md=roles,
        has_global=has_global,
        generated_at="2026-05-08 20:40 UTC",
    )


class TestRankingSectionRendered(unittest.TestCase):
    def test_ranking_section_appears_with_overview_and_5_roles(self) -> None:
        out = _mk_prompt(has_global=True)
        # 1 overview + 5 roles + 1 ranking = section 7
        self.assertIn(
            "## Sección 7 — Ranking final + Plan de acción (Coach Jefe)", out
        )
        # Sub-secciones 7.1 (ranking de roles), 7.2 (top 5 acciones), 7.3 (cierre)
        self.assertIn("**7.1 Ranking de roles", out)
        self.assertIn("**7.2 Top 5 acciones accionables cross-role", out)
        self.assertIn("**7.3 Cierre del coach jefe**", out)

    def test_ranking_section_index_without_global(self) -> None:
        # Sin global: 5 roles + ranking => seccion 6
        out = _mk_prompt(has_global=False)
        self.assertIn(
            "## Sección 6 — Ranking final + Plan de acción (Coach Jefe)", out
        )
        self.assertIn("**6.1 Ranking de roles", out)
        self.assertIn("**6.2 Top 5 acciones accionables cross-role", out)
        self.assertIn("**6.3 Cierre del coach jefe**", out)

    def test_ranking_section_index_with_partial_roles(self) -> None:
        # Solo 2 roles + global => ranking en seccion 4
        out = _mk_prompt(
            has_global=True,
            roles=[("TOP", "Top", 162), ("MIDDLE", "Mid", 80)],
        )
        self.assertIn(
            "## Sección 4 — Ranking final + Plan de acción (Coach Jefe)", out
        )
        self.assertIn("**4.1 Ranking de roles", out)


class TestSectionsOutline(unittest.TestCase):
    def test_outline_lists_ranking_section(self) -> None:
        out = _mk_prompt(has_global=True)
        # El outline en el header debe listar todas las secciones por numero
        self.assertIn(
            "7. **Sección 7 — Ranking final + Plan de acción (Coach Jefe)**",
            out,
        )

    def test_outline_lists_correct_number_of_sections(self) -> None:
        out = _mk_prompt(has_global=True)
        # Cierre debe mencionar n_sections=7 (1 overview + 5 roles + 1 ranking)
        self.assertIn("las 7 secciones", out)
        self.assertIn("la sección 7", out)


class TestTableFormat(unittest.TestCase):
    def test_ranking_table_has_required_columns(self) -> None:
        out = _mk_prompt(has_global=True)
        # Header de la tabla 7.1
        self.assertIn(
            "| # | Rol | Games | WR | E / M / L | Justificación", out
        )
        self.assertIn("Datos clave (2-3 stats con valor) |", out)

    def test_top5_actions_table_has_required_columns(self) -> None:
        out = _mk_prompt(has_global=True)
        self.assertIn(
            "| # | Acción | Por qué (evidencia con número) | Roles afectados | Esfuerzo |",
            out,
        )

    def test_ranking_table_includes_example_row(self) -> None:
        out = _mk_prompt(has_global=True)
        # El ejemplo concreto guia al LLM
        self.assertIn("| 1 | Top | 245 | 51.8%", out)
        self.assertIn("Mordekaiser 64% WR [TOP.md sec. 5, 7]", out)


class TestRankingEdgeCases(unittest.TestCase):
    def test_no_roles_no_ranking_block(self) -> None:
        out = _mk_prompt(has_global=True, roles=[])
        # Si no hay roles, no se renderiza la seccion de ranking
        self.assertNotIn("Ranking final + Plan de acción", out)

    def test_rules_section_present(self) -> None:
        out = _mk_prompt(has_global=True)
        # Reglas estrictas que deben aparecer en la seccion
        self.assertIn("Cero invenciones", out)
        self.assertIn("Coherencia interna", out)
        self.assertIn("Sin emojis", out)


class TestPromptStability(unittest.TestCase):
    """Si tocamos accidentalmente la longitud, este test salta."""

    def test_prompt_length_within_expected_range(self) -> None:
        out = _mk_prompt(has_global=True)
        # Despues de agregar la seccion de ranking, deberia rondar 20k-32k chars
        self.assertGreater(len(out), 20000)
        self.assertLess(len(out), 32000)


if __name__ == "__main__":
    unittest.main()
