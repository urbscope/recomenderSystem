
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup

#Gets landmark name from Location tag. ({Location: Landmark_name})
def getLocationName(str):
    x = str.find(":")
    if x != -1:
         return str[x+2:].encode('ascii', 'ignore')
    return x

#Returns ratings from string "bubble_X"
def getRating(str):
    return str[7].encode('ascii', 'ignore')
    return 0

def scrapper(source, id):
    #page = urllib2.urlopen(url_link.strip())
    soup = BeautifulSoup(source, 'html.parser')                       #Parse HTML

    name = soup.find_all("span", class_="nameText")                 #Get name of the user

    locations = soup.find_all("div", class_="cs-review-location")   #Get the name of the landmarks

    landmarks = []
    for l in xrange(len(locations)):
        landmarks.append(getLocationName(locations[l].string))

    ratings = []
    ratingTag = soup.find_all("span", class_="ui_bubble_rating")    #Get the corresponding ratings
    for r in xrange(len(ratingTag)):
        ratings.append(getRating(ratingTag[r].attrs['class'][1]))

    result = ""
    for i in xrange(len(landmarks)):
        result += str(id) + '|' + str(name[0].string.encode('ascii', 'ignore')) + '|' + str(landmarks[i]) + '\t' + str(ratings[i]) + '\n'
        #result += str(id) + '\t' + '\t' + str(landmarks[i]) + '\t' + str(ratings[i]) + '\n'
    return result;

driver = webdriver.Firefox(executable_path='/home/sevenones/Mustafa/Python/geckodriver-v0.19.1-linux64/geckodriver')
driver.get("https://www.tripadvisor.com/members/sawbograham".strip())

total = []
current = ""
prev = ""
str2 = 'user_data.txt'  #output of the data
fa = open(str2, "a+")       #pointer to file from which data is appended
while True:
    # do whatever you want
    try:
        current = scrapper(driver.page_source, 0)
        if current != prev:
            prev = current
            total.append(current)
        driver.find_element_by_xpath(str1).click()
    except NoSuchElementException:
        break
driver.close()
for l in total:
    fa.write(l)
fa.close()
