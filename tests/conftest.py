import allure
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from selene import browser

from .. import config
from .. import attach


@pytest.fixture(scope='function')
def mobile_management_android():
    options = UiAutomator2Options().load_capabilities(
        {
            'platformVersion': config.settings.platformVersion_android,
            'deviceName': config.settings.deviceName_android,
            'app': config.settings.app,
            'bstack:options': {
                "projectName": "First Python project",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack first_test",
                "userName": config.settings.USER_NAME,
                "accessKey": config.settings.ACCESS_KEY,
            },
        }
    )

    browser.config.timeout = config.settings.timeout

    with allure.step("Open browserstack"):
        browser.config.driver = webdriver.Remote(
            'http://hub.browserstack.com/wd/hub',
            options=options)

    yield
    attach.add_screenshot(browser)
    attach.add_xml(browser)
    attach.add_video(browser)

    with allure.step("Tear down"):
        browser.quit()


@pytest.fixture(scope='function')
def mobile_management_ios():
    options = XCUITestOptions().load_capabilities(
        {
            'platformVersion': config.settings.platformVersion_ios,
            'deviceName': config.settings.deviceName_ios,
            'app': config.settings.app,
            'bstack:options': {
                "projectName": "First Python project",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack first_test",
                "userName": config.settings.USER_NAME,
                "accessKey": config.settings.ACCESS_KEY,
            },
        }
    )

    browser.config.timeout = config.settings.timeout

    with allure.step("Open browserstack"):
        browser.config.driver = webdriver.Remote(
            'http://hub.browserstack.com/wd/hub',
            options=options)

    yield
    attach.add_screenshot(browser)
    attach.add_xml(browser)
    attach.add_video(browser)

    with allure.step("Tear down"):
        browser.quit()
