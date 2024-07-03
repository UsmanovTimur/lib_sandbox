import falcon.asgi

import falcon


class ThingsResource:
    async def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_TEXT
        resp.text = ('Hello world!')


app = falcon.asgi.App()

things = ThingsResource()

app.add_route('/', things)
