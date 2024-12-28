from pathlib import Path
from abc import ABC, abstractmethod

class ContentExtractor(ABC):
    @abstractmethod
    def fetch(self, profile_link: str, target_folder: Path):
        """Fetch content from profile and save to target folder"""
        pass