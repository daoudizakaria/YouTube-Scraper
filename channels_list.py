from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import re

video_trend = []
channel_name = []
op = webdriver.ChromeOptions()
op.add_argument('headless')

driver = webdriver.Chrome(options=op)
driver.get("https://www.youtube.com/results?search_query=gaming&sp=CAMSAhAC")

i = 0
while i < 100 :
   youtube_channel = driver.find_elements(By.XPATH, '//yt-formatted-string[contains(@class, "style-scope ytd-channel-name")]')
   channel_URL = driver.find_elements(By.XPATH, '//a[contains(@href, "")]')
   driver.execute_script("var scrollingElement = (document.scrollingElement || document.body);scrollingElement.scrollTop = scrollingElement.scrollHeight;")
   i += 1

for url in channel_URL :
   print(url.text.strip())
   channel_name.append(url.text.strip())

fout = open("data.txt","w+")
i = 0
length = len(channel_name)
while i < int(length) :
 fout.write(channel_name[i])
 i += 1
fout.close()
lines = open("data.txt", 'r').readlines()
print(lines)
j = 0
channels_name=[]
first = "@"
last = "•"
while j < int(len(lines)):
 if lines[j][0] == "@":
  channel = lines[j]
  name =(channel.split(first))[1].split(last)[0]
  channels_name.append(name) 
 j += 1

df = pd.DataFrame({'Channel':channels_name})
df.to_csv('channels.csv', index=False, encoding='utf-8')
  
   
   
   
   
   
   

