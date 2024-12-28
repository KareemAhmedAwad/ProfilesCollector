import unittest
from pathlib import Path
from content_manager import ContentManager
from person_info import PersonInfo

class TestContentManager(unittest.TestCase):
    def setUp(self):
        self.test_dir = Path("test_content_persons")
        self.manager = ContentManager(self.test_dir)
        self.person = PersonInfo(
            name="Jane Doe",
            other_names=["JD", "Jane"],
            nationality="Canadian",
            profiles={
                "YouTube": "https://www.youtube.com/user/janedoe",
                "Instagram": "https://www.instagram.com/janedoe"
            }
        )

    def tearDown(self):
        if self.test_dir.exists():
            for file in self.test_dir.glob("*"):
                file.unlink()
            self.test_dir.rmdir()

    def test_add_person(self):
        self.manager.add_person(self.person)
        loaded_person = self.manager.load_person("Jane Doe")
        self.assertEqual(loaded_person.name, self.person.name)