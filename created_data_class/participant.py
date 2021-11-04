from dataclasses import dataclass, field, asdict
from typing import Any, Union, List, Dict
from dacite import from_dict



@dataclass
class Participant:

    participantId: int = field(default=None)
    puuid: str = field(default=None)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Participant":
        return from_dict(cls, data=data)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
