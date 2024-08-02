from undetected_chromedriver import Chrome, ChromeOptions


def create_driver() -> Chrome:
    options = ChromeOptions()
    chrome = Chrome(options=options)
    return chrome
