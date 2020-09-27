import sys
sys.path[0] = 'd:\\Univer\\Alg\\PythonProject1'
from application.equation.Equation import Equation

class Router:
    def __init__(self, app, web):
        self.web = web
        app.router.add_static('/js/', path = str('./public/js/'))
        app.router.add_static('/css/', path = str('./public/css/'))
        self.equation = Equation
        app.router.add_route('GET', '/test', self.testHandler)
        app.router.add_route('GET', '/pow/{value}/{pow}',self.powHandler)
        app.router.add_route('*', '/', self.staticHandler)
        app.router.add_route('GET', '/equation',self.equationHandler)
    
    def testHandler(self,request):
        return self.web.json_response(dict(result = 'ok'))

    def staticHandler(self,request):
        return self.web.FileResponse('./public/index.html')

    def powHandler(self,request):
        value = request.match_info.get('value')
        pow = request.match_info.get('pow')
        name = request.rel_url.query['name']
        result = float(value) ** float (pow)
        return self.web.json_response(dict(result = result, name = name))

    def equationHandler(self,request):
        return self.web.json_response(self.equation.squareEquarion(1,2,3))



