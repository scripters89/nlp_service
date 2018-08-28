#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 20:00:32 2018

@author: mashiksa
"""

"""
Holds configuration attributes for rest service
"""

HOST = "68.3.248.113"
PORT = 38182
DEBUG = False
THREADS_PER_PAGE = 4
CSRF_ENABLED = True
CSRF_SESSION_KEY = "secret"
PROMETHEUS_PORT = 5000