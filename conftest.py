import pytest
from selene.support.shared import browser


@pytest.fixture
def browser_open():
    browser.config.window_width = 1980
    browser.config.window_height = 1200
    browser.config.browser_name = 'chrome'
    browser.open('https://google.com')

    yield

    browser.quit()
