from extractors import ContentExtractor
from pathlib import Path

class InstagramExtractor(ContentExtractor):
    def fetch(self, profile_link: str, target_folder: Path):
        print(f"Fetching Instagram content from {profile_link}...")
        sample_file = target_folder / "instagram_sample_image.jpg"
        with open(sample_file, "w") as f:
            f.write(f"Simulated Instagram content from {profile_link}")
