"""
Title: run_app
Author: Mirte Draaijer, Ivar Lottman, Kasthury Inparajah, Storm Steller
Date: 1-4-2024
Version: 1.0
Summary: This script functions as the main module of the website. and calls
the flak app from main.py
"""
from main import app


def run_website():
    """
    This function is for running the website
    """
    app.debug = False
    app.run()

    return None


run_website()
