from pathlib import Path
import os
import json
from typing import Union, Dict
from person_info import PersonInfo
from content_extractor import ContentExtractor

class ContentManager:
    def __init__(self, storage_path: Union[str, Path]):
        self.storage_path = Path(storage_path)
        self.extractors: Dict[str, ContentExtractor] = {}
        self.storage_path.mkdir(exist_ok=True)

    def register_extractor(self, platform: str, extractor: ContentExtractor):
        self.extractors[platform] = extractor

    def add_person(self, person: PersonInfo) -> None:
        person_dir = self.storage_path / person.name
        person_dir.mkdir(exist_ok=True)
        
        info_file = person_dir / "info.json"
        with open(info_file, "w", encoding='utf-8') as f:
            json.dump(person.to_dict(), f, indent=4)

    def load_person(self, name: str) -> PersonInfo:
        info_file = self.storage_path / name / "info.json"
        if not info_file.exists():
            raise FileNotFoundError(f"Person {name} not found")
            
        with open(info_file, encoding='utf-8') as f:
            data = json.load(f)
        return PersonInfo.from_dict(data)

    def sync_content(self, name: str) -> None:
        person = self.load_person(name)
        person_dir = self.storage_path / name

        for platform, profile_link in person.profiles.items():
            if platform in self.extractors:
                extractor = self.extractors[platform]
                platform_dir = person_dir / platform
                platform_dir.mkdir(exist_ok=True)
                try:
                    extractor.fetch(profile_link, platform_dir)
                except Exception as e:
                    print(f"Error fetching {platform} content: {e}")