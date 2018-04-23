import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

#writes the latitudes and longitudes in cordinates.txt file
def getLatLong(query,driver, fw):
    #print driver.find_element_by_xpath('//input[@id="lat"]').get_attribute("value").encode("utf-8")
    soup = BeautifulSoup(driver, 'html.parser')
    cordinates = soup.find('span', {'id': 'latlngspan'}).string.split(",")
    latitude = cordinates[0][1:].encode("ascii", 'ignore').strip()
    longitude = cordinates[1][:-2].encode('ascii', 'ignore').strip()
    fw.write(query+"|"+latitude + "|" + longitude + "\n")

#this function is called when longitudes and latitudes cant be found. It simply writes 0,0
def insertNothing(query, fw):
    fw.write(query+"|360|360\n")

def getCordinates(filename, cordinateFile):
    fr = open(filename, "r")
    fw = open(cordinateFile, "a+")
    places = fr.readlines()
    findButton = '//button[text()="Find" and @class="button" and @title="Find Lat & Long"]'
    driver = webdriver.Firefox(executable_path='/home/sevenones/Mustafa/Python/geckodriver-v0.19.1-linux64/geckodriver')
    driver.get("https://www.latlong.net/")
    badPlaces = 0
    i = 0
    for place in places:
        query = place.split("|")[1]
        i = i + 1
        try:
            element = driver.find_element_by_xpath('//input[@placeholder="Type a place name"]')
            element.send_keys(query)
            driver.find_element_by_xpath(findButton).click()
            #time.sleep(1)
            try:
                WebDriverWait(driver, 3).until(EC.alert_is_present(),"")
                alert = driver.switch_to.alert
                alert.accept()
                badPlaces = badPlaces + 1
                insertNothing(query, fw)
                element.clear()
                print i
            except TimeoutException:
                getLatLong(query,driver.page_source, fw)
                element.clear()
                print i
                pass
        except NoSuchElementException:
            print "Error"
    driver.close()
    fw.write("Bad Places: " + str(badPlaces))
    print "Bad Places: " + str(badPlaces)
    fr.close()
    fw.close()

def main():
    filename = "user_data3.txt"
    cordinateFile = "cordinates3.txt"
    getCordinates(filename, cordinateFile)

if __name__ == '__main__':
    main()
