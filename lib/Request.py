import urllib.request
import json
import time
import requests


class Request:
    step_interval = 0
    max_delay = 0

    def __init__(self, si, md):
        self.step_interval = si
        self.max_delay = md

    def send_request(self, url):
        requests.post(url)
        # while True:
        #     try:
        #         with urllib.request.urlopen(url) as response:
        #             r = response.read()
        #     except IOError:
        #         pass  # Fall through to the retry loop.
        #     else:
        #         # If we didn't get an IOError then parse the result.
        #         result = json.loads(r.replace('\\n', ''))
        #         if result['status'] == 'OK':
        #             return result
        #         elif result['status'] != 'UNKNOWN_ERROR':
        #             # Many API errors cannot be fixed by a retry, e.g. INVALID_REQUEST or
        #             # ZERO_RESULTS. There is no point retrying these requests.
        #             raise Exception(result['error_message'])
        #
        #     if self.step_interval > self.max_delay:
        #         raise Exception('Too many retry attempts.')
        #     print("Waiting" + str(self.step_interval) + "seconds before retrying.")
        #     time.sleep(self.step_interval)
        #     self.step_interval *= 2  # Increase the delay each time we retry.
