from app.talana_kombat_jrpg.constants import (
    ARNOLD_REMUYUKEN_COMBINATION,
    ARNOLD_REMUYUKEN_ENERGY,
    ARNOLD_TALADOKEN_COMBINATION,
    ARNOLD_TALADOKEN_ENERGY,
    REMUYUKEN_NAME,
    TALADOKEN_NAME,
    TONY_REMUYUKEN_COMBINATION,
    TONY_REMUYUKEN_ENERGY,
    TONY_TALADOKEN_COMBINATION,
    TONY_TALADOKEN_ENERGY,
)
from app.talana_kombat_jrpg.utils import GenerateMoves


class TestGenerateMoves:
    def test_specials_tony(self, tony):
        special_taladoken = GenerateMoves.special(
            moves_message=TONY_TALADOKEN_COMBINATION,
            name_fighter=tony.name,
            special_name=TALADOKEN_NAME,
            combination=TONY_TALADOKEN_COMBINATION,
            energy=TONY_TALADOKEN_ENERGY,
        )
        special_remuyuken = GenerateMoves.special(
            moves_message=TONY_REMUYUKEN_COMBINATION,
            name_fighter=tony.name,
            special_name=REMUYUKEN_NAME,
            combination=TONY_REMUYUKEN_COMBINATION,
            energy=TONY_REMUYUKEN_ENERGY,
        )
        assert special_taladoken["message"] == f"{tony.name} use {TALADOKEN_NAME}"
        assert special_remuyuken["message"] == f"{tony.name} use {REMUYUKEN_NAME}"

    def test_specials_arnaldor(self, arnaldor):
        special_taladoken = GenerateMoves.special(
            moves_message=ARNOLD_TALADOKEN_COMBINATION,
            name_fighter=arnaldor.name,
            special_name=TALADOKEN_NAME,
            combination=ARNOLD_TALADOKEN_COMBINATION,
            energy=ARNOLD_TALADOKEN_ENERGY,
        )
        special_remuyuken = GenerateMoves.special(
            moves_message=ARNOLD_REMUYUKEN_COMBINATION,
            name_fighter=arnaldor.name,
            special_name=REMUYUKEN_NAME,
            combination=ARNOLD_REMUYUKEN_COMBINATION,
            energy=ARNOLD_REMUYUKEN_ENERGY,
        )
        assert special_taladoken["message"] == f"{arnaldor.name } use {TALADOKEN_NAME}"
        assert special_remuyuken["message"] == f"{arnaldor.name} use {REMUYUKEN_NAME}"
