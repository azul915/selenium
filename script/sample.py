#!/usr/local/bin/python3
from selenium import webdriver
#from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
import datetime

def vote(browser: webdriver):

    # スクリーンショットのファイル名用に日付を取得
    dt = datetime.datetime.today()
    dtstr = dt.strftime("%Y%m%d%H%M%S")

    # ページアクセス
    browser.get('https://aoyama.missportal.jp/mr/06/')
    sleep(3)

    # 投票
    vote_button = browser.find_element_by_id('submit-btn')
    vote_button.click()
    sleep(3)

    # スクショ
    browser.save_screenshot('images/' + dtstr + '.png')

if __name__ == '__main__':
    try:

        # HEADLESSブラウザに接続
        browser = webdriver.Remote(
            command_executor='http://selenium-hub:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)

        # 投票
        vote(browser)

    finally:
        # 終了
        browser.close()
        browser.quit()

