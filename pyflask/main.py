from flask import Flask, render_template

from flask import jsonify


import requests
from bs4 import BeautifulSoup

from flask_mysqldb import MySQL

from urllib.request import urlopen
  
# import json
import json
# store the URL in url as 
# parameter for urlopen


app = Flask(__name__, static_folder='static') 

app.config['MYSQL_HOST'] = 'database1.c8whdiwgu7ut.us-east-2.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'admin123456'
app.config['MYSQL_DB'] = 'weather'

mysql = MySQL(app)


@app.route("/")
def home():
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT *,'Ontario' as province FROM scrapdataOntario where scrapdataOntario.temperature>'59' and scrapdataOntario.wind>'7' ORDER by scrapdataOntario.id DESC LIMIT 12""")
    user = cur.fetchone()
    print(user)
    return render_template('index.html', user = user)



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
            windx = windx.replace('mph', '')
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
                   
        






   
