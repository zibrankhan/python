from bs4 import BeautifulSoup
import mechanize
import html5lib

my_url = "https://www.flipkart.com/search?p%5B%5D=facets.brand%255B%255D%3DSamsung&sid=tyy%2F4io&sort=recency_desc&wid=1.productCard.PMU_V2_1"

browser = mechanize.Browser()
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]


soup = BeautifulSoup(browser.open(my_url).read(),"html.parser")
containers = soup.findAll("div", attrs={"class":"bhgxx2 col-12-12"})
soup = BeautifulSoup(containers ,"html.parser")
b = soup.findAll("p")






