from flask import render_template
from . import main

@main.errorhandler(404)
def four_oh_four(error):
    
    return render_template('404.html'),404
   