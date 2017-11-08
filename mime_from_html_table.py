
# coding: utf-8

# In[1]:


import pandas as pd
import json


# In[2]:


import pandas as pd
url = r'https://www.iana.org/assignments/media-types/media-types.xhtml'
tables = pd.read_html(url) # Returns list of all tables on page

application = tables[0] 
audio = tables[1]
font = tables[2]
images = tables[4]
message = tables[5]
model = tables[6]
multipart = tables[7]
text = tables[8]
video = tables[9]

media_tables = [application,
                audio,
                font,
                images,
                message,
                model,
                multipart,
                text,
                video]


# In[3]:


buf = []
for k in range(len(media_tables)):
    buf2 = []
    for i in media_tables[k]['Name']:
        try:
            buf2.append((str(i).split("/")[1]))
        except:
            buf2.append("nan")
    buf.append(buf2)


# In[4]:


with open('mime_json.json', 'w') as mime_json:
    json.dump(
        {'application':buf[0]
          ,'audio':buf[1]
          ,'font':buf[2]
          ,'images':buf[3]
          ,'message':buf[4]
          ,'model':buf[5]
          ,'multipart':buf[6]
          ,'text':buf[7]
          ,'video':buf[8]}
    , mime_json)

