import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

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

def getUserRatings(source, id):
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
        #result += str(id) + '\t' + str(name[0].string.encode('ascii', 'ignore')) + '\t' + str(landmarks[i]) + '\t' + str(ratings[i]) + '\n'
        result += str(id) + '|' +  str(landmarks[i]) + '|' + str(ratings[i]) + '\n'
    return result;

#File to read = str1, File to write to = str2
def dataScrapper(str1, str2):
    nextButton = '//button[text()="Next" and @class=""]'
    fr = open(str1, "r")        #pointer to file from which links are read
    fa = open(str2, "a+")       #pointer to file from which data is appended
    id = 0
    lines = fr.readlines()
    for r in lines:
        driver = webdriver.Firefox(executable_path='/home/sevenones/Mustafa/Python/geckodriver-v0.19.1-linux64/geckodriver')
        result = []
        current = ""
        prev = ""
        driver.get(r)
        while True:
            # do whatever you want
            try:
                current = getUserRatings(driver.page_source, id)
                if current != prev:
                    prev = current
                    result.append(current)
                driver.find_element_by_xpath(nextButton).click()
            except NoSuchElementException:
                break
        driver.close()
        for l in result:
            fa.write(l)
        id = id + 1
    fr.close()
    fa.close()

def main():
    str1 = 'user_links.txt' #name of the txt file with TripAdvisor links
    str2 = 'user_data.txt'  #output of the data
    dataScrapper(str1,str2)

if __name__ == '__main__':
    main()
