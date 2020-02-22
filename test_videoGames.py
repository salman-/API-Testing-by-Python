import requests
import jsonpath
import json
import pytest
from Config import Config

class VideoGamesTest:

    config = Config()
    url = config.get_url()

    def test_create_a_new_videoGame(self):

        response = requests.get(self.url,headers={'Accept': 'application/json'})

        payload = {
                "id": 16,
                "name": "I am my Hero",
                "releaseDate": "2020-02-21T16:54:03.200Z",
                "reviewScore": 9.0,
                "category": "Biography",
                "rating": "9.0"
            }

        response = requests.post(self.url,data=json.dumps(payload),headers={'Content-Type': 'application/json'} )
        response = json.loads(response.text)
        assert 'status' in response.keys()
        assert 'Record Added Successfully' in response.values()

    def test_get_all_videoGames(self):

        response = requests.get(self.url,headers={'Accept': 'application/json'})
        response = json.loads(response.text)[0]
        print(response)

        assert 'id' in response.keys()
        assert 'name' in response.keys()
        assert 'releaseDate' in response.keys()
        assert 'reviewScore' in response.keys()
        assert 'category' in response.keys()
        assert 'rating' in response.keys()

    def test_get_videoGames(self):

        self.url = self.url+'/16'
        response = requests.get(self.url,headers={'Accept': 'application/json'})
        response = json.loads(response.text)

        print(response)

        assert 'id' in response.keys()
        assert 'name' in response.keys()
        assert 'releaseDate' in response.keys()
        assert 'reviewScore' in response.keys()
        assert 'category' in response.keys()
        assert 'rating' in response.keys()

    def test_delete_videoGame(self):

        self.url = self.url+'/16'
        response = requests.delete(self.url)

        response = json.loads(response.text)
        assert 'status' in response.keys()
        assert 'Record Deleted Successfully' in response.values()



