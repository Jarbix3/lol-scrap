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
        # El ejemplo concreto guia al LLM (sin refs tipo [ARCHIVO.md sec. X])
        self.assertIn("| 1 | Top | 245 | 51.8%", out)
        self.assertIn("Mordekaiser 64% WR en 59 games", out)
        # Verifica que el ejemplo NO trae el formato prohibido
        self.assertNotIn("[TOP.md sec. 5, 7]", out)


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
        # Despues de las nuevas reglas R7-R10 + tablas obligatorias en role
        # prompts, el prompt completo ronda ~38k-50k chars con 5 roles + global.
        self.assertGreater(len(out), 30000)
        self.assertLess(len(out), 55000)


class TestNewRules(unittest.TestCase):
    """Valida que las reglas globales R1-R10 estan presentes y tienen el
    contenido esperado (R7-R10 son nuevas)."""

    def test_R1_no_inventes_datos(self) -> None:
        out = _mk_prompt(has_global=True)
        self.assertIn("**R1. Regla de oro**", out)
        self.assertIn("NO INVENTES DATOS", out)

    def test_R2_no_file_refs(self) -> None:
        out = _mk_prompt(has_global=True)
        self.assertIn("**R2. Cita evidencia con números, NO con archivos**", out)
        # Debe explicitar el formato prohibido y el formato correcto.
        # PROHIBIDO/escribir queda separado por newline, busco cada parte:
        self.assertIn("PROHIBIDO", out)
        self.assertIn("KDA 2.51 en tu data de Top", out)
        # Y debe nombrar los formatos prohibidos (sin caer en falso positivo)
        self.assertIn("[GLOBAL.md sec. 4]", out)  # como ejemplo de "Mal"
        self.assertIn("[TOP.md sec. 6]", out)  # como ejemplo de "Mal"

    def test_R4_tablas_sobre_prosa(self) -> None:
        out = _mk_prompt(has_global=True)
        self.assertIn("**R4. Tablas sobre prosa cuando hay ≥3 elementos comparables**", out)
        self.assertIn("USÁ TABLA MARKDOWN", out)

    def test_R5_drill_down_pattern(self) -> None:
        out = _mk_prompt(has_global=True)
        self.assertIn("**R5. Patrón \"tabla resumen → drill-down debajo\"**", out)
        self.assertIn("Tabla compacta primero", out)
        self.assertIn("Explicación detallada debajo", out)

    def test_R8_counter_matchups_obligatorios(self) -> None:
        out = _mk_prompt(has_global=True)
        self.assertIn("**R8. Counter matchups obligatorios por rol**", out)
        self.assertIn("Top 3-5 peores matchups", out)
        self.assertIn("Top 3 mejores matchups", out)

    def test_R10_sin_emojis(self) -> None:
        out = _mk_prompt(has_global=True)
        self.assertIn("**R10. Sin emojis", out)


class TestRolePromptsHaveMatchupTables(unittest.TestCase):
    """Cada role prompt debe pedir explicitamente E1 (peores) y E2
    (mejores) con tabla, y F (champ pool) con tabla."""

    def test_top_role_has_E1_E2_F_tables(self) -> None:
        out = _mk_prompt(
            has_global=True, roles=[("TOP", "Top", 245)]
        )
        self.assertIn("**E1) Top 3-5 PEORES matchups en lane Top**", out)
        self.assertIn("**E2) Top 3 MEJORES matchups en lane Top**", out)
        self.assertIn("**F) Champ pool propio en Top**", out)
        self.assertIn("TABLA OBLIGATORIA", out)

    def test_jungle_role_has_E1_E2_F_tables(self) -> None:
        out = _mk_prompt(
            has_global=True, roles=[("JUNGLE", "Jungla", 126)]
        )
        self.assertIn("**E1) Top 3-5 PEORES matchups vs jungla enemigo**", out)
        self.assertIn("**E2) Top 3 MEJORES matchups vs jungla enemigo**", out)
        self.assertIn("**F) Champ pool propio (junglas)**", out)

    def test_middle_role_has_E1_E2_F_tables(self) -> None:
        out = _mk_prompt(
            has_global=True, roles=[("MIDDLE", "Mid", 268)]
        )
        self.assertIn("**E1) Top 3-5 PEORES matchups en lane Mid**", out)
        self.assertIn("**E2) Top 3 MEJORES matchups en lane Mid**", out)
        self.assertIn("**F) Champ pool propio (mids)**", out)

    def test_bottom_role_has_E1_E2_F_G_tables(self) -> None:
        out = _mk_prompt(
            has_global=True, roles=[("BOTTOM", "ADC", 38)]
        )
        self.assertIn("**E1) Top 3-5 PEORES matchups vs ADC enemigo**", out)
        self.assertIn("**E2) Top 3 MEJORES matchups vs ADC enemigo**", out)
        self.assertIn("**F) Champ pool propio (ADCs)**", out)
        self.assertIn("**G) Sinergias con sup duo**", out)

    def test_utility_role_has_E1_E2_F_G_tables(self) -> None:
        out = _mk_prompt(
            has_global=True, roles=[("UTILITY", "Support", 28)]
        )
        self.assertIn("**E1) Top 3-5 PEORES matchups vs sup enemigo**", out)
        self.assertIn("**E2) Top 3 MEJORES matchups vs sup enemigo**", out)
        self.assertIn("**F) Champ pool propio (sups) por arquetipo**", out)
        self.assertIn("**G) Sinergias con ADC duo**", out)


class TestOverviewHasTables(unittest.TestCase):
    """El _OVERVIEW_PROMPT debe pedir tablas obligatorias en 1.1, 1.2,
    1.3 y 1.4."""

    def test_overview_demands_tables(self) -> None:
        out = _mk_prompt(has_global=True)
        self.assertIn("**1.1 Identificación del rol natural** — TABLA OBLIGATORIA", out)
        self.assertIn("**1.2 Inversión de tiempo vs WR** — TABLA + 1 párrafo", out)
        self.assertIn("**1.3 Sinergias humanas globales** — TABLA + 1 párrafo", out)
        self.assertIn("**1.4 Patrones cruzados", out)

    def test_overview_table_columns_have_lectura(self) -> None:
        out = _mk_prompt(has_global=True)
        # La regla obliga a columna "Lectura" en tablas comparativas
        self.assertIn("| Aliado | Games | WR juntos | Δpp vs tu WR overall | Lectura |", out)
        self.assertIn("| Rol | Games | WR | KDA | CS/m | DPM | Vision/min | Lectura |", out)


class TestNoFileRefsInExampleRows(unittest.TestCase):
    """Los ejemplos en las tablas y reglas no deben usar el formato
    prohibido [ARCHIVO.md sec. X] para no enviar señal mixta al LLM."""

    def test_no_md_refs_in_ranking_example_row(self) -> None:
        """La FILA EJEMPLO de la tabla 7.1 no debe traer [ARCHIVO.md sec. X].

        OJO: la regla de llenado de 7.1 menciona el formato prohibido
        explicitamente (como negacion); por eso buscamos solo la linea
        de la fila 1 con datos reales.
        """
        out = _mk_prompt(has_global=True)
        # La fila ejemplo empieza con "| 1 | Top | 245 |" y termina al \n
        row_start = out.find("| 1 | Top | 245 |")
        self.assertGreater(row_start, 0, "Fila ejemplo no encontrada")
        row_end = out.find("\n", row_start)
        row = out[row_start:row_end]
        self.assertNotIn("[TOP.md", row)
        self.assertNotIn("[GLOBAL.md", row)
        self.assertNotIn("sec.", row)

    def test_no_md_refs_in_top5_actions_example_row(self) -> None:
        """La FILA EJEMPLO de la tabla 7.2 tampoco debe traer
        [ARCHIVO.md sec. X]."""
        out = _mk_prompt(has_global=True)
        row_start = out.find("| 1 | Subir CS@10")
        self.assertGreater(row_start, 0, "Fila ejemplo no encontrada")
        row_end = out.find("\n", row_start)
        row = out[row_start:row_end]
        self.assertNotIn("[GLOBAL.md", row)
        self.assertNotIn("[TOP.md", row)
        self.assertNotIn("sec.", row)


if __name__ == "__main__":
    unittest.main()
