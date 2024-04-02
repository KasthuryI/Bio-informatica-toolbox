"""
Title: run_app
Author: Mirte Draaijer, Ivar Lottman, Kasthury Inparajah, Storm Steller
Date: 2-4-2024
Version: 1.0
Summery: This module is for launcing the flask server it imports the functions
from upload_page_script
"""
from upload_page_script import app


def run_website():
    """
    This function is for running the website
    param:None
    Return:Hosting website
    """
    # debug console
    app.debug = True
    # run object
    app.run()
    return None


run_website()
