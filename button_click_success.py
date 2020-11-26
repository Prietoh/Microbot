# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 10:01:10 2020

@author: OHyic
"""

#system libraries
import os
import random
import time

#selenium libraries
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException   
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.chrome.options import Options

#recaptcha libraries
import speech_recognition as sr
import ffmpy
import requests
import urllib
import pydub
from config import keys

def delay ():
    time.sleep(random.randint(1,3))
def delay2 ():
    time.sleep(random.randint(5,1))
def delay3 ():
    time.sleep(random.randint(2,1))
def delay4():
    time.sleep(2)
    

   #  driver.find_element_by_id('i0118').send_keys(k["password"]) #old format
# link = driver.find_element_by_link_text('Place order')
# link.click()
 #driver.get("https://www.microsoft.com/en-US/store/buy/checkout")
   # driver.find_element_by_id("button").click()
#try:
#sign in button click
#driver.find_element_by_id("""ember1053""").click()
  # driver = webdriver.Chrome(os.getcwd()+"\\webdriver\\chromedriver.exe") 
        #  first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "#ember1053")))
      #  print(first_result.get_attribute("textContent"))
        
    #frames=driver.find_elements_by_tag_name("ember1064")
    #driver.switch_to.frame(frames[0]);
    #driver.find_element_by_id('ember1064').click()
   # frames=driver.find_elements_by_tag_name("iframe")
    #driver.find_element_by_xpath('//*[@id="sign-in-form"]/button[1]').click() 
   # driver.switch_to.frame(frames[0]);
    
    #driver.find_element_by_class_name('loginfmt').send_keys(k["email"])   
   # driver.find_element_by_xpath('//*[@id="password"]').send_keys(k["password"]) 
    #driver.find_element_by_xpath('//*[@id="sign-in-form"]/button[1]').click() 
   # driver.get("http://facebook.com")
    #create chrome driver     
    
    #except:
   # print("[-] Please update the chromedriver.exe in the webdriver folder according to your chrome version:https://chromedriver.chromium.org/downloads")

def order(k):
    driver = webdriver.Chrome(os.getcwd()+"\\webdriver\\chromedriver.exe") 
   # driver.get("https://www.walmart.com/ip/Xbox-Series-X/443574645")
    driver.get("https://login.live.com/login.srf?av=5139875.1&claims=%7B%22compact%22%3A%7B%22name%22%3A%7B%22essential%22%3Atrue%7D%7D%7D&id=74335&lc=1033&rpsnv=13&rver=7.3.6963.0&wa=wsignin1.0&wp=SAPI&wreply=https%3A%2F%2Fwww.microsoft.com%2Fen-US%2Fstore%2Fbuy%3Froute%3Dcheckout%26cartType%3Dconsumer%26orderIds%3Dp%3A2d789eb4-1663-4657-b9ca-0f9893514406%3A3929123530")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#i0116'))).send_keys(k["email"])
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#idSIButton9'))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#i0118'))).send_keys(k["password"])
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#idSIButton9'))).click()
    driver.get("https://www.microsoft.com/en-US/store/buy/checkout")
    driver.execute_script("setInterval(function(){document.getElementsByClassName('btn theme-default btn-primary cli-purchase ember-view')[0].click();}, 5000);")
    driver.execute_script("setInterval(function(){document.getElementsByClassName('btn theme-default btn-primary cli-purchase ember-view')[0].click();}, 5000);")
    driver.execute_script("setInterval(function(){document.getElementsByClassName('btn theme-default btn-primary cli-purchase ember-view')[0].click();}, 5000);").click()
    delay3()
    if  driver.find_element_by_class_name("l-col-16-24 cli-alert-message"):
        driver.execute_script("setInterval(function(){document.getElementsByCSS_SELECTOR('#ember1194')[0].click();}, 5000);")
        delay3()
    if  driver.find_element_by_id('i0116'):
        driver.find_element_by_id('i0116').send_keys(k["email"])
    if  driver.find_element_by_id('i0118'):
        driver.find_element_by_id('i0118').send_keys(k["password"])
        delay()
        driver.find_element_by_id('idSIButton9').click()
    delay4()
    if  WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#i0116'))).send_keys(k["email"]):
        WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#idSIButton9'))).click()
        WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#i0118'))).send_keys(k["password"])
        WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#idSIButton9'))).click()            
           

if __name__ == '__main__': 
    order(keys)
        
driver = webdriver.Chrome(os.getcwd()+"\\webdriver\\chromedriver.exe") 
if  WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#recaptcha-checkbox-border'))):
        
    #switch to recaptcha frame
    driver = webdriver.Chrome(os.getcwd()+"\\webdriver\\chromedriver.exe") 
    frames=driver.find_elements_by_tag_name("iframe")
    driver.switch_to.frame(frames[0]);
    delay()
    
    #click on checkbox to activate recaptcha
    driver.find_element_by_class_name("recaptcha-checkbox-border").click()
    
    #switch to recaptcha audio control frame
    driver.switch_to.default_content()
    frames=driver.find_element_by_xpath("/html/body/div[2]/div[4]").find_elements_by_tag_name("iframe")
    driver.switch_to.frame(frames[0])
    delay()
    
    #click on audio challenge
    driver.find_element_by_id("recaptcha-audio-button").click()
    
    #switch to recaptcha audio challenge frame
    driver.switch_to.default_content()
    frames= driver.find_elements_by_tag_name("iframe")
    driver.switch_to.frame(frames[-1])
    delay()
    
    #click on the play button
    driver.find_element_by_xpath("/html/body/div/div/div[3]/div/button").click()
    #get the mp3 audio file
    src = driver.find_element_by_id("audio-source").get_attribute("src")
    print("[INFO] Audio src: %s"%src)
    #download the mp3 audio file from the source
    urllib.request.urlretrieve(src, os.getcwd()+"\\sample.mp3")
    sound = pydub.AudioSegment.from_mp3(os.getcwd()+"\\sample.mp3")
    sound.export(os.getcwd()+"\\sample.wav", format="wav")
    sample_audio = sr.AudioFile(os.getcwd()+"\\sample.wav")
    r= sr.Recognizer()
    
    with sample_audio as source:
        audio = r.record(source)
    
    #translate audio to text with google voice recognition
    key=r.recognize_google(audio)
    print("[INFO] Recaptcha Passcode: %s"%key)
    
    #key in results and submit
    driver.find_element_by_id("audio-response").send_keys(key.lower())
    driver.find_element_by_id("audio-response").send_keys(Keys.ENTER)
    driver.switch_to.default_content()
    delay()
    driver.find_element_by_id("recaptcha-demo-submit").click()
    delay()