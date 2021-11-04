from dataclasses import dataclass, field, asdict
from typing import Any, Union, List, Dict
from dacite import from_dict

@dataclass
class DamageStat:

    magicDamageDone: int = field(default=None)
    magicDamageDoneToChampions: int = field(default=None)
    magicDamageTaken: int = field(default=None)
    physicalDamageDone: int = field(default=None)
    physicalDamageDoneToChampions: int = field(default=None)
    physicalDamageTaken: int = field(default=None)
    totalDamageDone: int = field(default=None)
    totalDamageDoneToChampions: int = field(default=None)
    totalDamageTaken: int = field(default=None)
    trueDamageDone: int = field(default=None)
    trueDamageDoneToChampions: int = field(default=None)
    trueDamageTaken: int = field(default=None)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DamageStat":
        return from_dict(cls, data=data)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
