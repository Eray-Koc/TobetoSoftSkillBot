from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.get("https://tobeto.com/giris")
driver.maximize_window()
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div/div/form/input[1]")))
driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div/div/form/input[1]").send_keys("") #MAILINIZI GIRIN
driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div/div/form/input[2]").send_keys("") # SIFRENIZI GIRIN
driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div/div/form/button").click()
WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.XPATH, "//*[@id='lessons-tab']")))
driver.find_element(By.XPATH, "//*[@id='lessons-tab']").click()
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='lessons-tab-pane']/div/div/div[2]")))
driver.find_element(By.XPATH, "//*[@id='lessons-tab-pane']/div/div/div[2]").click()
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='all-lessons-tab-pane']/div/div[1]/div/div[1]")))
driver.execute_script("window.scrollBy(0, 500)")
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='all-lessons-tab-pane']/div/div[12]/div/div[2]/a")))  #EGITIME GIT XPATH
driver.find_element(By.XPATH, "//*[@id='all-lessons-tab-pane']/div/div[12]/div/div[2]/a").click() #EGITIME GIT XPATH
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "//*[@id='my-player']/button")))

while True:
    sleep(2)
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='body']/div[4]/div/div[2]/div/div[2]/button")))
        driver.find_element(By.XPATH, "//*[@id='body']/div[4]/div/div[2]/div/div[2]/button").click()
    except:
        print("Yıldız gelmedi")
    driver.find_element(By.XPATH, "//*[@id='my-player']/button").click()
    sleep(0.4)
    try:
        deg = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='vjs-playback-rate-value-label-my-player_component_254']")))
        if deg:
            speedup = driver.find_element(By.XPATH, "//*[@id='vjs-playback-rate-value-label-my-player_component_254']").text
            print(speedup)
            while speedup != '2x':
                sleep(0.4)
                driver.find_element(By.XPATH, "//*[@id='my-player']/div[4]/div[9]/button").click()
                speedup = driver.find_element(By.XPATH, "//*[@id='vjs-playback-rate-value-label-my-player_component_254']").text
    except:
        print("Else çalıştı")
    WebDriverWait(driver, 870).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='my-player']/button")))
    sleep(10)




