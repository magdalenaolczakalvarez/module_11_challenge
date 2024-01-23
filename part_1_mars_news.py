#!/usr/bin/env python
# coding: utf-8

# # Module 11 Challenge
# ## Deliverable 1: Scrape Titles and Preview Text from Mars News

# In[10]:


from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://selenium.dev")

#driver.quit()


# In[11]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup


# In[12]:


browser = Browser('chrome')


# ### Step 1: Visit the Website
# 
# 1. Use automated browsing to visit the [Mars news site](https://static.bc-edx.com/data/web/mars_news/index.html). Inspect the page to identify which elements to scrape.
# 
#       > **Hint** To identify which elements to scrape, you might want to inspect the page by using Chrome DevTools.

# In[12]:


# Visit the Mars news site
url = 'https://static.bc-edx.com/data/web/mars_news/index.html'
browser.visit(url)


# ### Step 2: Scrape the Website
# 
# Create a Beautiful Soup object and use it to extract text elements from the website.

# In[13]:


# Create a Beautiful Soup object
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
soup


# In[14]:


# Extract all the text elements
all_text = soup.get_text().strip()
all_text


# ### Step 3: Store the Results
# 
# Extract the titles and preview text of the news articles that you scraped. Store the scraping results in Python data structures as follows:
# 
# * Store each title-and-preview pair in a Python dictionary. And, give each dictionary two keys: `title` and `preview`. An example is the following:
# 
#   ```python
#   {'title': "NASA's MAVEN Observes Martian Light Show Caused by Major Solar Storm", 
#    'preview': "For the first time in its eight years orbiting Mars, NASA’s MAVEN mission witnessed two different types of ultraviolet aurorae simultaneously, the result of solar storms that began on Aug. 27."
#   }
#   ```
# 
# * Store all the dictionaries in a Python list.
# 
# * Print the list in your notebook.

# In[16]:


# Create an empty list to store the dictionaries
articles = soup.find_all('div', class_='list_text')
articles


# In[17]:


# Loop through the text elements
# Extract the title and preview text from the elements
# Store each title and preview pair in a dictionary
# Add the dictionary to the list
art_list = []
for art in articles:
    title = art.find(class_='content_title').text
    preview = art.find(class_="article_teaser_body").text
    art_list.append({'title': title, 'preview': preview})
art_list


# In[8]:


# Print the list to confirm success
news_dict_list


# In[9]:


browser.quit()


# In[ ]:




