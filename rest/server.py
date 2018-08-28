# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask
from flask import request
from nlp_core import nlp_service
import logging as log
from flask_prometheus import monitor
from rest import nlpservice_urls
from rest import config

server = Flask(__name__)
server.register_blueprint(nlpservice_urls.core_blueprint)
server.register_blueprint(nlpservice_urls.blueprint)


@server.route('/')
def index():
    return "HEKMA Word2Vector Embedding Services"

               
@server.route('/qry')
def query_example():
    language = request.args.get('val1') #if key doesn't exist, returns None
    return '''<h1>The language value is: {}</h1>'''.format(language)

def runme():
    log.info("----> updating NLTK wordnet...")
    #monitor(server, port=config.PROMETHEUS_PORT, addr="")
    #server.run(host=config.HOST, debug=config.DEBUG)
    server.run()
    
if __name__ == "__main__":
    # Start 
    runme()