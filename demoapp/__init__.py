from flask import Flask, jsonify
from chatfirst.models import ActionResponse

application = Flask(__name__)


@application.route('/')
def get_index():
    """Renders the home page."""
    retobj = ActionResponse()
    retobj.messages.append("Hello world!")

    # from chatfirst.client import ChatFirst
    # client = Chatfirst(<YOUR_USER_TOKEN>)
    # my_bots = client.bots_list()
    return jsonify(retobj.to_json()), 200
