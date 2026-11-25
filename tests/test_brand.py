from __future__ import annotations

from pathlib import Path

import pytest
from PIL import Image

BRAND = Path("custom_components/ha_anthropic_theme/brand")

EXPECTED_SIZES = {
    "icon.png": (256, 256),
    "icon@2x.png": (512, 512),
    "dark_icon.png": (256, 256),
    "dark_icon@2x.png": (512, 512),
    "logo.png": (1140, 128),
    "logo@2x.png": (2280, 256),
    "dark_logo.png": (1140, 128),
    "dark_logo@2x.png": (2280, 256),
}


def test_icon_svg_is_not_the_blueprint_placeholder() -> None:
    icon = (BRAND / "icon.svg").read_text()
    assert "TODO" not in icon
    assert "replace me" not in icon


@pytest.mark.parametrize(("name", "size"), EXPECTED_SIZES.items())
def test_brand_image_has_the_expected_size(name: str, size: tuple[int, int]) -> None:
    with Image.open(BRAND / name) as image:
        assert image.format == "PNG"
        assert image.size == size
        assert image.mode == "RGBA"


@pytest.mark.parametrize(
    "name", ["icon.png", "icon@2x.png", "dark_icon.png", "dark_icon@2x.png"]
)
def test_icons_are_square(name: str) -> None:
    with Image.open(BRAND / name) as image:
        width, height = image.size
    assert width == height


@pytest.mark.parametrize(
    "name", ["logo.png", "logo@2x.png", "dark_logo.png", "dark_logo@2x.png"]
)
def test_logos_are_landscape(name: str) -> None:
    with Image.open(BRAND / name) as image:
        width, height = image.size
    assert width > height


@pytest.mark.parametrize("name", EXPECTED_SIZES)
def test_brand_image_has_a_transparent_background(name: str) -> None:
    with Image.open(BRAND / name) as image:
        corner_alpha = image.getpixel((0, 0))
    assert isinstance(corner_alpha, tuple)
    assert corner_alpha[3] == 0


def test_brand_holds_only_the_assets() -> None:
    shipped = {path.name for path in BRAND.iterdir() if not path.name.startswith(".")}
    assert shipped == {"icon.svg", "logo.svg", *EXPECTED_SIZES}


def mean_opaque_luminance(name: str) -> float:
    with Image.open(BRAND / name) as image:
        grayscale = image.convert("LA")
        opaque = [
            luminance
            for luminance, alpha in grayscale.get_flattened_data()
            if alpha == 255
        ]
    assert opaque
    return sum(opaque) / len(opaque)


@pytest.mark.parametrize("name", EXPECTED_SIZES)
def test_dark_variants_are_light_and_the_others_dark(name: str) -> None:
    luminance = mean_opaque_luminance(name)
    if name.startswith("dark_"):
        assert luminance > 200
    else:
        assert luminance < 55
