import os
import urllib2
import pycld2
from bs4 import BeautifulSoup
import re
import tldextract
import bs4.element as e
import json
from string import lower
from urlparse import urljoin
from datetime import datetime
import mysql.connector
import time
#from categorization_factory import Category_Detector
#from saasnotsaas_predict_factory import SaasNotSaasDetector_Signleton

SUB_URL_ERROR = "Sub URL Error"
CONTENT_TYPE_ERROR = "Content type Error"
LANG_ERROR = "Langauage Error"
URL_READ_ERROR = "URL read Error"
RETRY_COUNT = 3

def update_db(appid,crawled):
    cnxn = mysql.connector.connect(user='appinfoadmin', password='appinfo@admin',host='172.16.96.171',database='security_index')
    cursor = cnxn.cursor()
    now = datetime.now()
    query = 'update newapp_data set crawled_updated_date = "'+now.strftime("%Y-%m-%d")+'",crawled = '+str(crawled)+' where id = '+str(appid)
    cursor.execute(query)
    cnxn.commit() 
    cnxn.close()     
    del cnxn
    
def page_text_return(page_text):
    page_text = re.sub("(https?:\/\/\S+)|(([a-zA-Z0-9])*?[@])|((http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-zA-Z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?)"," ",page_text)
    page_text = re.sub("[^a-zA-Z0-9]+"," ",page_text)
    page_text = re.sub("[a-z]*[0-9]+?[a-z0-9]*"," ",page_text)
    page_text = page_text.replace("\r+","\r")
    page_text = page_text.replace("\r"," ")
    page_text = page_text.replace("\n+","\n")
    page_text = page_text.replace("\n"," ")
    page_text = lower(re.sub(" +",' ',page_text))   
    return page_text

def get_url_from_href(url,webpage):
    if webpage == None:
        return False
    elif "contact-us" in webpage or "cookie" in webpage or "contact" in webpage or "contactus" in webpage or "condition" in webpage or "legal" in webpage or "partners" in webpage or "privacy" in webpage or "policy" in webpage or "terms" in webpage or "careers" in webpage or "sitemap" in webpage or ".ico" in webpage or ".png" in webpage or ".jpeg" in webpage or webpage.endswith(".dat") or webpage.endswith(".deb") or webpage.endswith(".tar") or webpage.endswith(".tgz") or webpage.endswith(".xz") or webpage.endswith(".mp3") or webpage.endswith(".mp4") or webpage.endswith(".gz") or webpage.endswith(".rpm") or webpage.endswith(".dmg") or webpage.endswith(".exe") or webpage.endswith(".msi") or webpage.endswith(".wmv") or webpage.endswith(".css") or webpage.endswith(".js") or webpage.endswith(">") or ".jpg" in webpage or  webpage.endswith(".pdf") or "javascript:" in webpage:
        return False
    elif "/css/" in webpage or "/js/" in webpage:
        return False
    elif "mailto" in webpage:
        return False
    else:
        page = urljoin(url,webpage) 
        url_domain = tldextract.extract(url)
        page_domain = tldextract.extract(page)
        if url_domain.domain == page_domain.domain:
            return page
    return False


def form_json_data(text,url,result):
    content = []
    soup = BeautifulSoup(text,"html.parser")
    links = []
    for tag in soup.findAll(href=True):
        links.append(tag['href'])
    for tag in soup.findAll(src=True):
        links.append(tag['src'])    
    for webpage in set(links):
        page = get_url_from_href(url, webpage)
        if page:
            if page not in result["a"]:
                result["a"].append(page)


    texts = soup.findAll(text=True)
    for i in texts:
        if len(i.strip()) < 1:
            continue
        if isinstance(i,e.PreformattedString):
            continue
        parent_object = i.parent.name
        parent_object_text = i.parent.text
        if parent_object in ['style', 'script', 'head', 'title', 'meta', '[document]','option','picture','code']:
            continue
        elif parent_object == "button":
            display_text = page_text_return(i).strip()
            if len(display_text) > 0 and display_text not in result["button"]:
                result["button"].append(display_text)
        else:
            p = page_text_return(i).strip()
            if len(p) > 2 :
                content.append(p)
    cralwed_page_data = " ".join(content)
    if cralwed_page_data not in result["content"].values():
        result["content"][url] = cralwed_page_data
    return result

def dump_data_json(name,data):
    if data:
        with open(name,"w") as f:
            json.dump(data,f,indent=4)


def read_url(url,error_log):
    i = RETRY_COUNT
    while(i>0):
        try:
            req = urllib2.Request(str(url), headers={'User-Agent' : "Magic Browser"})
            url_response = urllib2.urlopen(req,timeout = 10)
            if url_response.msg:
                return url_response.url,url_response
        except Exception as e:
            i = i -1
            time.sleep(1)
            continue
    else:
        error_log[url] = {URL_READ_ERROR : str(e)}
        return "",False  

def check_url_content_type(url,urlresponse,error_log):

    content_type = urlresponse.headers.getheader('content-type')
    if not content_type:
        error_log[url] = {CONTENT_TYPE_ERROR : "None"}
        return False    
    else:
        if "text/html" not in content_type:
            error_log[url] = {CONTENT_TYPE_ERROR :content_type}
            return False
        else:
            return True

def english_page(url,page_data,error_log):
    try:
        eng,_,lang = pycld2.detect(page_data)
    except Exception as e:
        error_log[url] = {LANG_ERROR : str(e)}
        return False
    
    if "ENGLISH" not in lang[0] or lang[0][2] < 80:
        error_log = {url : {LANG_ERROR :lang}}
        return False    
    else:
        return True
        
    
def getdata_from_url(name,url,check_category,saasnotpredict):
    
    file_path = os.path.dirname(os.path.realpath(__file__))
    now = datetime.now()
    dir_name = now.strftime("%Y-%m-%d")
    dir_name = file_path+"/"+dir_name
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)   
        
    if not url.startswith("http"):
        url = "http://"+url    
    
    error_log = {}
    redirect_url, url_response = read_url(url,error_log)
    
    if not url_response:
        dump_data_json(dir_name+"/"+name+".err", error_log)
        update_db(name,-1)
        return error_log
    
    if not check_url_content_type(url,url_response,error_log):
        dump_data_json(dir_name+"/"+name+".err", error_log)
        update_db(name,-1)
        return error_log
        
    page_data = url_response.read()
    
    if not english_page(url,page_data,error_log):
        dump_data_json(dir_name+"/"+name+".err", {url : LANG_ERROR})
        update_db(name,-1)
        return {url : LANG_ERROR}
    
    result = {"a":[],"content":{},"button":[]}
    form_json_data(page_data,url,result)
    
    #check_category = Category_Detector.get_categ_detector()
    check_category.classify_app_categ(name,url)

    visited_url = [url]
    for i in set(result["a"]):
        
        redirected_url, url_response = read_url(i,error_log)
        if redirected_url in visited_url:
            continue
        if not url_response:
            continue
        
        if not check_url_content_type(i,url_response,error_log):
            continue
            
        page_data = url_response.read()
        
        if not english_page(i,page_data,error_log):
            continue  
        
        form_json_data(page_data,i,result)
 
    with open(dir_name+"/"+name+".csv","w") as f:
        for i in result["content"].keys():
            f.write(i+"\n")
    
    app_crawled_data = " ".join(result["content"].values())
    dump_data_json(dir_name+"/"+name+".err", error_log)
    dump_data_json(dir_name+"/"+name+".json",result)
    f = open(dir_name+"/"+name+".txt","w")
    f.write(app_crawled_data)
    f.close() 
    update_db(name,1)
    saasnotpredict.predict_saasnotsaas(name,app_crawled_data)
#    saasnotsaas = SaasNotSaasDetector_Signleton.get_saasnotsaas_detector()
#    saasnotsaas.predict_saasnotsaas(name,app_crawled_data)
    return {url:True}

#print getdata_from_url("979","http://www.calibraleadership.com/")
#print getdata_from_url("5","https://www.1010data.com/")
#print getdata_from_url("8","http://www.measure360.co.uk/")