from selenium import webdriver
import time
import os

class browser_operations():
    def __init__(self, msEdge = True, chrome = False) -> None:
        self.browser = None
        if msEdge and chrome:
            chrome = False
        self.msEdge = msEdge
        self.chrome = chrome
    
    def window_open(self):
        if self.msEdge:
            self.browser = webdriver.Edge(os.getcwd() + "\\msedgedriver.exe")
        elif self.chrome:
            self.browser = webdriver.Chrome()
        self.browser.maximize_window()

    def window_quit(self):
        self.browser.quit()

    def download_driver(self):
        if self.chrome:
            return
        if self.msEdge:
            return

    def brower_login(self, path = None):
        path = "https://www.taobao.com"
        self.browser.get(path)
        time.sleep(3)
        # Taobao will check if this operation is driven by driver. 
        # If so, only scanning method can be used to login.
        if self.browser.find_element_by_link_text("亲，请登录"):
            self.browser.find_element_by_link_text("亲，请登录").click()
            print(f"请尽快扫码登录")
            time.sleep(100)


if __name__ == "__main__":
    b_op = browser_operations()
    b_op.window_open()
    b_op.brower_login()
    time.sleep(1)
    b_op.window_quit()