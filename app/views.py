# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os, json
# Flask modules
from flask   import render_template, request, jsonify
from jinja2  import TemplateNotFound
# App modules
from app      import app
import stripe



# Product Index
@app.route('/products')
def hello_world():
  return 'Hello World akhil'