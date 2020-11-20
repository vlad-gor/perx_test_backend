from aiohttp import web

async def hello(request):
    return web.Response(text="Hello, perx")

app = web.Application()
app.add_routes([web.get('/', hello)])

web.run_app(app, host='127.0.0.1', port=8283)
