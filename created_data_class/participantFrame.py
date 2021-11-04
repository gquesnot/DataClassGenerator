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
    currentGold: int = field(default=500)
    goldPerSecond: int = field(default=0)
    jungleMinionsKilled: int = field(default=0)
    level: int = field(default=1)
    minionsKilled: int = field(default=0)
    participantId: int = field(default=1)
    timeEnemySpentControlled: int = field(default=0)
    totalGold: int = field(default=500)
    xp: int = field(default=0)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ParticipantFrame":
        return from_dict(cls, data=data)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
