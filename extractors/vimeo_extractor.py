from extractors import ContentExtractor
from pathlib import Path

class VimeoExtractor(ContentExtractor):
    def fetch(self, profile_link: str, target_folder: Path):
        print(f"Fetching Vimeo content from {profile_link}...")
        sample_file = target_folder / "vimeo_sample_video.mp4"
        with open(sample_file, "w") as f:
            f.write(f"Simulated Vimeo content from {profile_link}")
