from blacksheep import Application, get

app = Application()


@get("/")
async def home():
    return "Hello, World!"
