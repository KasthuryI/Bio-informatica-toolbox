"""
HTML validation test
console command:
python3 -m pytest
"""
import pytest
import html5lib
from run_app import app
from pathlib import Path


testfolder = Path(__file__).parent /"test_files_map"
@pytest.fixture
def client():
    return app.test_client()


def test_root(client):
    response = client.get('/')
    assert response.status_code == 200


def test_input_form(client):
    response = client.post('/succes', data={"file": ((testfolder/"good_test_fastq.fastq").open('rb'), 'filename.fastq', '')})
    assert response.status_code == 200


def test_trim_form(client):
    response = client.post('/options_page', data={"minlen":"30","crop":"30"})
    assert response.status_code == 200

@pytest.mark.parametrize('uri',['/about','/homepage','/uploadpage','fastqc','/trimmomatic','/contact','/how_does_it_work','/diclaimer'])
def test_html_validation(client, uri):
    response = client.get(uri)
    assert response.status_code == 200
    try:
        parser = html5lib.HTMLParser(strict=True, namespaceHTMLElements=False)
        htmldoc = parser.parse(response.data)
    except html5lib.html5parser.ParseError as error:
        pytest.fail(f'{error.__class__.__name__}:{str(error)}',pytrace=False)