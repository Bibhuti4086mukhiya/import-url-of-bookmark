#!/usr/bin/env python
# coding: utf-8

# In[9]:


import os

def get_chrome_bookmarks_path():
    if os.name == 'nt':  # Windows
        app_data_path = os.getenv('LOCALAPPDATA')
        return os.path.join(app_data_path, 'Google', 'Chrome', 'User Data', 'Default', 'Bookmarks')
    elif os.name == 'posix':  # macOS or Linux
        home_path = os.path.expanduser('~')
        return os.path.join(home_path, '.config', 'google-chrome', 'Default', 'Bookmarks')
    else:
        raise OSError("Unsupported operating system.")

# Usage example
bookmarks_path = get_chrome_bookmarks_path()
# print("Chrome bookmarks path:",bookmarks_path)
# print(os.startfile(bookmarks_path))


# In[11]:


def read_unknown_file(file_path):
    with open(file_path, 'rb') as file:
        contents = file.read()
    return contents
# Usage example
file_path = bookmarks_path
try:
    file_contents = read_unknown_file(file_path)
    # print("File contents: successful read path", )
except Exception as e:
    print("Error reading the file:", str(e))


# In[12]:


import json
file_dict = json.loads(file_contents)


# In[14]:


data={
     "BookMarks":
        [{
            "title":"",
            "url":""
        }],
    }
for i in file_dict['roots']['bookmark_bar']['children']:
    try:
        if [i][0]['name']=='' or [i][0]['url']=='':
            continue
        data['BookMarks'] +=[{ "title":f"{[i][0]['name']}",
                              "url: ":f"{[i][0]['url']}"
                            }]
        updated_json = json.dumps(data, indent=2) 
    except:
        pass
# print(updated_json)


# In[15]:


save_file = open("output.json", "w")  
json.dump(data, save_file, indent = 6)  
save_file.close()  


# In[ ]:




