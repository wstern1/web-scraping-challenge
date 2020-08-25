#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
import requests

def scrape():

# In[2]:


    url = 'https://mars.nasa.gov/news/'


# In[3]:


    response = requests.get(url)


# In[4]:


    soup = bs(response.text, 'html.parser')


# In[5]:


    print(soup.prettify())


# In[6]:


    soup.find_all('div', class_='content_title')


# In[7]:


    title = soup.find('div', class_='content_title')
    news_title = title.text
    news_title


# In[8]:


    p = soup.find('div', class_='rollover_description_inner')
    news_p = p.text
    news_p


# In[9]:


    from splinter import Browser
    


# In[10]:



    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    url_base = 'https://www.jpl.nasa.gov'

    response = requests.get(url)
    soup = bs(response.text, 'html.parser')

    result = soup.find('article', class_='carousel_item').attrs







    style_prop = str(result['style'])
    trim1 = style_prop.replace("background-image:", "")
    trim2 = trim1.replace(" url('", "")
    image = trim2.replace("');", "")
    image_url = url_base + image
    print(image_url)


# In[12]:


    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}

    browser = Browser('chrome', **executable_path, headless=False)
    featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA22374_hires.jpg'
    browser.visit(featured_image_url)


# In[26]:



    url = 'https://twitter.com/marswxreport?lang=en'


    browser.visit(url)

    html = browser.html
    soup = bs(html, 'html.parser')
    print(soup.prettify())


# In[31]:


    result = soup.find('span', class_="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0")

    mars_weather = result


# In[14]:


    url = "https://space-facts.com/mars/"
    table = pd.read_html(url)
    print(table)


# In[15]:


    df = table[0]
    df.columns = ["Parameters", "Values"]
    df.head()


# In[16]:


    html_table = df.to_html()
    html_table


# In[17]:


    html_table.replace('\n', '')


# In[18]:


    url_parent = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url_parent)

    html = browser.html
    soup = bs(html, 'html.parser')

    base_url = "https://astrogeology.usgs.gov"
    links = [base_url + item.find(class_="description").a["href"] for item in soup.find_all("div", class_="item")]


# In[20]:


    hemisphere_image_urls = []

    for url in links:
    
   
        browser.visit(url)
        html = browser.html
        soup = bs(html, 'html.parser')
    
    # Extract data
        title = soup.find("div", class_="content").find("h2", class_="title").text.replace(" Enhanced", "")
        img_url = base_url + soup.find("img", class_="wide-image")["src"]
    
    # Store in list
        hemisphere_image_urls.append({"title": title, "img_url": img_url})


# In[21]:


    hemisphere_image_urls


# In[29]:


    browser.quit()


# In[33]:


    mars = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_weather": mars_weather,
        "table_html": html_table,
        "hemisphere_image_urls": hemisphere_image_urls
        }


# In[35]:


    return mars







