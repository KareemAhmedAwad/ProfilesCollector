from content_manager import ContentManager
from person_info import PersonInfo
from extractors.youtube_extractor import YouTubeExtractor
from extractors.instagram_extractor import InstagramExtractor
from extractors.twitter_extractor import TwitterExtractor
from extractors.vimeo_extractor import VimeoExtractor

if __name__ == "__main__":
    manager = ContentManager("content_persons")
    manager.register_extractor("YouTube", YouTubeExtractor())
    manager.register_extractor("Instagram", InstagramExtractor())
    manager.register_extractor("Twitter", TwitterExtractor())
    manager.register_extractor("Vimeo", VimeoExtractor())

    person = PersonInfo(
        name="John Doe",
        other_names=["JD", "John"],
        nationality="American",
        profiles={
            "YouTube": "https://www.youtube.com/user/johndoe",
            "Instagram": "https://www.instagram.com/johndoe",
            "Twitter": "https://twitter.com/johndoe",
            "Vimeo": "https://vimeo.com/johndoe"
        }
    )

    manager.add_person(person)
    manager.sync_content("John Doe")