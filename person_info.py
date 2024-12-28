from typing import List, Dict
from dataclasses import dataclass

@dataclass
class PersonInfo:
    name: str
    other_names: List[str]
    nationality: str
    profiles: Dict[str, str]

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "other_names": self.other_names,
            "nationality": self.nationality,
            "profiles": self.profiles
        }

    @staticmethod
    def from_dict(data: Dict) -> 'PersonInfo':
        return PersonInfo(
            name=data["name"],
            other_names=data.get("other_names", []),
            nationality=data.get("nationality", ""),
            profiles=data.get("profiles", {})
        )