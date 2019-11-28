from applications import WebApp
from web_objects import Response, Request


class MiddleWare(object):
    def __add__(self, other):
        if other is None:
            return self

        aggregate = WebApp(self)
        return aggregate + other

    def __call__(self, request, response):
        return request, response


class HeaderProcessor(MiddleWare):
    def __call__(self, request, response):
        header = Request()
        for k, v in request.items():
            header += Request(key=k, content=v)

        request = header

        return request, response


class ResponseInitializer(MiddleWare):
    def __call__(self, request, response):
        return request, Response('', handler=response)


# Make the objects
header_processor = HeaderProcessor()
response_init = ResponseInitializer()
