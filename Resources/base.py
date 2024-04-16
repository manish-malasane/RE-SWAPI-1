class ResourceBase(object):
    def __init__(self):
        self.home_url = "https://swapi.dev/api"

    def get_count(self):
        raise NotImplementedError

    def get_resource_urls(self):
        raise NotImplementedError

    def get_random_data(self, resource_id):
        raise NotImplementedError
