from .youtube_extractor import YouTubeExtractor
from .instagram_extractor import InstagramExtractor
from .twitter_extractor import TwitterExtractor
from .vimeo_extractor import VimeoExtractor

class ContentExtractor:
    def fetch(self, profile_link: str, target_folder: Path):
        raise NotImplementedError
