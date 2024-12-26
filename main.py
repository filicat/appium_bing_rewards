import time
import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from faker import Faker
import easygui

if __name__ == '__main__':
    fake = Faker('zh_CN')
    options = UiAutomator2Options().load_capabilities({
        'platformName': 'Android',
        'automationName': 'uiautomator2',
        'deviceName': 'Android',
        'appPackage': 'com.microsoft.emmx',
        'appActivity': 'com.microsoft.ruby.Main',
        'noReset': True,
        'dontStopAppOnReset': True  # 保持应用运行，不重启
    })
    appium_server_url = 'http://localhost:4723'
    driver = webdriver.Remote(appium_server_url, options=options)
    try:
        for i in range(20):
            input_elem = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="sb_form_q"]')
            input_elem.send_keys(fake.company() + ' ' + fake.name())
            submit_btn = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="sb_form_go"]')
            submit_btn.click()
            time.sleep(10)
    finally:
        easygui.msgbox("搜索完成", title="必应搜索_移动")
        driver.quit()
