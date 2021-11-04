from dataclasses import dataclass, field, asdict
from typing import Any, Union, List, Dict
from dacite import from_dict

from created_data_class.championStat import ChampionStat
from created_data_class.damageStat import DamageStat
from created_data_class.position import Position


@dataclass
class ParticipantFrame:

    championStats: ChampionStat
    damageStats: DamageStat
    position: Position
    currentGold: int = field(default=None)
    goldPerSecond: int = field(default=None)
    jungleMinionsKilled: int = field(default=None)
    level: int = field(default=None)
    minionsKilled: int = field(default=None)
    participantId: int = field(default=None)
    timeEnemySpentControlled: int = field(default=None)
    totalGold: int = field(default=None)
    xp: int = field(default=None)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ParticipantFrame":
        return from_dict(cls, data=data)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
