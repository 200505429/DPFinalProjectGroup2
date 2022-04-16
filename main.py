from flask import Flask, render_template, request

from flask import jsonify


import requests
from bs4 import BeautifulSoup

from flask_mysqldb import MySQL

from urllib.request import urlopen
  
# import json
import json
# store the URL in url as 
# parameter for urlopen
import datetime
import random 


app = Flask(__name__, static_folder='static') 

app.config['MYSQL_HOST'] = 'database1.c8whdiwgu7ut.us-east-2.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'admin123456'
app.config['MYSQL_DB'] = 'weather'

mysql = MySQL(app)


@app.route("/")
def home():
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT *,'Ontario' as province FROM scrapdataOntario ORDER by scrapdataOntario.id DESC LIMIT 130""")
    sections = cur.fetchall()
    cur.close()
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT *,'Alberta' as province FROM scrapdataAlberta ORDER by scrapdataAlberta.id DESC LIMIT 130""")
    sections1 = cur.fetchall()
    cur.close()
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT *,'British Columbia' as province FROM scrapdataBritish ORDER by scrapdataBritish.id DESC LIMIT 130""")
    British = cur.fetchall()
    cur.close()
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT *,'Prince Edward Island' as province FROM scrapdataIsland ORDER by scrapdataIsland.id DESC LIMIT 130""")
    Island = cur.fetchall()
    cur.close()
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT *,'Manitoba' as province FROM scrapdataManitoba ORDER by scrapdataManitoba.id DESC LIMIT 130""")
    Manitoba = cur.fetchall()
    cur.close()
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT *,'Newfoundland And Labrador' as province FROM scrapdataLabrador ORDER by scrapdataLabrador.id DESC LIMIT 130""")
    Labrador = cur.fetchall()
    cur.close()
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT *,'New Brunswick' as province FROM scrapdataBrunswick ORDER by scrapdataBrunswick.id DESC LIMIT 130""")
    Brunswick = cur.fetchall()
    cur.close()
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT *,'Quebec' as province FROM scrapdataQuebec ORDER by scrapdataQuebec.id DESC LIMIT 130""")
    Quebec = cur.fetchall()
    cur.close()
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT *,'Saskatchewan' as province FROM scrapdataSaskatchewan ORDER by scrapdataSaskatchewan.id DESC LIMIT 130""")
    Saskatchewan = cur.fetchall()
    cur.close()
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT *,'Nova Scotia' as province FROM scrapdataScotia ORDER by scrapdataScotia.id DESC LIMIT 130""")
    Scotia = cur.fetchall()
    cur.close()
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT *,'Northwest Territories' as province FROM scrapdataTerritories ORDER by scrapdataTerritories.id DESC LIMIT 130""")
    Territories = cur.fetchall()
    cur.close()
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT *,'Yukon' as province FROM scrapdataYukon ORDER by scrapdataYukon.id DESC LIMIT 130""")
    Yukon = cur.fetchall()
    cur.close()
    
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT count(*) FROM scrapdataOntario""")
    sectionscount = cur.fetchone()
    cur.close()
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT count(*) FROM scrapdataAlberta""")
    sections1count = cur.fetchone()
    cur.close()
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT count(*) FROM scrapdataBritish""")
    Britishcount = cur.fetchone()
    cur.close()
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT count(*) FROM scrapdataIsland""")
    Islandcount = cur.fetchone()
    cur.close()
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT count(*) FROM scrapdataManitoba""")
    Manitobacount = cur.fetchone()
    cur.close()
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT count(*) FROM scrapdataLabrador""")
    Labradorcount = cur.fetchone()
    cur.close()
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT count(*) FROM scrapdataBrunswick""")
    Brunswickcount = cur.fetchone()
    cur.close()
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT count(*) FROM scrapdataQuebec""")
    Quebeccount = cur.fetchone()
    cur.close()
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT count(*) FROM scrapdataSaskatchewan""")
    Saskatchewancount = cur.fetchone()
    cur.close()
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT count(*) FROM scrapdataScotia""")
    Scotiacount = cur.fetchone()
    cur.close()
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT count(*) FROM scrapdataTerritories""")
    Territoriescount = cur.fetchone()
    cur.close()
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT count(*) FROM scrapdataYukon""")
    Yukoncount = cur.fetchone()
    cur.close()
    random_number = random.randint(1, 1000)
    return render_template('index.html',random_number=random_number,sections=sections,sections1=sections1,British=British,Island=Island,Manitoba=Manitoba,Labrador=Labrador,Brunswick=Brunswick,Quebec=Quebec,Saskatchewan=Saskatchewan,Scotia=Scotia,Territories=Territories,Yukon=Yukon,sectionscount=sectionscount,sections1count=sections1count,Britishcount=Britishcount,Islandcount=Islandcount,Manitobacount=Manitobacount,Labradorcount=Labradorcount,Brunswickcount=Brunswickcount,Quebeccount=Quebeccount,Saskatchewancount=Saskatchewancount,Scotiacount=Scotiacount,Territoriescount=Territoriescount,Yukoncount=Yukoncount)
    

@app.route("/getAllData")
def getAllData():
    allData=[]
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT *,'Ontario' as province FROM scrapdataOntario ORDER by scrapdataOntario.id DESC LIMIT 130""")
    sections = cur.fetchall()
    allData.append(sections)
    cur.close()
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT *,'Alberta' as province FROM scrapdataAlberta ORDER by scrapdataAlberta.id DESC LIMIT 130""")
    sections1 = cur.fetchall()
    allData.append(sections1)
    cur.close()
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT *,'British Columbia' as province FROM scrapdataBritish ORDER by scrapdataBritish.id DESC LIMIT 130""")
    British = cur.fetchall()
    allData.append(British)
    cur.close()
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT *,'Prince Edward Island' as province FROM scrapdataIsland ORDER by scrapdataIsland.id DESC LIMIT 130""")
    Island = cur.fetchall()
    allData.append(Island)
    cur.close()
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT *,'Manitoba' as province FROM scrapdataManitoba ORDER by scrapdataManitoba.id DESC LIMIT 130""")
    Manitoba = cur.fetchall()
    allData.append(Manitoba)
    cur.close()
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT *,'Newfoundland And Labrador' as province FROM scrapdataLabrador ORDER by scrapdataLabrador.id DESC LIMIT 130""")
    Labrador = cur.fetchall()
    allData.append(Labrador)
    cur.close()
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT *,'New Brunswick' as province FROM scrapdataBrunswick ORDER by scrapdataBrunswick.id DESC LIMIT 130""")
    Brunswick = cur.fetchall()
    allData.append(Brunswick)
    cur.close()
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT *,'Quebec' as province FROM scrapdataQuebec ORDER by scrapdataQuebec.id DESC LIMIT 130""")
    Quebec = cur.fetchall()
    allData.append(Quebec)
    cur.close()
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT *,'Saskatchewan' as province FROM scrapdataSaskatchewan ORDER by scrapdataSaskatchewan.id DESC LIMIT 130""")
    Saskatchewan = cur.fetchall()
    allData.append(Saskatchewan)
    cur.close()
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT *,'Nova Scotia' as province FROM scrapdataScotia ORDER by scrapdataScotia.id DESC LIMIT 130""")
    Scotia = cur.fetchall()
    allData.append(Scotia)
    cur.close()
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT *,'Northwest Territories' as province FROM scrapdataTerritories ORDER by scrapdataTerritories.id DESC LIMIT 130""")
    Territories = cur.fetchall()
   
    allData.append(Territories)
    cur.close()
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT *,'Yukon' as province FROM scrapdataYukon ORDER by scrapdataYukon.id DESC LIMIT 130""")
    Yukon = cur.fetchall()
    allData.append(Yukon)
    cur.close()
    return (jsonify(allData))

   
@app.route("/dashboard",methods=['GET', 'POST'])
def dashboard():
    city = request.args.get('city')
    province = request.args.get('province')
    if province=='null': 
        province='Ontario'
    if city=='null': 
        city='Barrie'
    province='scrapdata'+province
   
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT temperature,wind FROM """+province+""" where location=%s LIMIT 24""",(city,))
    result = cur.fetchall()
    cur.close()
    barrie=[]
    for itemx in result:
        resultx = {"wind":None,"temperature":None}
        
        resultx['wind'] = itemx[1].replace(' mph', '')
        resultx['temperature'] = itemx[0]
        barrie.append(resultx)
    return jsonify(barrie)



    
    

@app.route("/getdatawind")
def getdata():
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT id,wind FROM scrapdataOntario ORDER by scrapdataOntario.id DESC LIMIT 12""")
    result = cur.fetchall()
    cur.close()
    
    ontario = []
    alberta = []
    british = []
    manitoba= []
    quebec=[]
    yukon=[]
    labrador = []
    territories = []
    saskatchewan = []
    scotia = []
    island = []
    brunswick = []
    for itemx in result:
        resultx = {"wind":None}
        
        resultx['wind'] = itemx[1].replace(' mph', '')
        
        #date = itemx[4]
        #datem = datetime.datetime.strptime(date, "%A %I:%M %p")

       

        #resultx['time'] = datem.hour
        ontario.append(resultx)

    cur = mysql.connection.cursor() 
    cur.execute("""SELECT id,wind FROM scrapdataAlberta ORDER by scrapdataAlberta.id DESC LIMIT 12""")
    result = cur.fetchall()
    cur.close()

    for itemy in result:
        resultx = {"wind":None}
        
        resultx['wind'] = itemy[1].replace(' mph', '')
        
        alberta.append(resultx)
        
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT id,wind FROM scrapdataBritish ORDER by scrapdataBritish.id DESC LIMIT 12""")
    result = cur.fetchall()
    cur.close()

    for itemy in result:
    
        resultx = {"wind":None}
        
        resultx['wind'] = itemy[1].replace(' mph', '')
        
        british.append(resultx)
        
        
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT id,wind FROM scrapdataManitoba ORDER by scrapdataManitoba.id DESC LIMIT 12""")
    result = cur.fetchall()
    cur.close()

    for itemy in result:
    
        resultx = {"wind":None}
        
        resultx['wind'] = itemy[1].replace(' mph', '')
        
        manitoba.append(resultx)

    cur = mysql.connection.cursor() 
    cur.execute("""SELECT id,wind FROM scrapdataQuebec ORDER by scrapdataQuebec.id DESC LIMIT 12""")
    result = cur.fetchall()
    cur.close()

    for itemy in result:
    
        resultx = {"wind":None}
        
        resultx['wind'] = itemy[1].replace(' mph', '')
        
        quebec.append(resultx)
        
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT id,wind FROM scrapdataYukon ORDER by scrapdataYukon.id DESC LIMIT 12""")
    result = cur.fetchall()
    cur.close()

    for itemy in result:
    
        resultx = {"wind":None}
        
        resultx['wind'] = itemy[1].replace(' mph', '')
        
        yukon.append(resultx)
        
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT id,wind FROM scrapdataLabrador ORDER by scrapdataLabrador.id DESC LIMIT 12""")
    result = cur.fetchall()
    cur.close()

    for itemy in result:
    
        resultx = {"wind":None}
        
        resultx['wind'] = itemy[1].replace(' mph', '')
        
        labrador.append(resultx)
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT id,wind FROM scrapdataTerritories ORDER by scrapdataTerritories.id DESC LIMIT 12""")
    result = cur.fetchall()
    cur.close()

    for itemy in result:
    
        resultx = {"wind":None}
        
        resultx['wind'] = itemy[1].replace(' mph', '')
        
        territories.append(resultx)
        
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT id,wind FROM scrapdataSaskatchewan ORDER by scrapdataSaskatchewan.id DESC LIMIT 12""")
    result = cur.fetchall()
    cur.close()

    for itemy in result:
    
        resultx = {"wind":None}
        
        resultx['wind'] = itemy[1].replace(' mph', '')
        
        saskatchewan.append(resultx)
        
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT id,wind FROM scrapdataScotia ORDER by scrapdataScotia.id DESC LIMIT 12""")
    result = cur.fetchall()
    cur.close()

    for itemy in result:
    
        resultx = {"wind":None}
        
        resultx['wind'] = itemy[1].replace(' mph', '')
        
        scotia.append(resultx)
        
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT id,wind FROM scrapdataIsland ORDER by scrapdataIsland.id DESC LIMIT 12""")
    result = cur.fetchall()
    cur.close()

    for itemy in result:
    
        resultx = {"wind":None}
        
        resultx['wind'] = itemy[1].replace(' mph', '')
        
        island.append(resultx)
        
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT id,wind FROM scrapdataBrunswick ORDER by scrapdataBrunswick.id DESC LIMIT 12""")
    result = cur.fetchall()
    cur.close()

    for itemy in result:
    
        resultx = {"wind":None}
        
        resultx['wind'] = itemy[1].replace(' mph', '')
        
        brunswick.append(resultx)
  
    return jsonify(ontario,alberta,british,manitoba,quebec,yukon,labrador,territories,saskatchewan,scotia,island,brunswick)

#1
@app.route("/getWindByRange")
def getWindByRange():
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT * FROM scrapdataOntario where wind > 9 and wind < 30""")
    result = cur.fetchall()
    cur.close()
    
  
    return jsonify(result)

@app.route("/getItemById",methods=['GET', 'POST'])
def getItemById():
    
    idx = request.args.get('id')
   
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT * from scrapdataOntario where id=%s""",(idx,))
    result = cur.fetchone()
    cur.close()
    
    return jsonify(result)
    
    



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
                   
        


@app.after_request
def add_header(response):
    
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    response.headers['Cache-Control'] = 'public, max-age=0'

    return response



   
