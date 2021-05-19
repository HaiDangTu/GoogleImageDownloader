from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.keys import Keys
import requests
import sys
if __name__ == "__main__":
    chrome_options = Options()
    querystring = sys.argv[1]
    frag = sys.argv[2]
    chrome_options.add_argument("--window-size=1500,700")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(querystring);
    images = driver.find_elements_by_css_selector("img.rg_i.Q4LuWd")
    
    target = 1000  #   <900
    import time
    while True:
      print(len(images))
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
      time.sleep(1)
      images = driver.find_elements_by_css_selector("img.rg_i.Q4LuWd")
      # mye4qd
      if len(images) > target:
        print("END")
        break
      end = driver.find_elements_by_css_selector("div.OuJzKb.Yu2Dnd")
      if len(end[0].text)>0:
        print("END")
        break
      try:
        more = driver.find_elements_by_css_selector("input.mye4qd")
        more[0].click()
      except Exception as e:
        #print(e)
        pass
        
    i = 0
    for el in images:
      el.click()
      p1 = el.find_element_by_xpath('..')
      p2 = p1.find_element_by_xpath('..')
      l=p2.get_attribute("href")
      cmd = "window.open('{}')".format(l)
      driver.execute_script(cmd)
      driver.switch_to.window(driver.window_handles[1])
      try:
        src = driver.find_elements_by_css_selector("img.n3VNCb")[0].get_attribute("src")
        response = requests.get(src)
        file = open("G:\\IMGS\\{}{}.png".format(i,frag), "wb")
        file.write(response.content)
        file.close()
        i += 1
      except Exception as e:
        pass
      driver.close()
      driver.switch_to.window(driver.window_handles[0])