from dataclasses import dataclass, field, asdict
from typing import Any, Union, List, Dict
from dacite import from_dict

@dataclass
class ChampionStat:

    abilityHaste: int = field(default=0)
    abilityPower: int = field(default=0)
    armor: int = field(default=23)
    armorPen: int = field(default=0)
    armorPenPercent: int = field(default=0)
    attackDamage: int = field(default=25)
    attackSpeed: int = field(default=100)
    bonusArmorPenPercent: int = field(default=0)
    bonusMagicPenPercent: int = field(default=0)
    ccReduction: int = field(default=0)
    cooldownReduction: int = field(default=0)
    health: int = field(default=520)
    healthMax: int = field(default=520)
    healthRegen: int = field(default=0)
    lifesteal: int = field(default=0)
    magicPen: int = field(default=0)
    magicPenPercent: int = field(default=0)
    magicResist: int = field(default=28)
    movementSpeed: int = field(default=335)
    omnivamp: int = field(default=0)
    physicalVamp: int = field(default=0)
    power: int = field(default=490)
    powerMax: int = field(default=490)
    powerRegen: int = field(default=0)
    spellVamp: int = field(default=0)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ChampionStat":
        return from_dict(cls, data=data)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
