"""
Website runspace

"""
from upload_page_script import app


def run_website():
    """
    This function is for running the website
    """
    app.debug = True
    app.run()

    return None


run_website()
