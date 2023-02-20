from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from fp.fp import FreeProxy


proxy = FreeProxy().get()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server={}'.format(proxy))
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)


# driver = webdriver.Chrome()
print(proxy)

driver.get('XXX')
time.sleep(5)
driver.implicitly_wait(50)
time.sleep(5)
driver.implicitly_wait(50)

click_script = "document.querySelector('#cmpwrapper').shadowRoot.querySelector('#cmpwelcomebtnyes > a').click()"
driver.execute_script(click_script)


button = driver.find_element(by=By.XPATH, value="//div[@id='OsobaOcena']//button[contains(@title, 'Popieram')]")
button.click()


time.sleep(5)
driver.implicitly_wait(50)
