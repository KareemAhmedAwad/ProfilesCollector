from extractors import ContentExtractor
from pathlib import Path

class YouTubeExtractor(ContentExtractor):
    def fetch(self, profile_link: str, target_folder: Path):
        print(f"Fetching YouTube content from {profile_link}...")
        sample_file = target_folder / "youtube_sample_video.mp4"
        with open(sample_file, "w") as f:
            f.write(f"Simulated YouTube content from {profile_link}")
