#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 20:53:19 2018

@author: mashiksa
"""

import logging as log
from flask import Blueprint, abort, request, jsonify
from nlp_core import nlp_service

core_blueprint = Blueprint(name="system-health", import_name=__name__)

@core_blueprint.route('/ping', methods=['GET'])
def ping():
    return nlp_service.ping()

@core_blueprint.route('/health', methods=['GET'])
def health_check():
    return nlp_service.health_check()

blueprint = Blueprint(name="nlpservice-core", import_name=__name__)

@blueprint.route("/wordpre", methods = ['POST'])
def word2vec():
    print(request.is_json)
    content = request.get_json()
    comments = nlp_service.pre_process(content['comment'])    
    return "User : {}".format(comments)
    #return "User Name {}".format(content["user"])

@blueprint.route("/word2vec_spacy", methods = ['POST'])
def spacy2vec():
    if request.is_json:
        content = request.get_json()
        comments = nlp_service.wordEmbed(content['comment'])
        return "spacy2vec : {}".format(comments)
    else:
        return "Error No Json Found Post format : {\"comment\":\"This is a sentence\"}"