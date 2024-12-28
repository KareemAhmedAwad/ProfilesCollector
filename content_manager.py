import os
import json
from pathlib import Path
from typing import Union
from person_info import PersonInfo
from extractors import YouTubeExtractor, InstagramExtractor, TwitterExtractor, VimeoExtractor

class ContentManager:
    def __init__(self, base_directory: Union[str, Path]):
        self.base_directory = Path(base_directory)
        self.creators_directory = self.base_directory / "persons"
        self.creators_directory.mkdir(parents=True, exist_ok=True)
        self.extractors = {}

    def add_person(self, person: PersonInfo):
        person_file = self.creators_directory / f"{person.name}.json"
        with open(person_file, "w") as f:
            json.dump(person.to_dict(), f, indent=4)

    def load_person(self, person_name: str) -> PersonInfo:
        person_file = self.creators_directory / f"{person_name}.json"
        if not person_file.exists():
            raise ValueError(f"Person {person_name} not found.")
        with open(person_file, "r") as f:
            data = json.load(f)
            return PersonInfo.from_dict(data)

    def sync_content(self, person_name: str):
        person = self.load_person(person_name)
        person_folder = self.base_directory / person.name
        person_folder.mkdir(parents=True, exist_ok=True)

        for website, profile_link in person.profiles.items():
            website_folder = person_folder / website
            website_folder.mkdir(exist_ok=True)
            self._fetch_content(website, profile_link, website_folder)

    def _fetch_content(self, website: str, profile_link: str, target_folder: Path):
        extractor = self._get_extractor(website)
        if extractor:
            try:
                extractor.fetch(profile_link, target_folder)
            except Exception as e:
                print(f"Failed to fetch content from {website}: {e}")
        else:
            print(f"No extractor found for {website}. Skipping...")

    def register_extractor(self, website: str, extractor):
        self.extractors[website] = extractor

    def _get_extractor(self, website: str):
        return self.extractors.get(website)
