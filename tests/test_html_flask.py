"""
Title: test_html_flask
Author: Mirte Draaijer, Ivar Lottman, Kasthury Inparajah, Storm Steller
Date: 1-4-2024
Version: 1.0
HTML validation test
console command:
python3 -m pytest
"""
import pytest
import html5lib
import os
from run_app import app
from pathlib import Path

#second_testfolder = Path(__file__).parent/"file_uploading"
#tritest = second_testfolder + "filename.fastq"
testfolder = Path(__file__).parent /"test_files_map"
@pytest.fixture
def client():
    return app.test_client()


def test_root(client):
    response = client.get('/')
    assert response.status_code == 200


def test_input_form(client):
    response = client.post('/succes', data={"file": ((testfolder/"good_test_fastq.fastq").open('rb'), 'file.filename', '')})
    assert response.status_code == 200


def test_trim_form(client):
    #with client.session_transaction() as session:
        # set a user id without going through the login route
        #session["filename"] = "file.filename"

    #path = os.getcwd() + "../" + "tools/Trimmomatic-0.39"
    #print(path)
    #os.chdir(path)
    response = client.post('/options_page', data={"leading":"3", "trailing":"3", "sliding":"4:15", "minlen":"75", "crop":"100",})
    assert response.status_code == 200


@pytest.mark.parametrize('uri', ['/about',
                                '/homepage', '/uploadpage', 'fastqc'
                                ,'/trimmomatic', '/contactpage', '/how_does_it_work', '/disclaimer'])
def test_html_validation(client, uri):
    response = client.get(uri)
    assert response.status_code == 200
    try:
        parser = html5lib.HTMLParser(strict=True, namespaceHTMLElements=False)
        htmldoc = parser.parse(response.data)
    except html5lib.html5parser.ParseError as error:
        pytest.fail(f'{error.__class__.__name__}:{str(error)}',pytrace=False)
