from dataclasses import dataclass, field, asdict
from typing import Any, Union, List, Dict
from dacite import from_dict

@dataclass
class Participant:

    participantId: int = field(default=1)
    puuid: str = field(default="ZNwHkHel7nDxyki239CvRenMNIjWjl-Rv5C3YdaK1SVj4wcEmsNto2tEqbZRB6AWGmh_Hhg72JL-dg")

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Participant":
        return from_dict(cls, data=data)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
