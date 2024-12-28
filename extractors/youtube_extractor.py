from ..content_extractor import ContentExtractor
from pathlib import Path
import requests

class YouTubeExtractor(ContentExtractor):
    def fetch(self, profile_link: str, target_folder: Path):
        print(f"Fetching YouTube content from {profile_link}...")
        metadata_file = target_folder / "metadata.json"
        with open(metadata_file, "w") as f:
            f.write(f'{{"source": "{profile_link}", "type": "youtube"}}')