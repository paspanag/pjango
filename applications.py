class NotAllowed(Exception):
    pass


class WebApp(object):
    def __init__(self, *callables):
        self._all_callables = [c for c in callables]
        self._index = 0

    def __add__(self, other):
        if isinstance(other, WebApp):
            for c in list(other):
                self._all_callables.append(c)
        elif other != None:
            self._all_callables.append(other)

        return self

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        try:
            c = self._all_callables[self._index]
            self._index += 1
            return c
        except IndexError:
            raise StopIteration

    def __call__(self, request, response):
        for c in self._all_callables:
            request, response = c(request, response)

        return [bytes(response)]
