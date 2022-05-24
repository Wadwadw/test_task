import requests as r
import sys
import json


def parse_api(url):
    response = r.get(url)
    json_data = json.loads(response.text)
    return json_data, response.status_code




if __name__ == "__main__":
    url = sys.argv[1]
    print(parse_api(url)[0])
