from extractors import ContentExtractor
from pathlib import Path

class TwitterExtractor(ContentExtractor):
    def fetch(self, profile_link: str, target_folder: Path):
        print(f"Fetching Twitter content from {profile_link}...")
        sample_file = target_folder / "twitter_sample_tweet.txt"
        with open(sample_file, "w") as f:
            f.write(f"Simulated Twitter content from {profile_link}")
