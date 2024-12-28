import unittest
from content_manager import ContentManager
from person_info import PersonInfo

class TestContentManager(unittest.TestCase):
    def setUp(self):
        self.manager = ContentManager("test_content_persons")
        self.person = PersonInfo(
            name="Jane Doe",
            other_names=["JD", "Jane"],
            nationality="Canadian",
            profiles={
                "YouTube": "https://www.youtube.com/user/janedoe",
                "Instagram": "https://www.instagram.com/janedoe"
            }
        )

    def test_add_person(self):
        self.manager.add_person(self.person)
        loaded_person = self.manager.load_person("Jane Doe")
        self.assertEqual(loaded_person.name, self.person.name)

if __name__ == "__main__":
    unittest.main()
