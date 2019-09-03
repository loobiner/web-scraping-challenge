#importing dependencies
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser

def init_browser():
    executable_path = {"executable path": "C:/users/loobi/OneDrive/Documents/chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    executable_path = {"executable path": "C:/users/loobi/OneDrive/Documents/chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)
    
    url = "https://mars.nasa.gov/news/"
    
    #scraping up ingredients for soup
    r = requests.get(url)
                       
    #all html from NASA site
    soup = bs(r.content)
   
    #I used the inspect element option on chrome to find that each article on the Mars contains an a element and a div element
    #I populated a list called text_elements with all text contained in a or div tags using the whitelist. I then refined that list
    #into preferred_text to make the task more manageable. Then I got the title and paragraphs out of the list and assigned them
    #to variables
  
    whitelist = ['a', 'div']
    
    text_elements = [t for t in soup.find_all(text=True) if t.parent.name in whitelist]
    preferred_text = []
    for t in text_elements:
        if t != '\n':
            preferred_text.append(t)
    
    news_title = preferred_text[6]
    news_p = preferred_text[5]
    print(news_title)
    print(news_p)
 
    #image website, using browser to visit site and save html to a list
    images_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    Browser.visit(images_url)
    html = Browser.html
    images = []
    image_soup = bs(html, 'html.parser')
    
    #parsing html containing images and appending images to list
    for i in image_soup.find_all('div',class_='img'):
        images.append(i.find('img').get('src')) 
            
    #putting together the url to the featured image by splitting and concatenating strings.
    split_url = images_url.split('?')
    split_images = images[0].split('/')
   
    featured_image_url = (split_url[0] + split_images[2] + '/' + split_images[3] + '/' + split_images[4])
    featured_image_url
       
    mars_twitter_url = 'https://twitter.com/marswxreport?lang=en'
    
    #ingredients for the soup
    Browser.visit(mars_twitter_url)
    
    twitter_html = Browser.html
    # bon appetite
    twitter_soup = bs(twitter_html, 'html.parser')
    
    #found that tweets are in a p using inspector, got second tweet because of Mars solar conjunction, second tweet had weather data
    p = ['p']
    tweets = [tweet for tweet in twitter_soup.find_all(text=True) if tweet.parent.name in p]
    mars_weather = tweets[9]
    print(mars_weather)
        
    #url for table
    mars_facts_url = 'https://space-facts.com/mars'
    
    #making request
    mars_facts = requests.get(mars_facts_url)
    
    #delicious soup
    facts_soup = bs(mars_facts.content)
   
    #pulling table from soup
    table = facts_soup.find_all('table')
   
    #turning table to html string
    facts = pd.read_html(str(table))
        
    #hemisphere image urls\n",
    cerberus_url ='https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    schiaparelli_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    syrtis_major_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    valles_marineris_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    
    hemisphere_images_urls = [
                                {'title':'Cerberus Hemisphere', 'image_url':cerberus_url},
                                {'title':'Schiaparelli Hemisphere','image_url':schiaparelli_url},
                                {'title':'Syrtis Major Hemisphere','image_url':syrtis_major_url},
                                {'title':'Valles Marineris Hemisphere','image_url':valles_marineris_url}
                             ]
    
   
    
  