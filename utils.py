from undetected_chromedriver import Chrome, ChromeOptions


def create_driver() -> Chrome:
    """Run a browser driver

    Returns:
        Chrome: Browser driver interface
    """
    options = ChromeOptions()
    
    options.add_argument("--headless")  # Run Chrome in headless mode (without a GUI)
    
    chrome = Chrome(options=options)
    return chrome
