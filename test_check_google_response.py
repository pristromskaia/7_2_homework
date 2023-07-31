from selene import browser, be, have


def test_check_google_search_yashaka(browser_open):
    browser.element('[id="L2AGLb"]').press_enter()
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in'))


def test_check_google_search_random(browser_open):
    browser.element('[id="L2AGLb"]').press_enter()
    browser.element('[name="q"]').should(be.blank).type('ERERFDFDG').press_enter()
    browser.element('[id="result-stats"]').should(have.text('0'))
