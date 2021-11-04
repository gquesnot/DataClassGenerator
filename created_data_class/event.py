from dataclasses import dataclass, field, asdict
from typing import Any, Union, List, Dict
from dacite import from_dict

@dataclass
class Event:

    realTimestamp: int = field(default=1635796811348)
    timestamp: int = field(default=0)
    type: str = field(default="PAUSE_END")

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Event":
        return from_dict(cls, data=data)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
