from middleware import MiddleWare
from web_objects import Response


class Router(MiddleWare):
    def __init__(self, **kwargs):
        self._mapping = {**kwargs}

    def __call__(self, request, response):
        callable = self._mapping.get(request['PATH_INFO'])

        if callable:
            return callable(request, response)

        return request, response

    def __setitem__(self, key, value):
        self._mapping[key] = value
        return value

    def __getitem__(self, key):
        return self._mapping.get(key)


class ReturnHelloWorld(MiddleWare):
    def __call__(self, request, response):
        hello = Response('<H1> Hello </H1>')
        world = Response('<H2> World! </H2>')
        hello_world = hello + world
        return request, response + hello_world


class PyYYC(MiddleWare):
    def __call__(self, request, response):
        path_return = Response(f'<p>Thank you for listening. Hopefully you learned something today!</p>')
        path_return += Response(f'<p>Thank you for comming to Nov 27 PyYYC meetup!</p>')
        return request, response + path_return


# Router
router = Router()
router['/'] = ReturnHelloWorld()
router['/pyyyc'] = PyYYC()
