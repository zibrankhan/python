from bs4 import BeautifulSoup
import mechanize
url = "https://www.pythonforbeginners.com/cheatsheet/python-mechanize-cheat-sheet"
browser = mechanize.Browser()
browser.addheaders = [("User-agent", "Mozilla/5.0")]
browser.set_handle_refresh(False)
soup = BeautifulSoup(browser.openurl)
