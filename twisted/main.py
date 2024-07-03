from twisted.web import server, resource
from twisted.internet import reactor, endpoints


class Counter(resource.Resource):
    isLeaf = True
    numberRequests = 0

    def render_GET(self, request):
        self.numberRequests += 1
        request.setHeader(b"content-type", b"text/plain")
        content = "Hello World!"
        return content.encode("ascii")


endpoints.serverFromString(reactor, "tcp:8000").listen(server.Site(Counter()))
reactor.run()
