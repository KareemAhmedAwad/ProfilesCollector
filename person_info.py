from typing import List, Dict

class PersonInfo:
    def __init__(self, name: str, other_names: List[str], nationality: str, profiles: Dict[str, str]):
        self.name = name
        self.other_names = other_names
        self.nationality = nationality
        self.profiles = profiles

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
