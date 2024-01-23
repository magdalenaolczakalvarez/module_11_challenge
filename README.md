# module_11_challenge web-scraping
UNC-CH-DA - Module 11 Challenge -web-scraping

INSTRUCTIONS
Clone the repository to your local machine
cd into the "web-scraping-challenge" directory.
The Jupyter Notebook for Part 1 of the challenge is 'part_1_mars_news.ipynb'
The Jupyter Notebook for Part 2 of the Challenge is 'part_2_mars_weather.ipynb'.
NOTE: You will need to have both Splinter and BeautifulSoup properly installed on your local system to be able to run the code.
ADDITIONAL NOTE: If you encounter an error with opening a chrome browser when trying to run the code, you may need to update the PATH per the instructions in 'download_chromedriver.md'
BACKGROUND
We are now ready to take on a full web-scraping and data analysis project. Use the skills we have learned such as identifying HTML elements on a page and identifying their 'id' and 'class' attributes. Use this inof to then extract inof using both automated browsing with Splinter and HTML parsing with BeautifulSoup. We will scrape for various info like HTML tables and recurring elements like newss articles.

REQUIREMENTS
Part 1: Scrape Titles and Preview Text from Mars News (40 points)
Automated browsing (with Splinter) was used to visit the Mars news site, and the HTML code was extracted (with Beautiful Soup). (10 points)

The titles and preview text of the news articles were scraped and extracted. (20 points)

The scraped information was stored in the specified Python data structure—specifically, a list of dictionaries. (10 points)

Part 2: Scrape and Analyze Mars Weather Data (60 points)
The HTML table was extracted into a Pandas DataFrame. Either Pandas or Splinter and Beautiful Soup were used to scrape the data. The columns have the correct headings and data types. (15 points)

The data was analyzed to answer the following questions: (10 points)

How many months exist on Mars? (5 points)
How many Martian days' worth of data are there? (5 points)
The data was analyzed to answer the following questions, and a data visualization was created to support each answer: (30 points)

Which month, on average, has the lowest temperature? The highest? (10 points)
Which month, on average, has the lowest atmospheric pressure? The highest? (10 points)
How many terrestrial days exist in a Martian year? A visual estimate within 25% was made. (10 points)
The DataFrame was exported into a CSV file. (5 points)

RESOURCES
Convert datetime to int: https://www.statology.org/pandas-convert-timedelta-to-int/

Pandas 'astype' method: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.astype.html

Pandas 'to_datetime' method: https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html?highlight=to_datetime#pandas.to_datetime
