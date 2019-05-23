# This code should get you some peanut butter data. I wrote it in a rush, so let me know if it breaks! 
# I'll be back on Monday. Good luck, and cheers from New Orleans!  - Louise

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# These packages will help us act like a human.
import time
import random

# This is for reading and writing CSV (comma-separated value) files.
import csv

def pause():
    """Call this function to pause for just a moment, like a human, instead of plunging forward."""
    time.sleep(abs(random.gauss(1.032028, 0.4983)))

def minipause():
    """Use this one for a short pause"""
    time.sleep(abs(random.gauss(.04398, 0.0231)))

def getpbut():
    """Gets our zipcodes from the file"""
    with open('pbs.txt') as f:
        pbut = [i.strip() for i in f.readlines()]
        
    return pbut

def visitwall():
    """Visits the Wall and returns a browser"""
    # chromedriver must be in the same folder as this file.
    browser = webdriver.Chrome('./chromedriver')

    # Now that we have a robo-browser, we can robo-visit a given link.
    browser.get('https://letterboxd.com/siracusa/films/')

    return browser

def getsearchbar():
    """Finds the search bar and returns it."""
    return browser.find_element_by_xpath('//*[@id="global-search-input"]')

def searchforpeanutbutter():
    # QUICK, ACT HUMAN
    pause()

    # Okay, coast is clear. Get the searchbar.
    searchbar = getsearchbar()

    # Set the zipcode,
    for x in pbut:
        print("Setting pbut to " + currentpbut)
        x = currentpbut
        #setzipcode(currentpbut)

    # Look for peanut butter
        searchbar.send_keys(x)
        
        searchbar.send_keys(Keys.ENTER)

        browser.find_element_by_xpath('//*[@id="searchProductResult"]/ul/li[1]/div/div[2]/div[5]/div/span[2]/a').click()

        Ingredients = browser.find_element_by_class_name('Ingredients')

        return "hydrogenated" in Ingredients.text


       # import pdb; pdb.set_trace()


        

def findOnPage():
    for x in range(2,15):
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")

        #Item 2 in list
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[2]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[2]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")


    #Item 3 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[3]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[3]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")

    #Item 4 in List
        item =  browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[4]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[4]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 5 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[5]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[5]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 6 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[6]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[6]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 7 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[7]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[7]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 8 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[8]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[8]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")    

    #Item 9 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[9]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[9]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")    
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[10]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")    
       
    #Item 10 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[11]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[11]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")    
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[12]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[12]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")    


        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[13]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[13]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 14 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[14]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[14]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 16 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[15]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[15]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 17 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[16]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[16]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 18 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[17]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[17]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 19 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[18]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[18]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 20 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[19]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[19]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 21 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[20]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[20]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 22 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[21]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[21]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 23 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[22]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[22]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 24 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[23]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[23]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 25 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[24]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[24]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 26 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[25]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[25]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 27 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[26]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[26]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 28 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[27]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[27]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 29 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[28]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[28]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 30 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[29]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[29]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 31 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[30]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[30]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 32 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[31]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[31]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 33 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[32]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[32]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 34 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[33]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[33]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 35 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[34]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[34]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 36 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[35]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[35]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 37 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[36]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[36]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 38 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[37]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[37]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 39 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[38]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[38]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 40 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[39]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[39]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 41 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[40]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[40]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 42 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[41]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[41]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 43 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[42]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[42]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 44 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[43]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[43]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 45 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[44]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[44]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 46 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[45]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[45]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 47 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[46]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[47]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 48 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[48]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[48]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 49 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[49]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[49]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 50 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[50]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[50]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 51 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[51]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[51]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 52 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[52]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[52]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 53 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[53]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[53]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 54 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[54]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[54]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 55 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[55]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[55]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 56 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[56]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[56]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")

        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[57]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[57]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")

    #Item 57 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[58]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[58]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 58 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[59]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[59]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 59 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[60]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[60]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 60 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[61]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[61]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 61 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[62]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[62]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 62 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[63]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[63]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 63 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[64]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[64]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 64 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[65]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[65]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 65 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[66]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[66]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 66 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[67]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[67]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 67 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[68]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[68]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 68 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[69]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[69]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 69 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[70]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[70]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 70 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[71]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[71]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
    #Item 70 in List
        item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[72]/div")
        # value = item.get_attribute("data-component-class")
        releaseYear = item.get_attribute("data-film-release-year")
        print(releaseYear)
        # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
        # print(rating)
        rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[72]").get_attribute("data-owner-rating")
        rating = int(rating)   
        rating/=2
        print(rating)
        movieName = item.get_attribute("data-film-name")
        print(movieName)
        pause()
        # Put that product in the CSV.
        with open('out.csv','a') as f:
            w = csv.writer(f)
            try:
                row = [movieName, releaseYear, rating]
                w.writerow(row)
            except:
                print("error")
        a = "https://letterboxd.com/siracusa/films/page/"
        b = str(x)
        c = a+b
        browser.get(c)
        pause()
        pause()

    browser.get("https://letterboxd.com/siracusa/films/page/15")

    item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div")
    # value = item.get_attribute("data-component-class")
    releaseYear = item.get_attribute("data-film-release-year")
    print(releaseYear)
    # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
    # print(rating)
    rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]").get_attribute("data-owner-rating")
    rating = int(rating)   
    rating/=2
    print(rating)
    movieName = item.get_attribute("data-film-name")
    print(movieName)
    pause()
    # Put that product in the CSV.
    with open('out.csv','a') as f:
        w = csv.writer(f)
        try:
            row = [movieName, releaseYear, rating]
            w.writerow(row)
        except:
            print("error")

    #Item 2 in list
    item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[2]/div")
    # value = item.get_attribute("data-component-class")
    releaseYear = item.get_attribute("data-film-release-year")
    print(releaseYear)
    # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
    # print(rating)
    rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[2]").get_attribute("data-owner-rating")
    rating = int(rating)   
    rating/=2
    print(rating)
    movieName = item.get_attribute("data-film-name")
    print(movieName)
    pause()
    # Put that product in the CSV.
    with open('out.csv','a') as f:
        w = csv.writer(f)
        try:
            row = [movieName, releaseYear, rating]
            w.writerow(row)
        except:
            print("error")


#Item 3 in List
    item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[3]/div")
    # value = item.get_attribute("data-component-class")
    releaseYear = item.get_attribute("data-film-release-year")
    print(releaseYear)
    # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
    # print(rating)
    rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[3]").get_attribute("data-owner-rating")
    rating = int(rating)   
    rating/=2
    print(rating)
    movieName = item.get_attribute("data-film-name")
    print(movieName)
    pause()
    # Put that product in the CSV.
    with open('out.csv','a') as f:
        w = csv.writer(f)
        try:
            row = [movieName, releaseYear, rating]
            w.writerow(row)
        except:
            print("error")

#Item 4 in List
    item =  browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[4]/div")
    # value = item.get_attribute("data-component-class")
    releaseYear = item.get_attribute("data-film-release-year")
    print(releaseYear)
    # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
    # print(rating)
    rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[4]").get_attribute("data-owner-rating")
    rating = int(rating)   
    rating/=2
    print(rating)
    movieName = item.get_attribute("data-film-name")
    print(movieName)
    pause()
    # Put that product in the CSV.
    with open('out.csv','a') as f:
        w = csv.writer(f)
        try:
            row = [movieName, releaseYear, rating]
            w.writerow(row)
        except:
            print("error")
#Item 5 in List
    item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[5]/div")
    # value = item.get_attribute("data-component-class")
    releaseYear = item.get_attribute("data-film-release-year")
    print(releaseYear)
    # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
    # print(rating)
    rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[5]").get_attribute("data-owner-rating")
    rating = int(rating)   
    rating/=2
    print(rating)
    movieName = item.get_attribute("data-film-name")
    print(movieName)
    pause()
    # Put that product in the CSV.
    with open('out.csv','a') as f:
        w = csv.writer(f)
        try:
            row = [movieName, releaseYear, rating]
            w.writerow(row)
        except:
            print("error")
#Item 6 in List
    item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[6]/div")
    # value = item.get_attribute("data-component-class")
    releaseYear = item.get_attribute("data-film-release-year")
    print(releaseYear)
    # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
    # print(rating)
    rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[6]").get_attribute("data-owner-rating")
    rating = int(rating)   
    rating/=2
    print(rating)
    movieName = item.get_attribute("data-film-name")
    print(movieName)
    pause()
    # Put that product in the CSV.
    with open('out.csv','a') as f:
        w = csv.writer(f)
        try:
            row = [movieName, releaseYear, rating]
            w.writerow(row)
        except:
            print("error")
    print("Complete!")

# #Item 71 in List
#     item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div")
#     # value = item.get_attribute("data-component-class")
#     releaseYear = item.get_attribute("data-film-release-year")
#     print(releaseYear)
#     # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
#     # print(rating)
#     rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]").get_attribute("data-owner-rating")
#     rating = int(rating)   
#     rating/=2
#     print(rating)
#     movieName = item.get_attribute("data-film-name")
#     print(movieName)
#     pause()
#     # Put that product in the CSV.
#     with open('out.csv','a') as f:
#         w = csv.writer(f)
#         try:
#             row = [movieName, releaseYear, rating]
#             w.writerow(row)
#         except:
#             print("error")
# #Item 72 in List
#     item = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div")
#     # value = item.get_attribute("data-component-class")
#     releaseYear = item.get_attribute("data-film-release-year")
#     print(releaseYear)
#     # rating = item.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]/div/div/a").get_attribute("data-original-title")
#     # print(rating)
#     rating = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul/li[1]").get_attribute("data-owner-rating")
#     rating = int(rating)   
#     rating/=2
#     print(rating)
#     movieName = item.get_attribute("data-film-name")
#     print(movieName)
#     pause()
#     # Put that product in the CSV.
#     with open('out.csv','a') as f:
#         w = csv.writer(f)
#         try:
#             row = [movieName, releaseYear, rating]
#             w.writerow(row)
#         except:
#             print("error")
    # test = browser.find_element_by_xpath("//*[@id='content']/div/div/section/ul").get_attribute("data-owner-rating")
    # data-original-title="Avengers: Endgame (2019) ★★★½"
    # print(value)
    # print(value)

        

# browser.find_element_by_xpath("//*[@id='header']/section/div/div/nav/ul/li[1]/a").click()
# pause()

# password.send_keys(Keys.ENTER)

# pause()
# pause()
# browser.get('https://letterboxd.com/siracusa/films')
browser = visitwall()

# pause()

# Set up our CSV file.
with open('out.csv','a') as f:
    w = csv.writer(f)
    w.writerow(['Movie', 'Release Year', "John Siracusa's Rating on Letterboxd"])

findOnPage()



import pandas as pd

# Set up our CSV file.
# with open('out.csv','a') as f:
#     w = csv.writer(f)
#     w.writerow(['brand', 'Hydroginated Oil'])

# # Get zipcodes
# pbut = getpbut()

# # Get the products in each zipcode
# for currentpbut in pbut:

#     # Visit the Wall
#     browser = visitwall()

#     # Search for peanut butter
#     searchforpeanutbutter()


#     # Get all products on page
#     for i in list(range(1, 2)):

#         hOil = searchforpeanutbutter

#         # Put that product in the CSV.
#         with open('out.csv','a') as f:
#             w = csv.writer(f)

#             try:
#                 row = [currentpbut, hOil]
#                 w.writerow(row)
#             except:
#                 import pdb; pdb.set_trace()

#     # Quit the browser.
#     browser.quit()

#     # Pretend to reflect on what you have done.
#     pause()
        

# (Assignment by Mustafa Hussain)
