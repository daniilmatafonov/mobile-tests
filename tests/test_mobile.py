import allure
import pytest
from allure_commons._allure import StepContext, step
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selene import have, be
from selene.support._logging import wait_with
from selene.support.shared import browser

from configuration import config
from utilities.utils import add_video

FIRST_CHECK_EXPECT = 'The Free Encyclopedia'
SECOND_CHECK_EXPECT = 'New ways to explore'
THIRD_CHECK_EXPECT = 'Reading lists with sync'
FORTH_CHECK_EXPECT = 'Send anonymous data'

textView = "org.wikipedia.alpha:id/primaryTextView"
forwardButton = "org.wikipedia.alpha:id/fragment_onboarding_forward_button"


@pytest.fixture(scope='function', autouse=True)
def init():
    browser.config.timeout = config.settings.timeout
    browser.config._wait_decorator = wait_with(
        context=StepContext
    )

    browser.config.driver = webdriver.Remote(
        config.settings.remote_url, options=config.settings.driver_options
    )

    return browser


@allure.tag('mobile')
@allure.title('Test screen checking')
def test_skip_wiki_search_screens():
    with step('First screen checking'):
        print(browser.config.desired_capabilities)
        browser.element((AppiumBy.ID, textView)) \
            .should(have.text(FIRST_CHECK_EXPECT))
        browser.element((AppiumBy.ID, forwardButton)).click()
        add_video(browser)

    with step('Second screen checking'):
        browser.element((AppiumBy.ID, textView)) \
            .should(have.text(SECOND_CHECK_EXPECT))
        browser.element((AppiumBy.ID, forwardButton)).click()
        add_video(browser)

    with step('Third screen checking'):
        browser.element((AppiumBy.ID, textView)) \
            .should(have.exact_text(THIRD_CHECK_EXPECT))
        browser.element((AppiumBy.ID, forwardButton)).click()
        add_video(browser)

    with step('Fourth screen checking'):
        browser.element((AppiumBy.ID, textView)) \
            .should(have.text(FORTH_CHECK_EXPECT))
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_done_button")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_container")) \
            .should(be.visible)
        add_video(browser)

    browser.quit()