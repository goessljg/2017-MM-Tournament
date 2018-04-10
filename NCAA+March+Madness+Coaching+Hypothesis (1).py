
# coding: utf-8

# In[1]:

get_ipython().system('python --version')


# In[2]:

#version of python installed


# In[3]:

get_ipython().system('pip --version')


# In[4]:

#version of pip installed, upgrade pip to newest release
#install setuptoos and wheel


# In[5]:

get_ipython().system('python -m pip install --upgrade pip setuptools wheel')


# In[6]:

#make sure that beatiful soup is installed


# In[7]:

get_ipython().system('pip install beautifulsoup4')


# In[8]:

#make sure that html5lib is installed
#  <body>
#   <p class="title">


# In[9]:

get_ipython().system('pip install html5lib')


# In[10]:

#go to sports-reference.com website and import coach and statistics for 2000-2017


# In[11]:

import requests
from bs4 import BeautifulSoup


page = requests.get('https://www.sports-reference.com/cbb/seasons/2018-coaches.html')

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')


# In[14]:

import requests
from bs4 import BeautifulSoup


# Collect and parse first page
page = requests.get('https://www.sports-reference.com/cbb/seasons/2018-coaches.html')
soup = BeautifulSoup(page.text, 'html.parser')

# Pull all text from the BodyText div
coach_name_list = soup.find(class_='left')

# Pull text from all instances of <a> tag within BodyText div
coach_name_list_items = coach_name_list.find_all ('a')

for coach_name in coach_name_list_items:
    print(coach_name.prettify())


# In[24]:

import requests
from bs4 import BeautifulSoup


# Collect and parse first page
page = requests.get('https://www.sports-reference.com/cbb/seasons/2018-coaches.html')
soup = BeautifulSoup(page.text, 'html.parser')

# Pull all text from the BodyText div
coach_name_list = soup.find(class_='left')

# Pull text from all instances of <a> tag within BodyText div
coach_name_list_items = coach_name_list.find ('a')

for coach_name in coach_name_list_items:
    print(coach_name)


# In[27]:

import requests
from bs4 import BeautifulSoup


# Collect and parse first page
page = requests.get('https://www.sports-reference.com/cbb/seasons/2018-coaches.html')
soup = BeautifulSoup(page.text, 'html.parser')

table = soup.find('div',id= 'div_coaches')
rows = table.find_all('tr')
for row in rows:
    print (row.text)


# In[ ]:




# In[ ]:




# In[ ]:



