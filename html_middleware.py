from middleware import MiddleWare
from web_objects import Response


class HTMLStart(MiddleWare):
    def __call__(self, request, response):
        val = Response('<html>')
        return request, response + val


class HTMLEnd(MiddleWare):
    def __call__(self, request, response):
        val = Response('</html>')
        return request, response + val


class HTMLHeaderStart(MiddleWare):
    def __call__(self, request, response):
        val = Response('<head>')
        return request, response + val


class HTMLHeaderEnd(MiddleWare):
    def __call__(self, request, response):
        val = Response('</head>')
        return request, response + val


class HTMLBodyStart(MiddleWare):
    def __call__(self, request, response):
        val = Response('<body>')
        return request, response + val


class HTMLBodyEnd(MiddleWare):
    def __call__(self, request, response):
        val = Response('</body>')
        return request, response + val


class MetaUTF8(MiddleWare):
    def __call__(self, request, response):
        val = Response('<meta charset="UTF-8">')
        return request, response + val


class PathAppender(MiddleWare):
    def __call__(self, request, response):
        path = request['PATH_INFO']
        path_return = Response(f'<p>This is from this path <bold>{path}</bold></p>')
        return request, response + path_return


class MadeByPete(MiddleWare):
    def __call__(self, request, response):
        val = Response('<small> Made By Peter P. </small>')
        return request, response + val


end_sig = MadeByPete()
path_appender = PathAppender()
html_start = HTMLStart()
html_end = HTMLEnd()
meta_utf8 = MetaUTF8()
header_start = HTMLHeaderStart()
header_end = HTMLHeaderEnd()
body_start = HTMLBodyStart()
body_end = HTMLBodyEnd()
