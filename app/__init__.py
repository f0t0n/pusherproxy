#!/usr/bin/env python

from flask import Flask, request, make_response
import pusher
import json


app = Flask(__name__)
app.config.from_object('app.config.ProductionConfig')
app.config.from_envvar('PUSHER_PROXY_CONFIG')


@app.route('/pusher_auth', methods=['post', 'get'])
def pusher_auth():
    channel_name = request.args.get('channel_name')
    socket_id = request.args.get('socket_id')
    channel_data = dict(user_id=socket_id, name=channel_name)
    p = _get_pusher_instance()
    auth = p[channel_name].authenticate(socket_id, channel_data)
    response_text = "{callback_name}({json})".format(
        callback_name=request.args.get('callback'),
        json=json.dumps(auth)
    )
    response = make_response(response_text)
    response.headers['Content-Type'] = 'application/javascript'
    return response


def _get_pusher_instance():
    return pusher.Pusher(app_id=app.config['PUSHER']['APP_ID'],
                         key=app.config['PUSHER']['KEY'],
                         secret=app.config['PUSHER']['SECRET'])
