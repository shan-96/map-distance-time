import googlemaps
from lib import GlobalConstants


class Request:
    gmaps = None

    def __init__(self, key):
        self.gmaps = googlemaps.Client(key=key)

    def send_request(self):
        matrix = self.gmaps.distance_matrix(GlobalConstants.ORIGIN, GlobalConstants.DEST, mode="driving", departure_time=GlobalConstants.SECONDS)
        return matrix
