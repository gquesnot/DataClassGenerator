from dataclasses import dataclass, field, asdict
from typing import Any, Union, List, Dict
from dacite import from_dict
from created_data_class.frame import Frame
from created_data_class.participant import Participant

@dataclass
class Info:

    frames: List[Frame]
    participants: List[Participant]
    frameInterval: int = field(default=60000)
    gameId: int = field(default=5533819036)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Info":
        return from_dict(cls, data=data)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
