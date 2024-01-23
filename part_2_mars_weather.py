#!/usr/bin/env python
# coding: utf-8

# # Module 12 Challenge
# ## Deliverable 2: Scrape and Analyze Mars Weather Data

# In[36]:


# Import relevant libraries
from splinter import Browser
from bs4 import BeautifulSoup as soup
import matplotlib.pyplot as plt
import pandas as pd


# In[37]:


browser = Browser('chrome')


# ### Step 1: Visit the Website
# 
# Use automated browsing to visit the [Mars Temperature Data Site](https://static.bc-edx.com/data/web/mars_facts/temperature.html). Inspect the page to identify which elements to scrape.
# 
#    > **Hint** To identify which elements to scrape, you might want to inspect the page by using Chrome DevTools to discover whether the table contains usable classes.
# 

# In[38]:


# Visit the website
# https://static.bc-edx.com/data/web/mars_facts/temperature.html
url = "https://static.bc-edx.com/data/web/mars_facts/temperature.html"
browser.visit(url)


# ### Step 2: Scrape the Table
# 
# Create a Beautiful Soup object and use it to scrape the data in the HTML table.
# 
# Note that this can also be achieved by using the Pandas `read_html` function. However, use Beautiful Soup here to continue sharpening your web scraping skills.

# In[39]:


# Create a Beautiful Soup Object
html = browser.html
mars_soup = soup(html, 'html.parser')
mars_soup


# ### Step 3: Store the Data
# 
# Assemble the scraped data into a Pandas DataFrame. The columns should have the same headings as the table on the website. Here’s an explanation of the column headings:
# 
# * `id`: the identification number of a single transmission from the Curiosity rover
# * `terrestrial_date`: the date on Earth
# * `sol`: the number of elapsed sols (Martian days) since Curiosity landed on Mars
# * `ls`: the solar longitude
# * `month`: the Martian month
# * `min_temp`: the minimum temperature, in Celsius, of a single Martian day (sol)
# * `pressure`: The atmospheric pressure at Curiosity's location

# In[40]:


# Create an empty list
mars_table_data = []

# Loop through the scraped data to create a list of rows
for row in mars_data_rows:
    # extract list of tds from table row
    row_data = row.select('td')
    
     # create a temporary row data list
    temp_row_data = []

    # loop through row_data to and append to temp_row_data
    for td in row_data:
        # append data to temp list
        temp_row_data.append(td.text)
    
    # append temp_row_data list to mars_table_data
    mars_table_data.append(temp_row_data)


# In[41]:


# Create a Pandas DataFrame by using the list of rows and a list of the column names
mars_df = pd.DataFrame(mars_table_data, columns=['id', 'terrestrial_date', 'sol', 'ls', 'month', 'min_temp', 'pressure'])


# In[42]:


# Confirm DataFrame was created successfully
mars_df.head()


# ### Step 4: Prepare Data for Analysis
# 
# Examine the data types that are currently associated with each column. If necessary, cast (or convert) the data to the appropriate `datetime`, `int`, or `float` data types.
# 
#   > **Hint** You can use the Pandas `astype` and `to_datetime` methods to accomplish this task.
# 

# In[43]:


# Examine data type of each column
mars_df.dtypes


# In[44]:


# Change data types for data analysis
mars_df = mars_df.astype({
    "id": object,
    "terrestrial_date": "datetime64[ns]",
    "sol": int,
    "ls": int,
    "month": int,
    "min_temp": float,
    "pressure": float
})


# In[45]:


# Confirm type changes were successful by examining data types again
mars_df.dtypes


# ### Step 5: Analyze the Data
# 
# Analyze your dataset by using Pandas functions to answer the following questions:
# 
# 1. How many months exist on Mars?
# 2. How many Martian (and not Earth) days worth of data exist in the scraped dataset?
# 3. What are the coldest and the warmest months on Mars (at the location of Curiosity)? To answer this question:
#     * Find the average the minimum daily temperature for all of the months.
#     * Plot the results as a bar chart.
# 4. Which months have the lowest and the highest atmospheric pressure on Mars? To answer this question:
#     * Find the average the daily atmospheric pressure of all the months.
#     * Plot the results as a bar chart.
# 5. About how many terrestrial (Earth) days exist in a Martian year? To answer this question:
#     * Consider how many days elapse on Earth in the time that Mars circles the Sun once.
#     * Visually estimate the result by plotting the daily minimum temperature.
# 

# In[46]:


# 1. How many months are there on Mars?
mars_df['month'].value_counts().sort_index()


# In[47]:


# 2. How many Martian days' worth of data are there?
mars_df['sol'].nunique()


# In[48]:


# 3. What is the average low temperature by month?
mars_mos_avg_low_temp = mars_df.groupby('month').min_temp.agg('mean')
mars_mos_avg_low_temp


# In[49]:


# Plot the average temperature by month
mars_mos_avg_low_temp.plot.bar()
plt.xlabel('month')
plt.ylabel('Temperature in Celsius')
plt.show()


# In[50]:


# Identify the coldest and hottest months in Curiosity's location
mars_mos_min_temp = mars_mos_avg_low_temp.sort_values()
mars_mos_min_temp

mars_mos_min_temp.plot.bar()
plt.xlabel('month')
plt.ylabel('Temperature in Celsius')
plt.show()


# In[51]:


# 4. Average pressure by Martian month
mars_mos_avg_pressure = mars_df.groupby('month').pressure.agg('mean')
mars_mos_avg_pressure


# In[52]:


# Plot the average pressure by month
mars_mos_avg_pressure.plot.bar()
plt.xlabel('month')
plt.ylabel('Atmospheric Pressure')
plt.show()


# In[53]:


# 5. How many terrestrial (earth) days are there in a Martian year?
first_terra_day = mars_df['terrestrial_date'].agg('min')
terra_days_min_temps_df = pd.DataFrame({
    "min_temp": mars_df['min_temp'],
    "terra_days": mars_df['terrestrial_date'] - first_terra_day
})
plt.plot(terra_days_min_temps_df["terra_days"].dt.days, terra_days_min_temps_df["min_temp"])
plt.xlabel("Number of terrestrial days")
plt.ylabel("Minimum temperature")
plt.show()


# On average, the third month has the coldest minimum temperature on Mars, and the eighth month is the warmest. But it is always very cold there in human terms!
# 
# 

# Atmospheric pressure is, on average, lowest in the sixth month and highest in the ninth.

# The distance from peak to peak is roughly 1425-750, or 675 days. A year on Mars appears to be about 675 days from the plot. Internet search confirms that a Mars year is equivalent to 687 earth days.

# ### Step 6: Save the Data
# 
# Export the DataFrame to a CSV file.

# In[54]:


# Write the data to a CSV
mars_df.to_csv('mars_weather_data.csv', header=True, index=False, date_format='%Y-%m-%d')


# In[55]:


browser.quit()


# In[ ]:




