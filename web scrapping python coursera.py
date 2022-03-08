#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1
import yfinance as yf


# In[3]:


tesla = yf.Ticker('TSLA')
tesla_data  = tesla.history(period = 'max')
tesla_data.reset_index(inplace = True)
tesla_data.head()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[1]:


#2
from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[10]:


html_data = requests.get("https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue").text
soup = BeautifulSoup(html_data, "html.parser")
soup.find_all('title')
tesla_revenue = pd.DataFrame(columns = ['Date', 'Revenue'])

for row in soup.find_all("tbody")[1].find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    revenue = col[1].text.replace("$", "").replace(",", "")
    
    tesla_revenue = tesla_revenue.append({"Date": date, "Revenue": revenue}, ignore_index = True)
tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
tesla_revenue.tail()


# In[ ]:





# In[ ]:





# In[11]:


#3
GameStop = yf.Ticker("GME")
gme_data = GameStop.history(period = 'max')
gme_data.reset_index(inplace = True)
gme_data.head()


# In[ ]:





# In[ ]:





# In[12]:


#4
url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, "html.parser")
soup.find_all('title')
gme_revenue = pd.DataFrame(columns = ['Date', 'Revenue'])

for row in soup.find_all("tbody")[1].find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    revenue = col[1].text.replace("$", "").replace(",", "")
    
    gme_revenue = gme_revenue.append({"Date": date, "Revenue": revenue}, ignore_index = True)
tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
gme_revenue.tail()


# In[ ]:





# In[2]:


#5
make_graph(tesla_data, tesla_revenue, 'Tesla')


# In[ ]:





# In[ ]:





# In[ ]:


#6


# In[ ]:


make_graph(gme_data, gme_revenue, 'GameStop')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




