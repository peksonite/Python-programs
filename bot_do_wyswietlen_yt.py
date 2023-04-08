# https://www.youtube.com/watch?v=Cz_RJtHnECs

from random import randint
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType

# set proxy

proxy_up_port = "IP:Port"

proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = proxy_ip_port

capabilities = webdriver.DesiredCapabilities.CHROME
proxy.add_to_capabilities(capabilities)

#call browser

driver = webdriver.Chrome(desired_capabilities=capabilities)

driver.get('https://youtube.com/watch?v=*********')
sleep(randint(1200, 1800))

#close browser
driver.quit