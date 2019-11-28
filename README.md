The Almost Algebraic WSGI Framework

The main goal of this framework is to abuse the dunder methods to compose a web app.

This first concept uses the `__add__()` dunder method to combine middlewares into applications

Next concepts to apply:

* `__sub__()` - dunder to remove responces and requests or middlewares
* `__next__()`, `__iter__()`  - in conjuction with `__str__()` to generate a human readable pipeline of the app
* determine what the other math operators mean in the context of middlewares, applications, and the web request cycle
* Add support for POST/PUT (and other HTTP actions)
* complete SQLite DB support as persistent storage
* design templating that follows the idea of the framework