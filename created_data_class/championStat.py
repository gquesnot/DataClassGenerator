from dataclasses import dataclass, field, asdict
from typing import Any, Union, List, Dict
from dacite import from_dict

@dataclass
class ChampionStat:

    abilityHaste: int = field(default=None)
    abilityPower: int = field(default=None)
    armor: int = field(default=None)
    armorPen: int = field(default=None)
    armorPenPercent: int = field(default=None)
    attackDamage: int = field(default=None)
    attackSpeed: int = field(default=None)
    bonusArmorPenPercent: int = field(default=None)
    bonusMagicPenPercent: int = field(default=None)
    ccReduction: int = field(default=None)
    cooldownReduction: int = field(default=None)
    health: int = field(default=None)
    healthMax: int = field(default=None)
    healthRegen: int = field(default=None)
    lifesteal: int = field(default=None)
    magicPen: int = field(default=None)
    magicPenPercent: int = field(default=None)
    magicResist: int = field(default=None)
    movementSpeed: int = field(default=None)
    omnivamp: int = field(default=None)
    physicalVamp: int = field(default=None)
    power: int = field(default=None)
    powerMax: int = field(default=None)
    powerRegen: int = field(default=None)
    spellVamp: int = field(default=None)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ChampionStat":
        return from_dict(cls, data=data)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
