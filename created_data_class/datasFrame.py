from dataclasses import dataclass, field, asdict
from typing import Any, Union, List, Dict
from dacite import from_dict
from created_data_class.metadata import Metadata
from created_data_class.info import Info

@dataclass
class DatasFrame:

    metadata: Metadata
    info: Info

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DatasFrame":
        return from_dict(cls, data=data)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
