import unittest
from pathlib import Path
import shutil
from content_manager import ContentManager
from person_info import PersonInfo

class TestContentManager(unittest.TestCase):
    def setUp(self):
        self.test_dir = Path("test_content")
        self.manager = ContentManager(self.test_dir)
        self.person = PersonInfo(
            name="Test Person",
            other_names=["TP"],
            nationality="Test",
            profiles={"YouTube": "https://youtube.com/test"}
        )

    def tearDown(self):
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)

    def test_add_person(self):
        self.manager.add_person(self.person)
        loaded_person = self.manager.load_person("Test Person")
        self.assertEqual(loaded_person.name, self.person.name)
        self.assertEqual(loaded_person.profiles, self.person.profiles)

if __name__ == '__main__':
    unittest.main()