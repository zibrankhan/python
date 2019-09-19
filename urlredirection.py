import mechanize

browser = mechanize.Browser()
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
browser.set_handle_refresh(False)

url_list = open("list.txt",'r').readlines()
url_active = open("active.txt",'w')
url_not_active = open("notActive.txt","w")
for i in url_list:
    br = browser.open(i)
    if br.code == 200:
        print i + "\t Active"
        url_active.write(str(i+"\t Active")+"\n")
        url_active.flush()
    else:
        print i + "\t Not Active"
        url_not_active.write(str(i+"\t Not Active")+"\n")
        url_not_active.flush()