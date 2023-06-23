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

description = []
all_des = []
all_names = []
all_emails = []
df = pd.read_csv('channels.csv')
matrix_data = df.to_numpy()
Len = len(matrix_data)
channel_url = [] 
XX = 1
for i in range(XX) :
   channel_name = matrix_data[i,0]
   print(channel_name)
   abt_url = f"https://www.youtube.com/@{matrix_data[i,0]}/about"
   driver = webdriver.Chrome()
   driver.get(abt_url)
   names = driver.find_elements(By.XPATH, '//yt-formatted-string[contains(@class, "style-scope ytd-channel-name")]')
   all_names.append(names)
   des = driver.find_elements(By.XPATH, '//yt-formatted-string[contains(@class, "style-scope ytd-channel-about-metadata-renderer")]')
   all_des.append(des[1])
#   emm = driver.find_elements(By.XPATH, '//a[contains(@id, "email")]')
#   print(emm)
#   print(emails)
   all_emails.append(emails)
   channel_url.append(f"https://www.youtube.com/@{matrix_data[i,0]}")
 
description = [] 
name_of_channel = [] 
email_channel = []
for desc in all_des :    
   description.append(desc.text.strip()) 

print(range(XX))   
for i in range(XX) :
   print(all_names[i][0].text.strip())
   name_of_channel.append(all_names[i][0].text.strip())   

#for i in range(XX) :
#   print("email =",all_emails[i][0].text.strip())
#   email_channel.append(all_emails[i][0].text.strip()) 
           
print(description)
print("="*50)   
print(channel_url)
print("="*50)
print(channel_name)
print("="*50)
print(len(channel_name),len(channel_url),len(description))   

df = pd.DataFrame({'Channel Name':name_of_channel,'URL':channel_url,'Description':description})
df.to_csv('youtube.csv', index=False, encoding='utf-8') 
