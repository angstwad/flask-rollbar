# flask-rollbar

Sets up a sane/reasonable Rollbar configuration for Flask apps, based
upon Rollbar's suggestions and personal experience.  Ignores some
400-level exceptions by default but can be customized.

Flask-Rollbar expects there to be two values defined on the Flask app's config:
``ROLLBAR_TOKEN`` and ``ROLLBAR_ENV``.  The ``ROLLBAR_TOKEN`` is your app's
server-side POST token, and the environment is the Rollbar environment to which
your events will be posted.  Flask-Rollbar defaults to an environment of "dev".

Here's a quick example of initializing this plugin in:

    from flask import Flask
    from flask.ext.rollbar import Rollbar

    app = Flask(__name__)
    app.config['ROLLBAR_TOKEN'] = 'mytoken'
    app.config['ROLLBAR_ENV'] = 'testing'

    Rollbar(app)

    @app.route('/')
    def this_will_fail():
        1/0

Customizing ignored exceptions:

```
from werkzeug.exceptions import Unauthorized, Forbidden, NotFound

ignored = [Unauthorized, Forbidden, NotFound]
Rollbar(app, ignore_exc=ignored)
```
