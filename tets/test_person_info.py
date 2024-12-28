import unittest
from person_info import PersonInfo

class TestPersonInfo(unittest.TestCase):
    def test_person_info(self):
        person = PersonInfo(
            name="John Doe",
            other_names=["JD", "John"],
            nationality="American",
            profiles={
                "YouTube": "https://www.youtube.com/user/johndoe",
                "Instagram": "https://www.instagram.com/johndoe"
            }
        )
        data = person.to_dict()
        self.assertEqual(data["name"], "John Doe")

    def test_from_dict(self):
        data = {
            "name": "John Doe",
            "other_names": ["JD", "John"],
            "nationality": "American",
            "profiles": {
                "YouTube": "https://www.youtube.com/user/johndoe",
                "Instagram": "https://www.instagram.com/johndoe"
            }
        }
        person = PersonInfo.from_dict(data)
        self.assertEqual(person.name, "John Doe")

if __name__ == "__main__":
    unittest.main()
