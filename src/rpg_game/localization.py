from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict


@dataclass(frozen=True)
class Localization:
    language: str
    strings: Dict[str, str]

    def get(self, key: str, default: str | None = None) -> str:
        if key in self.strings:
            return self.strings[key]
        if default is not None:
            return default
        return key


def load_localization(language: str, base_path: Path | None = None) -> Localization:
    root = base_path or Path(__file__).resolve().parent
    locale_path = root / "locales" / f"{language}.json"
    data = json.loads(locale_path.read_text(encoding="utf-8"))
    return Localization(language=language, strings=data)
