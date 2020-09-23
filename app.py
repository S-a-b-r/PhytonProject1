from aiohttp import web
import Equation

equation = Equation.Equation()
app = web.Application()

def testHandler(request):
    return web.json_response(dict(result = 'ok'))

def staticHandler(request):
    return web.FileResponse('./public/index.html')

def powHandler(request):
    value = request.match_info.get('value')
    pow = request.match_info.get('pow')
    result = float(value) ** float (pow)
    return web.json_response(dict(result = result))

def equationHandler(request):
    return web.json_response(equation.squareEquarion(1,2,3))


def human(request):
    return web.json_response()

app.router.add_route('GET', '/test', testHandler)
app.router.add_route('GET', '/pow/{value}/{pow}',powHandler)
app.router.add_route('*', '/', staticHandler)
app.router.add_route('GET', '/equation',equationHandler)


async def on_startup(app):
    print('Я родился')

async def on_shutdown(app):
    print('Я помер')

app.on_startup.append(on_startup)
app.on_shutdown.append(on_shutdown)
web.run_app(app)