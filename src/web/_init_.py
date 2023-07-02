from flask import Flask, request, redirect, url_for
from flask_restful import Api
from flask_cors import CORS

#start import block; free edit
from web.resource.gptbot import GDPBot

#end import block

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024
CORS(app, supports_credentials=True) # CORS handle

'''add api resource'''
api = Api(app)

#start mode-use block; free edit
api.add_resource(GDPBot, '/api/gpt')

#end mode-use block
