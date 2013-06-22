#!/usr/bin/env python

from app import app

if __name__ == '__main__':
    app.run(debug=app.debug, host='127.0.0.1', port=5000)
