from uuid import uuid4


class WebObject(object):
    def __init__(self, request, response):
        self._request = request
        self._response = response

    def __add__(self, other):
        if isinstance(other, WebObject):
            self._request += other._request
            self._response += other._response

        if isinstance(other, Request):
            self._request += other._request

        if isinstance(other, Response):
            self._response += other._response

        return self


class Request(object):
    def __init__(self, key=None, content=None):
        self._content = {}
        if key and content:
            self._content[key] = content
        self._id = uuid4()

    def __add__(self, other):
        if isinstance(other, Request):
            self._content = {**self._content, **other._content}

        if isinstance(other, Response):
            return WebObject(self, other)

        if isinstance(other, WebObject):
            other += self
            return other

        return self

    def __getitem__(self, key):
        return self._content.get(key)


class Response(object):
    def __init__(self, content, handler=None):
        self._handler = handler
        self._handler_status = '200 OK'
        self._handler_headers = [('Content-type', 'text/html; charset=utf-8')]
        self._internal_storage = {}
        assert type(content) == str
        self._content = [content]
        self._id = uuid4()

    def __add__(self, other):
        if isinstance(other, Response):
            assert all(type(c) == str for c in other._content)
            self._content += other._content

        if isinstance(other, Request):
            return WebObject(other, self)

        if isinstance(other, WebObject):
            other += self
            return other

        return self

    def __setitem__(self, key, value):
        if self._handler:
            if key == 'header':
                self._handler_headers.append(value)
            if key == 'status':
                self._handler_status = value

        self._internal_storage[key] = value

    def __bytes__(self):
        if self._handler:
            self._handler(self._handler_status, self._handler_headers)

        return bytes(''.join(self._content), 'utf-8')
