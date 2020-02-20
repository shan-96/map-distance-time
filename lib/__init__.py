from lib import GlobalConstants, Response, Request
from requests import get

if __name__ == '__main__':
    ip = get('https://api.ipify.org').text
    print('Requesting from IP Address:', ip)

    url = GlobalConstants.API_URL

    req = Request.Request(GlobalConstants.API_KEY)

    result = req.send_request()

    result = Response.Response.read(result)
