#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 20:07:46 2018

@author: mashiksa
"""

import logging as log
import logging.config
from time import sleep

from rest import server

if __name__ == '__main__':
    # loading and initiating log configuration
    log.config.fileConfig("logging.ini")

    log.info(" -------> Starting restful service...")
    server.runme()
    sleep(2)