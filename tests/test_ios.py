import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


@allure.title('Test search on ios')
def test_search_ios(mobile_management_ios):

    with allure.step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Button")).click()

    with allure.step('Input text'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Input")).send_keys('QaGuru' + '\n')

    with allure.step('Output text'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Output")).should(have.text("QaGuru"))