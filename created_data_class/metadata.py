from dataclasses import dataclass, field, asdict
from typing import Any, Union, List, Dict
from dacite import from_dict

@dataclass
class Metadata:

    participants: List[str]
    dataVersion: str = field(default="2")
    matchId: str = field(default="EUW1_5533819036")

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Metadata":
        return from_dict(cls, data=data)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
