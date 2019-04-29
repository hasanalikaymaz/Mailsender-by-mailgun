#!/usr/bin/env python
# coding: utf-8

# In[5]:


import requests


# In[6]:


requests.post(
    "https://api.mailgun.net/v3/sandbox3f42343d26904febb8a3c70347706c74.mailgun.org/messages",
    auth=("api", "9501a9bdda85d819b543bc70c031602c-6140bac2-cf5df748"),
    data={"from": "Mailgun Sandbox <postmaster@sandbox3f42343d26904febb8a3c70347706c74.mailgun.org>",
          "to": "test <hasanalikaymaz@gmail.com>",
              "subject": "Hello World",
          "text": "It works"
         
            
         })


# In[ ]:




