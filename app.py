from aiohttp import web
from application.equation.Equation import Equation
from application.router.Router import Router
from application.socket.Socket import Socket
import socketio

app = web.Application()
sio = socketio.AsyncServer()
sio.attach(app)
equation = Equation()

Router(app,web)
Socket(sio)

async def on_startup(app):
    print('Я родился')

async def on_shutdown(app):
    print('Я помер')

app.on_startup.append(on_startup)
app.on_shutdown.append(on_shutdown)
web.run_app(app)