from utility.urls_ import fetch_data
from Resources.base import ResourceBase


class People(ResourceBase):
    def __init__(self):
        super().__init__()
        self.relative_url = "/people"

    def get_count(self):
        complete_url = self.home_url + self.relative_url
        response = fetch_data(complete_url)
        count = response.get("count")
        return count

    def get_resource_urls(self):
        urls = []
        i = 0
        url = self.home_url + self.relative_url
        response = fetch_data(url)
        result = response.get("results")
        # while i < len(result):
        #     urls.append(result[i]["url"])
        #     i += 1
        for i in result:
            urls.append((i.get("url")))
        return urls

    def get_random_data(self, resource_id):
        url = self.home_url + self.relative_url + f"/{resource_id}"
        response = fetch_data(url)
        return response
