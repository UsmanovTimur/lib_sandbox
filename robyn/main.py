from robyn import Robyn

app = Robyn(__file__)


@app.get("/")
async def h(request):
    return "Hello, world!"


app.start(port=8000, host="0.0.0.0")
