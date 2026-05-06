"""Cache local en disco para matches y timelines (datos inmutables)."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class MatchCache:
    """Persiste matches y timelines como JSON, indexados por matchId."""

    def __init__(self, root: Path | str = "cache") -> None:
        self.root = Path(root)
        self.matches_dir = self.root / "matches"
        self.timelines_dir = self.root / "timelines"
        self.matches_dir.mkdir(parents=True, exist_ok=True)
        self.timelines_dir.mkdir(parents=True, exist_ok=True)

    def _match_path(self, match_id: str) -> Path:
        return self.matches_dir / f"{match_id}.json"

    def _timeline_path(self, match_id: str) -> Path:
        return self.timelines_dir / f"{match_id}.json"

    def get_match(self, match_id: str) -> dict[str, Any] | None:
        path = self._match_path(match_id)
        if not path.exists():
            return None
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return None

    def set_match(self, match_id: str, data: dict[str, Any]) -> None:
        self._match_path(match_id).write_text(
            json.dumps(data, ensure_ascii=False), encoding="utf-8"
        )

    def get_timeline(self, match_id: str) -> dict[str, Any] | None:
        path = self._timeline_path(match_id)
        if not path.exists():
            return None
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return None

    def set_timeline(self, match_id: str, data: dict[str, Any]) -> None:
        self._timeline_path(match_id).write_text(
            json.dumps(data, ensure_ascii=False), encoding="utf-8"
        )

    def has_match(self, match_id: str) -> bool:
        return self._match_path(match_id).exists()

    def has_timeline(self, match_id: str) -> bool:
        return self._timeline_path(match_id).exists()
