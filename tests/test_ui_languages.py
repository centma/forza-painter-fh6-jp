from __future__ import annotations

from app import LANGUAGES
from ui_preferences import SUPPORTED_UI_LANGUAGES


# Both lists define the UI languages; a language missing from one is
# either unselectable or not remembered across restarts.
def test_language_lists_match():
    assert set(LANGUAGES.values()) == set(SUPPORTED_UI_LANGUAGES)
