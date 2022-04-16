from flask import Flask, render_template
from selenium import webdriver

from selenium.webdriver.common.by import By
from flask import jsonify

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from flask_mysqldb import MySQL

from urllib.request import urlopen
  
# import json
import json
# store the URL in url as 
# parameter for urlopen


options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--remote-debugging-port=9222")


app = Flask(__name__, static_folder='static') 

app.config['MYSQL_HOST'] = 'database1.c8whdiwgu7ut.us-east-2.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'admin123456'
app.config['MYSQL_DB'] = 'weather'

mysql = MySQL(app)


@app.route("/")
def home():
    return render_template('index.html')



@app.route("/getdata")
def getdata():
        data = {
            "name" : "Barrie",
            "weather" : "Partly Cloudy",
            "temp" : "4 F",
            "humidity" : "40",
            "wind" : "4",
            "condition" : "Partly Cloud"
            }   
  
        return jsonify(data)



#1
@app.route("/ontario")
def ontario():
    
    browser = webdriver.Chrome(chrome_options=options)
    
    url = "http://3.21.113.181:5000/static/locations.json"
      
    # store the response of URL
    response = urlopen(url)
      
    # storing the JSON response 
    # from url in data
    data_json = json.loads(response.read())

    data_jsonX =data_json['Ontario']
    arr = [] 
    leng=len(data_jsonX) 
    j=0    
    try:
    
        for i in data_jsonX: 
            browser.get("https://www.google.com/search?q=weather+"+i)
            temperaturex = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_tm"))
            ).text
            precipitationx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_pp"))
            ).text
            humidityx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_hm"))
            ).text
            windx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_ws"))
            ).text
            aconditionx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_dc"))
            ).text
            dateday = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_dts"))
            ).text
            windx = windx.replace(' mph', '')
           
            locationx=i
            j=j+1
            arr.append(j)
            arr.append(leng)
            cur = mysql.connection.cursor()
            sql = "INSERT INTO scrapdataOntario (location,daydate,precipitation,temperature,humidity,wind,curStatus) VALUES(%s,%s,%s,%s,%s,%s,%s)"
            values = (locationx,dateday,precipitationx,temperaturex,humidityx,windx,aconditionx)
            cur.execute(sql,values)
            mysql.connection.commit()
            cur.close()
            
    finally:
           
        browser.stop_client()
        browser.close()
        browser.quit()           
        json_format = json.dumps(arr)
                    
        return (json_format)

#2
@app.route("/manitoba")
def manitoba():
    
    browser = webdriver.Chrome(chrome_options=options)
    
    url = "http://3.21.113.181:5000/static/locations.json"
      
    # store the response of URL
    response = urlopen(url)
      
    # storing the JSON response 
    # from url in data
    data_json = json.loads(response.read())

    data_jsonX =data_json['Manitoba']
    arr = [] 
    leng=len(data_jsonX) 
    j=0    
    try:
    
        for i in data_jsonX: 
            browser.get("https://www.google.com/search?q=weather+"+i)
            temperaturex = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_tm"))
            ).text
            precipitationx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_pp"))
            ).text
            humidityx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_hm"))
            ).text
            windx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_ws"))
            ).text
            aconditionx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_dc"))
            ).text
            dateday = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_dts"))
            ).text
            locationx=i
            j=j+1
            windx = windx.replace(' mph', '')
            arr.append(j)
            arr.append(leng)
            cur = mysql.connection.cursor()
            sql = "INSERT INTO scrapdataManitoba (location,daydate,precipitation,temperature,humidity,wind,curStatus) VALUES(%s,%s,%s,%s,%s,%s,%s)"
            values = (locationx,dateday,precipitationx,temperaturex,humidityx,windx,aconditionx)
            cur.execute(sql,values)
            mysql.connection.commit()
            cur.close()
            
    finally:
           
        browser.stop_client()
        browser.close()
        browser.quit()           
        json_format = json.dumps(arr)
                    
        return (json_format)
#3
@app.route("/labrador")
def labrador():
    
    browser = webdriver.Chrome(chrome_options=options)
    
    url = "http://3.21.113.181:5000/static/locations.json"
      
    # store the response of URL
    response = urlopen(url)
      
    # storing the JSON response 
    # from url in data
    data_json = json.loads(response.read())

    data_jsonX =data_json['Newfoundland And Labrador']
    arr = [] 
    leng=len(data_jsonX) 
    j=0    
    try:
    
        for i in data_jsonX: 
            browser.get("https://www.google.com/search?q=weather+"+i)
            temperaturex = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_tm"))
            ).text
            precipitationx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_pp"))
            ).text
            humidityx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_hm"))
            ).text
            windx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_ws"))
            ).text
            aconditionx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_dc"))
            ).text
            dateday = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_dts"))
            ).text
            windx = windx.replace(' mph', '')
            locationx=i
            j=j+1
            arr.append(j)
            arr.append(leng)
            cur = mysql.connection.cursor()
            sql = "INSERT INTO scrapdataLabrador (location,daydate,precipitation,temperature,humidity,wind,curStatus) VALUES(%s,%s,%s,%s,%s,%s,%s)"
            values = (locationx,dateday,precipitationx,temperaturex,humidityx,windx,aconditionx)
            cur.execute(sql,values)
            mysql.connection.commit()
            cur.close()
            
    finally:
           
        browser.stop_client()
        browser.close()
        browser.quit()           
        json_format = json.dumps(arr)
                    
        return (json_format)
#4        
@app.route("/quebec")
def quebec():
    
    browser = webdriver.Chrome(chrome_options=options)
    
    url = "http://3.21.113.181:5000/static/locations.json"
      
    # store the response of URL
    response = urlopen(url)
      
    # storing the JSON response 
    # from url in data
    data_json = json.loads(response.read())

    data_jsonX =data_json['Quebec']
    arr = [] 
    leng=len(data_jsonX) 
    j=0    
    try:
    
        for i in data_jsonX: 
            browser.get("https://www.google.com/search?q=weather+"+i)
            temperaturex = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_tm"))
            ).text
            precipitationx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_pp"))
            ).text
            humidityx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_hm"))
            ).text
            windx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_ws"))
            ).text
            aconditionx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_dc"))
            ).text
            dateday = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_dts"))
            ).text
            windx = windx.replace(' mph', '')
            locationx=i
            j=j+1
            arr.append(j)
            arr.append(leng)
            cur = mysql.connection.cursor()
            sql = "INSERT INTO scrapdataQuebec (location,daydate,precipitation,temperature,humidity,wind,curStatus) VALUES(%s,%s,%s,%s,%s,%s,%s)"
            values = (locationx,dateday,precipitationx,temperaturex,humidityx,windx,aconditionx)
            cur.execute(sql,values)
            mysql.connection.commit()
            cur.close()
            
    finally:
           
        browser.stop_client()
        browser.close()
        browser.quit()           
        json_format = json.dumps(arr)
                    
        return (json_format)        
#5       
@app.route("/island")
def island():
    
    browser = webdriver.Chrome(chrome_options=options)
    
    url = "http://3.21.113.181:5000/static/locations.json"
      
    # store the response of URL
    response = urlopen(url)
      
    # storing the JSON response 
    # from url in data
    data_json = json.loads(response.read())

    data_jsonX =data_json['Prince Edward Island']
    arr = [] 
    leng=len(data_jsonX) 
    j=0    
    try:
    
        for i in data_jsonX: 
            browser.get("https://www.google.com/search?q=weather+"+i)
            temperaturex = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_tm"))
            ).text
            precipitationx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_pp"))
            ).text
            humidityx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_hm"))
            ).text
            windx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_ws"))
            ).text
            aconditionx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_dc"))
            ).text
            dateday = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_dts"))
            ).text
            windx = windx.replace(' mph', '')
            locationx=i
            j=j+1
            arr.append(j)
            arr.append(leng)
            cur = mysql.connection.cursor()
            sql = "INSERT INTO scrapdataIsland (location,daydate,precipitation,temperature,humidity,wind,curStatus) VALUES(%s,%s,%s,%s,%s,%s,%s)"
            values = (locationx,dateday,precipitationx,temperaturex,humidityx,windx,aconditionx)
            cur.execute(sql,values)
            mysql.connection.commit()
            cur.close()
            
    finally:
           
        browser.stop_client()
        browser.close()
        browser.quit()           
        json_format = json.dumps(arr)
                    
        return (json_format) 
        
#6       
@app.route("/territories")
def territories():
    
    browser = webdriver.Chrome(chrome_options=options)
    
    url = "http://3.21.113.181:5000/static/locations.json"
      
    # store the response of URL
    response = urlopen(url)
      
    # storing the JSON response 
    # from url in data
    data_json = json.loads(response.read())

    data_jsonX =data_json['Northwest Territories']
    arr = [] 
    leng=len(data_jsonX) 
    j=0    
    try:
    
        for i in data_jsonX: 
            browser.get("https://www.google.com/search?q=weather+"+i)
            temperaturex = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_tm"))
            ).text
            precipitationx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_pp"))
            ).text
            humidityx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_hm"))
            ).text
            windx = windx.replace(' mph', '')
            windx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_ws"))
            ).text
            aconditionx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_dc"))
            ).text
            dateday = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_dts"))
            ).text
            locationx=i
            j=j+1
            arr.append(j)
            arr.append(leng)
            cur = mysql.connection.cursor()
            sql = "INSERT INTO scrapdataTerritories (location,daydate,precipitation,temperature,humidity,wind,curStatus) VALUES(%s,%s,%s,%s,%s,%s,%s)"
            values = (locationx,dateday,precipitationx,temperaturex,humidityx,windx,aconditionx)
            cur.execute(sql,values)
            mysql.connection.commit()
            cur.close()
            
    finally:
           
        browser.stop_client()
        browser.close()
        browser.quit()           
        json_format = json.dumps(arr)
                    
        return (json_format)           
#7
@app.route("/british")
def british():
    
    browser = webdriver.Chrome(chrome_options=options)
    
    url = "http://3.21.113.181:5000/static/locations.json"
      
    # store the response of URL
    response = urlopen(url)
      
    # storing the JSON response 
    # from url in data
    data_json = json.loads(response.read())

    data_jsonX =data_json['British Columbia']
    arr = [] 
    leng=len(data_jsonX) 
    j=0    
    try:
    
        for i in data_jsonX: 
            browser.get("https://www.google.com/search?q=weather+"+i)
            temperaturex = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_tm"))
            ).text
            precipitationx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_pp"))
            ).text
            humidityx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_hm"))
            ).text
            windx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_ws"))
            ).text
            aconditionx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_dc"))
            ).text
            dateday = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_dts"))
            ).text
            windx = windx.replace(' mph', '')
            locationx=i
            j=j+1
            arr.append(j)
            cur = mysql.connection.cursor()
            sql = "INSERT INTO scrapdataBritish (location,daydate,precipitation,temperature,humidity,wind,curStatus) VALUES(%s,%s,%s,%s,%s,%s,%s)"
            values = (locationx,dateday,precipitationx,temperaturex,humidityx,windx,aconditionx)
            cur.execute(sql,values)
            mysql.connection.commit()
            cur.close()
            
    finally:
           
        browser.stop_client()
        browser.close()
        browser.quit()           
        json_format = json.dumps(arr)
                    
        return (json_format)



#8
@app.route("/alberta")
def alberta():
    
    browser = webdriver.Chrome(chrome_options=options)
    
    url = "http://3.21.113.181:5000/static/locations.json"
      
    # store the response of URL
    response = urlopen(url)
      
    # storing the JSON response 
    # from url in data
    data_json = json.loads(response.read())

    data_jsonX =data_json['Alberta']
    arr = [] 
    leng=len(data_jsonX) 
    j=0    
    try:
    
        for i in data_jsonX: 
            browser.get("https://www.google.com/search?q=weather+"+i)
            temperaturex = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_tm"))
            ).text
            precipitationx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_pp"))
            ).text
            humidityx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_hm"))
            ).text
            windx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_ws"))
            ).text
            aconditionx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_dc"))
            ).text
            dateday = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_dts"))
            ).text
            windx = windx.replace(' mph', '')
            locationx=i
            j=j+1
            arr.append(j)
            cur = mysql.connection.cursor()
            sql = "INSERT INTO scrapdataAlberta (location,daydate,precipitation,temperature,humidity,wind,curStatus) VALUES(%s,%s,%s,%s,%s,%s,%s)"
            values = (locationx,dateday,precipitationx,temperaturex,humidityx,windx,aconditionx)
            cur.execute(sql,values)
            mysql.connection.commit()
            cur.close()
            
    finally:
           
        browser.stop_client()
        browser.close()
        browser.quit()           
        json_format = json.dumps(arr)
                    
        return (json_format)

#9
@app.route("/yukon")
def yukon():
    
    browser = webdriver.Chrome(chrome_options=options)
    
    url = "http://3.21.113.181:5000/static/locations.json"
      
    # store the response of URL
    response = urlopen(url)
      
    # storing the JSON response 
    # from url in data
    data_json = json.loads(response.read())

    data_jsonX =data_json['Yukon']
    arr = [] 
    leng=len(data_jsonX) 
    j=0    
    try:
    
        for i in data_jsonX: 
            browser.get("https://www.google.com/search?q=weather+"+i)
            temperaturex = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_tm"))
            ).text
            precipitationx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_pp"))
            ).text
            humidityx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_hm"))
            ).text
            windx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_ws"))
            ).text
            aconditionx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_dc"))
            ).text
            dateday = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_dts"))
            ).text
            windx = windx.replace(' mph', '')
            locationx=i
            j=j+1
            arr.append(j)
            cur = mysql.connection.cursor()
            sql = "INSERT INTO scrapdataYukon (location,daydate,precipitation,temperature,humidity,wind,curStatus) VALUES(%s,%s,%s,%s,%s,%s,%s)"
            values = (locationx,dateday,precipitationx,temperaturex,humidityx,windx,aconditionx)
            cur.execute(sql,values)
            mysql.connection.commit()
            cur.close()
            
    finally:
           
        browser.stop_client()
        browser.close()
        browser.quit()           
        json_format = json.dumps(arr)
                    
        return (json_format)

#10
@app.route("/scotia")
def scotia():
    
    browser = webdriver.Chrome(chrome_options=options)
    
    url = "http://3.21.113.181:5000/static/locations.json"
      
    # store the response of URL
    response = urlopen(url)
      
    # storing the JSON response 
    # from url in data
    data_json = json.loads(response.read())

    data_jsonX =data_json['Nova Scotia']
    arr = [] 
    leng=len(data_jsonX) 
    j=0    
    try:
    
        for i in data_jsonX: 
            browser.get("https://www.google.com/search?q=weather+"+i)
            temperaturex = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_tm"))
            ).text
            precipitationx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_pp"))
            ).text
            humidityx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_hm"))
            ).text
            windx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_ws"))
            ).text
            windx = windx.replace(' mph', '')
            aconditionx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_dc"))
            ).text
            dateday = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_dts"))
            ).text
            locationx=i
            j=j+1
            arr.append(j)
            cur = mysql.connection.cursor()
            sql = "INSERT INTO scrapdataScotia (location,daydate,precipitation,temperature,humidity,wind,curStatus) VALUES(%s,%s,%s,%s,%s,%s,%s)"
            values = (locationx,dateday,precipitationx,temperaturex,humidityx,windx,aconditionx)
            cur.execute(sql,values)
            mysql.connection.commit()
            cur.close()
            
    finally:
           
        browser.stop_client()
        browser.close()
        browser.quit()           
        json_format = json.dumps(arr)
                    
        return (json_format)

#11
@app.route("/brunswick")
def brunswick():
    
    browser = webdriver.Chrome(chrome_options=options)
    
    url = "http://3.21.113.181:5000/static/locations.json"
      
    # store the response of URL
    response = urlopen(url)
      
    # storing the JSON response 
    # from url in data
    data_json = json.loads(response.read())

    data_jsonX =data_json['New Brunswick']
    arr = [] 
    leng=len(data_jsonX) 
    j=0    
    try:
    
        for i in data_jsonX: 
            browser.get("https://www.google.com/search?q=weather+"+i)
            temperaturex = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_tm"))
            ).text
            precipitationx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_pp"))
            ).text
            humidityx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_hm"))
            ).text
            windx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_ws"))
            ).text
            windx = windx.replace(' mph', '')
            aconditionx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_dc"))
            ).text
            dateday = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_dts"))
            ).text
            locationx=i
            j=j+1
            arr.append(j)
            cur = mysql.connection.cursor()
            sql = "INSERT INTO scrapdataBrunswick (location,daydate,precipitation,temperature,humidity,wind,curStatus) VALUES(%s,%s,%s,%s,%s,%s,%s)"
            values = (locationx,dateday,precipitationx,temperaturex,humidityx,windx,aconditionx)
            cur.execute(sql,values)
            mysql.connection.commit()
            cur.close()
            
    finally:
           
        browser.stop_client()
        browser.close()
        browser.quit()           
        json_format = json.dumps(arr)
                    
        return (json_format)

#12
@app.route("/saskatchewan")
def saskatchewan():
    
    browser = webdriver.Chrome(chrome_options=options)
    
    url = "http://3.21.113.181:5000/static/locations.json"
      
    # store the response of URL
    response = urlopen(url)
      
    # storing the JSON response 
    # from url in data
    data_json = json.loads(response.read())

    data_jsonX =data_json['Saskatchewan']
    arr = [] 
    leng=len(data_jsonX) 
    j=0    
    try:
    
        for i in data_jsonX: 
            browser.get("https://www.google.com/search?q=weather+"+i)
            temperaturex = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_tm"))
            ).text
            precipitationx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_pp"))
            ).text
            humidityx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_hm"))
            ).text
            windx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_ws"))
            ).text
            windx = windx.replace(' mph', '')
            aconditionx = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_dc"))
            ).text
            dateday = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID,"wob_dts"))
            ).text
            locationx=i
            j=j+1
            arr.append(j)
            cur = mysql.connection.cursor()
            sql = "INSERT INTO scrapdataSaskatchewan (location,daydate,precipitation,temperature,humidity,wind,curStatus) VALUES(%s,%s,%s,%s,%s,%s,%s)"
            values = (locationx,dateday,precipitationx,temperaturex,humidityx,windx,aconditionx)
            cur.execute(sql,values)
            mysql.connection.commit()
            cur.close()
            
    finally:
           
        browser.stop_client()
        browser.close()
        browser.quit()           
        json_format = json.dumps(arr)
                    
        return (json_format)


@app.route("/checkchrome")
def checkchrome():
    
    browser = webdriver.Chrome(chrome_options=options)
    url = "http://3.21.113.181:5000/static/locations.json"
      
    # store the response of URL
    response = urlopen(url)
      
    # storing the JSON response 
    # from url in data
    data_json = json.loads(response.read())

    data_jsonX =data_json['Quebec']
    arr = [] 
    leng=len(data_jsonX) 
    j=0    
    
    try:
    
        for i in data_jsonX: 
            browser.get("https://www.google.com/search?q=weather+"+i)
            print(i)
            temperaturex=WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID,"wob_ws"))).text
           
            arr.append(temperaturex)
            arr.append(i)
           
          
    finally:
           
        browser.stop_client()
        browser.close()
        browser.quit()
        json_format = json.dumps(arr)
        return (json_format) 
                   
        






   
