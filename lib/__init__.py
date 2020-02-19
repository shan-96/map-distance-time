from lib import GlobalConstants, Response, Request

url = GlobalConstants.API_URL

req = Request.Request(0.1, 300)

result = req.send_request(url)

result = Response.Response.read(result)
