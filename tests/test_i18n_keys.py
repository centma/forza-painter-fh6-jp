from __future__ import annotations

import pytest

from i18n import TEXT

# Keys shown on screen before any user action
STARTUP_KEYS = ("text_layer_estimate_idle",)


@pytest.mark.parametrize("lang", ["en", "ja"])
@pytest.mark.parametrize("key", STARTUP_KEYS)
def test_startup_key_defined(lang, key):
    assert key in TEXT[lang]
