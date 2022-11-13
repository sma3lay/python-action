from selenium import webdriver
import time, random

links = ["https://shwepin.xyz/?p=221659",
         "https://shwepin.xyz"]
count =0;
while True:
    for link in links:
        driver = webdriver.Chrome()
        driver.get(link)
        print("Browser is reading...")
        height=driver.execute_script("return document.body.scrollHeight")
        Y=height/5
        for i in range(0,5):
            driver.execute_script("window.scrollTo(0,{})".format(Y))
            time.sleep(random.randint(5,15))
            Y+=Y
        count+=1
        print(count)
        driver.quit()
