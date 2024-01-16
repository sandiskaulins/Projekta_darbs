#Import libraries for the project
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

component_price_1a = []
component_names_1a = []
big_list_1a = []

component_price_220 = []
component_names_220 = []
big_list_220 = []

component_price_dateks = []
component_names_dateks = []
big_list_dateks = []

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)
driver.maximize_window()

url = "https://www.1a.lv"
driver.get(url)
time.sleep(2)

find = driver.find_element(By.CLASS_NAME, "c-button-inverse")
find.click()

def get_component_price_1a(name):

    find = driver.find_element(By.ID, "q")
    find.send_keys(name)
    time.sleep(1)

    find = driver.find_element(By.CLASS_NAME, "sn-suggest-doc-info")
    find.click()

    find = driver.find_element(By.TAG_NAME, "h1")
    component_name = find.text

    find = driver.find_element(By.CLASS_NAME, "price ")
    find1 = find.find_element(By.TAG_NAME, "span")
    component_value = find1.text
    if(name=="1116740"):
        component_names_1a.append("2X " + component_name)
        component_price_1a.append(2 * float(component_value.replace(",", ".")))
    else:
        component_names_1a.append(component_name)
        component_price_1a.append(float(component_value.replace(",", ".")))


get_component_price_1a("1210128")
get_component_price_1a("1367176")
get_component_price_1a("Videokarte Gigabyte Radeon RX 6600 EAGLE GV-R66EAGLE-8GD, 8 GB, GDDR6")
get_component_price_1a("Cietais disks (SSD) Kingstone NV2, M.2, 1 TB")
get_component_price_1a("1116740")
get_component_price_1a("897433")
get_component_price_1a("1399810")
get_component_price_1a("1258998")

time.sleep(1)

print(component_names_1a)
print(component_price_1a)

big_list_1a = list(zip(component_names_1a , component_price_1a))

url="https://220.lv"
driver.get(url)
time.sleep(2)

find = driver.find_element(By.CLASS_NAME, "c-link")
find.click()
time.sleep(1)
def get_component_price_220(name):

    find = driver.find_element(By.ID, "searchInput")
    find.clear()
    find.send_keys(name)
    time.sleep(1)

    find = driver.find_element(By.CLASS_NAME, "c-icon--search")
    find.click()

    find = driver.find_element(By.XPATH, "/html/body/div[9]/div/div[1]/section/div/div/div[2]/section/div[3]/div/div/div/div/div[3]/a/img")
    find.click()

    find = driver.find_element(By.XPATH, "/html/body/div[9]/div/div[2]/section/div/div/div[2]/h1")
    component_name = find.text
    
    find = driver.find_element(By.XPATH, "/html/body/div[9]/div/div[2]/section/div/div/div[3]/div[1]/div[1]")
    find1 = find.find_element(By.TAG_NAME, "div")
    component_value = find1.text
    component_value = component_value.replace("€","").replace("\n",".")
    component_value = component_value[:-1]


    component_names_220.append(component_name)
    component_price_220.append(float(component_value))


get_component_price_220("16534896")
get_component_price_220("22494327")
get_component_price_220("22803606")
get_component_price_220("6857420")
get_component_price_220("15088197")
get_component_price_220("8689198")
get_component_price_220("15303444")
get_component_price_220("26475011")

time.sleep(1)

print(component_names_220)
print(component_price_220)

big_list_220 = list(zip(component_names_220 , component_price_220))

url="https://www.dateks.lv/"
driver.get(url)
time.sleep(2)

find = driver.find_element(By.CLASS_NAME, "button")
find.click()
time.sleep(1)
def get_component_price_dateks(name):

    find = driver.find_element(By.XPATH, "/html/body/header[2]/div[6]/div[1]/form/input")
    find.clear()
    find.send_keys(name)
    time.sleep(1)

    find = driver.find_element(By.XPATH, "/html/body/header[2]/div[6]/div[1]/form/button")
    find.click()
    time.sleep(1)

    find = driver.find_element(By.XPATH, "/html/body/main/div[2]/div[1]/div/div/div[1]/a/div[2]")
    component_name = find.text
    
    find = driver.find_element(By.CLASS_NAME, "price")
    component_value = find.text

    if(name=="822171"):
        component_names_dateks.append("2X " + component_name)
        component_price_dateks.append(2 * float(component_value.replace(",",".").replace("€","")))
    else:
        component_names_dateks.append(component_name)
        component_price_dateks.append(float(component_value.replace(",",".").replace("€","")))


get_component_price_dateks("893889")
get_component_price_dateks("960553")
get_component_price_dateks("768341")
get_component_price_dateks("890433")
get_component_price_dateks("822171")
get_component_price_dateks("650781")
get_component_price_dateks("974991")
get_component_price_dateks("957236")

time.sleep(1)

print(component_names_dateks)
print(component_price_dateks)

big_list_dateks = list(zip(component_names_dateks , component_price_dateks))

pc_price_1a = sum(component_price_1a)
pc_price_220 = sum(component_price_220)
pc_price_dateks = sum(component_price_dateks)

cheapestPc = 0
store_name = ''

if(pc_price_1a < pc_price_220 and pc_price_dateks):
    cheapestPc = pc_price_1a
    store_name = '1A.lv'
elif(pc_price_220 < pc_price_1a and pc_price_dateks):
    cheapestPc = pc_price_220
    store_name = '220.lv'
else:
    cheapestPc = pc_price_dateks
    store_name = 'dateks.lv'

i=0
cheapest_component = 0
cheapest_component_name = ''
cheapest_component_store_name = ''
cheapest_component_list = []
cheapest_component_list_price = []
cheapest_component_name_list = []
cheapest_component_store_name_list = []

for line in big_list_1a:
    item = component_price_1a[i]
    item2 = component_price_220[i]
    item3 = component_price_dateks[i]
    if(item < item2 and item3):
        cheapest_component_name = component_names_1a[i]
        cheapest_component_store_name = '1A.lv'
        cheapest_component = component_price_1a[i]
    elif(item2 < item and item3):
        cheapest_component_name = component_names_220[i]
        cheapest_component_store_name = '220.lv'
        cheapest_component = component_price_220[i]
    elif(item == item2 or item3):
        cheapest_component_name = component_names_1a[i]
        cheapest_component_store_name = '1A'
        cheapest_component = component_price_1a[i]
    else:
        cheapest_component_name = component_names_dateks[i]
        cheapest_component_store_name = 'dateks.lv'
        cheapest_component = component_price_dateks[i]
    i+=1
    cheapest_component_list_price.append(cheapest_component)
    cheapest_component_name_list.append(cheapest_component_name)
    cheapest_component_store_name_list.append(cheapest_component_store_name)

cheapest_component_list = list(zip(cheapest_component_name_list, cheapest_component_list_price, cheapest_component_store_name_list))


import smtplib 
import email
from email.message import EmailMessage
from user_login import *

# SMTP Server and port no for GMAIL.com
gmail_server= "smtp.gmail.com"
gmail_port= 587


# Starting connection
my_server = smtplib.SMTP(gmail_server, gmail_port)
my_server.ehlo()
my_server.starttls()
    
# Login with your email and password
my_server.login(my_email, password_key)
msg = EmailMessage()
message_content = (
    'Viss izdēvīgāk ir pc ir salikt ' + store_name + ' un kopā tas izmaksās ' + str(cheapestPc) + ' eiro' + '\n'
    'Viss izdevīgākās cenas uz komponentēm ir: \n'
)

for component in cheapest_component_list:
    message_content += (
        'Komponentes nosaukums: ' + component[0] + ' kas maksā ' + str(component[1]) + ' eiro un to var iegādāties ' + component[2] + '\n'
    )

message_content += 'Ja pērk atsevišķos veikalos, tad cena kopā ir ' + str(round(sum(cheapest_component_list_price),2))+ ' eiro'
msg.set_content(message_content)

msg['Subject'] = 'Datora komponenšu cenas'
msg['From'] = "" #pievienojiet savu ēpastu
msg['To'] = "" #pievienojiet savu ēpastu

my_server.send_message(msg)
print('Mail Sent')


