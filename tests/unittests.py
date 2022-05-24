import unittest
from function import parse_api


class TestApiCallFunction(unittest.TestCase):

    def setUp(self) -> None:
        self.data = parse_api(
            "https://api.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid=10584f1ecf9dc5c83161989bc8c42410"
        )
        return super().setUp()

    def test_return_json_data(self):
        self.assertEqual(type(self.data[0]), dict)

    def test_response_status(self):
        self.assertEqual(self.data[1], 200)

    
