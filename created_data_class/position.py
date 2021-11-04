from dataclasses import dataclass, field, asdict
from typing import Any, Union, List, Dict
from dacite import from_dict

@dataclass
class Position:

    x: int = field(default=554)
    y: int = field(default=581)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Position":
        return from_dict(cls, data=data)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
