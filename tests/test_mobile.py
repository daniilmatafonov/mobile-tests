import allure
import pytest
from allure_commons._allure import step, StepContext
from selene.support._logging import wait_with
from selene import have, be
from selene.support.shared import browser, config
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from dotenv import load_dotenv

from utilities.utils import add_video


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


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
def test_skip_screens():
    with step('First screen checking'):
        print(browser.config.desired_capabilities)
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")) \
            .should(have.text("The Free Encyclopedia"))
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).click()
        add_video(browser)

    with step('Second screen checking'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")) \
            .should(have.text("New ways to explore"))
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).click()
        add_video(browser)

    with step('Third screen checking'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")) \
            .should(have.exact_text("Reading lists with sync"))
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).click()
        add_video(browser)

    with step('Fourth screen checking'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")) \
            .should(have.text("Send anonymous data"))
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_done_button")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_container")) \
            .should(be.visible)
        add_video(browser)

    browser.quit()