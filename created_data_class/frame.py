from dataclasses import dataclass, field, asdict
from typing import Any, Union, List, Dict
from dacite import from_dict
from created_data_class.event import Event
from created_data_class.participantFrame import ParticipantFrame

@dataclass
class Frame:

    events: List[Event]
    participantFrames: Dict[str, ParticipantFrame]
    timestamp: int = field(default=None)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Frame":
        return from_dict(cls, data=data)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
