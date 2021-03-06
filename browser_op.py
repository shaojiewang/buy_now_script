from selenium import webdriver
import time
import os
import requests
import zipfile
import datetime
from selenium.webdriver.common.by import By

class browser_operations():
    def __init__(self, msEdge = True, chrome = False) -> None:
        self.browser = None
        if msEdge and chrome:
            chrome = False
        self.msEdge = msEdge
        self.chrome = chrome
        self.buy_limit_time_hour = 20
        self.buy_limit_time_minute = 0
        self.time_limit_str = ""

    def set_buy_limit_time(self, time_limit = "20:00"):
        assert isinstance(time_limit, str), "wrong time given. em: 20:00"
        time_limit_list = time_limit.split(":")
        assert time_limit_list[0].isnumeric() and time_limit_list[1].isnumeric(), "wrong hour or minute"
        hour = int(time_limit_list[0]) 
        minute = int(time_limit_list[1])
        assert hour > 0 and hour < 24
        assert minute >=0 and minute < 60

        self.buy_limit_time_hour = hour
        self.buy_limit_time_minute = minute

    def set_time_limit_str(self):
        limit_milisec = 500000
        limit_sec = 59
        carry_to_hour = 0
        if self.buy_limit_time_minute > 0:
            limit_minute = self.buy_limit_time_minute - 1
        else:
            limit_minute = 59
            carry_to_hour = 1

        if self.buy_limit_time_hour > 0:
            limit_hour = self.buy_limit_time_hour - carry_to_hour
        else:
            assert False, "do not support day expansion"

        now_t = datetime.datetime.now()
        now = now_t.strftime('%Y-%m-%d %H:%M:%S.%f')
        print(now)
        wait_t = now_t.replace(now_t.year, now_t.month, now_t.day, limit_hour, limit_minute, limit_sec, limit_milisec)
        self.time_limit_str = wait_t.strftime('%Y-%m-%d %H:%M:%S.%f')

    def get_time_limit_str(self):
        return self.time_limit_str
    
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
            # download
            zip_path = 'msedge.zip'
            if not os.path.exists(zip_path):
                edge_url='https://msedgedriver.azureedge.net/99.0.1150.55/edgedriver_win64.zip'
                driver_file=requests.get(edge_url)
                with open(zip_path, 'wb') as zip_file:
                    zip_file.write(driver_file.content)

            # unzip
            exe_path = 'msedgedriver.exe'
            if not os.path.exists(exe_path):
                zip_file = zipfile.ZipFile(zip_path)
                zip_list = zip_file.namelist() # ??????????????????????????????
                for f in zip_list:
                    if f.endswith('.exe'):
                        zip_file.extract(f, '') # ?????????????????????????????????
 
                zip_file.close() # ???????????????????????????????????????

            return

    def brower_login(self, path = None):
        path = "https://www.taobao.com"
        self.browser.get(path)
        time.sleep(3)
        # Taobao will check if this operation is driven by driver. 
        # If so, only scanning method can be used to login.
        if self.browser.find_element_by_link_text("???????????????"):
            self.browser.find_element_by_link_text("???????????????").click()
            print(f"?????????????????????")
            time.sleep(15)

    def select_all_cart(self, path = "https://cart.taobao.com/cart.htm"):
        self.browser.get(path)
        time.sleep(3)

        while True:
            try:
                if self.browser.find_element_by_id("J_SelectAll1"):
                    self.browser.find_element_by_id("J_SelectAll1").click()
                    break
            except:
                print(f"?????????????????????")

    def buy_in_time(self):
        flag = 1
        while True:
            #???????????????????????????,                      year month day
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            # ?????????????????????????????????????????????
            print(now)
            #??????????????????????????????????
            if now > self.get_time_limit_str():
                # ??????????????????
                while True:
                    if flag == 0:
                        break
                    try:
                        if self.browser.find_element_by_link_text("??? ???"):
                            print("here")
                            a = self.browser.find_element_by_link_text("??? ???")
                            print(a)
                            c = a.click()#webdriver.ActionChains(browser).move_to_element(a).click(a).perform()
                            for i in range(5):
                                c = a.click()
                                time.sleep(0.01)
                            print(c)
                            flag = 0
                            print(f"??????,??????????????????,????????????")
                            break
                    except:
                        pass
                    time.sleep(0.01)
                # ????????????????????????
                while True:
                    try:
                        if self.browser.find_element(By.XPATH, '//a[text()="????????????"]'):
                            self.browser.find_element(By.XPATH, '//a[text()="????????????"]').click()
                            print(f"??????????????????????????????")
                    except:
                        print(f"??????,???????????????????????????,???????????????")
                        #browser.quit()
                        break
                    time.sleep(0.01)


if __name__ == "__main__":
    b_op = browser_operations()
    b_op.download_driver()
    b_op.window_open()
    b_op.brower_login()
    time.sleep(1)
    b_op.set_buy_limit_time("20:00")
    b_op.set_time_limit_str()
    print(b_op.get_time_limit_str())
    b_op.select_all_cart()
    b_op.buy_in_time()
    b_op.window_quit()