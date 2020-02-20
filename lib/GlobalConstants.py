from urllib.parse import quote
import datetime

# custom params
API_KEY = "AIzaSyA1dwWn7_VfAJ0UlvaNhdeUYbkkGyEUbkw"
START_POINT = quote("Commerzone IT Park Yerwada Pune 411006")
END_POINT = quote("Harmony - Chandrarang Developers Damodar Jagtap Path Pimple Gurav Pune 411061")
BASE_URL = "https://maps.googleapis.com/maps/api/distancematrix/"
OUTPUT_FORMAT = "json"  # can be "json / xml"
TRANSPORT = "driving"  # can be "driving / walking / bicycling / transit"
LANGUAGE = "en"  # en for English

# inferred params
PARAM_SEP = "&"
ORIGIN = "origins=" + START_POINT
DEST = "destinations=" + END_POINT
KEY = "key=" + API_KEY
MODE = "mode=" + TRANSPORT
LANGUAGE = "language=" + LANGUAGE

CURRENT_TIME = datetime.datetime.now()
OFFSET = datetime.timedelta(minutes=10)
UTC_START = datetime.datetime(1970, 1, 1)

SECONDS = int(((CURRENT_TIME + OFFSET) - UTC_START).total_seconds())

DEP_TIME = "departure_time=" + str(SECONDS)

PARAMETERS = OUTPUT_FORMAT + "?" + ORIGIN + PARAM_SEP + DEST + PARAM_SEP + MODE + PARAM_SEP + LANGUAGE + PARAM_SEP + DEP_TIME + PARAM_SEP + KEY

API_URL = BASE_URL + OUTPUT_FORMAT + "?" + PARAMETERS
