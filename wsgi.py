from wsgiref.simple_server import make_server

from html_middleware import end_sig, path_appender, header_start, header_end, meta_utf8, body_end, body_start, \
    html_start, html_end
from middleware import header_processor, response_init
from routes import router

PORT = 8002
ADDRESS = '127.0.0.1'

if __name__ == '__main__':
    headers = header_start + meta_utf8 + header_end
    body = body_start + path_appender + router + end_sig + body_end
    html_section = html_start + headers + body + html_end
    app = header_processor + response_init + html_section

    with make_server('127.0.0.1', 8002, app) as full_app:
        print(f'Serving on {ADDRESS}:{PORT}')
        full_app.serve_forever()



