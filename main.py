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

def read_unknown_file(file_path):
    with open(file_path, 'rb') as file:
        contents = file.read()
    return contents

def file_path():
    filePath = get_chrome_bookmarks_path()
    try:
        file_contents = read_unknown_file(filePath)
        return file_contents
    except Exception as e:
        print("Error reading the file:", str(e))

import json

def collecting(file_dict):
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
            json.dumps(data, indent=2) 
        except:
            pass
    return data


def main():
    contents=file_path()
    file_dict = json.loads(contents)
    data=collecting(file_dict)
    return data

save_file = open("output.json", "w") 
data= main()
json.dump(data, save_file, indent = 4)  
save_file.close()  


