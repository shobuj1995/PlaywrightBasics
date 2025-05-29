import os
import json
import pytest

@pytest.fixture(scope="session")
def credentials():
    here = os.path.dirname(os.path.abspath(__file__))  # folder where conftest.py lives
    path = os.path.join(here, "Data", "credentials.json")  # note 'Data' with uppercase D
    with open(path) as f:
        data = json.load(f)
    return data

@pytest.fixture
def launch_browser(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()
