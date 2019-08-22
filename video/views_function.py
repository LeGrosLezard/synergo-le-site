import os

def search_video_name(name_video):
    """Here when user upload his video
    we search if video name is present.
    If this name exists we ask user to change the
    name"""

    #Create folder to list
    liste = os.listdir(r"C:\Users\jeanbaptiste\Desktop\boboDancer\env\synergo\synergo\media\video_upload")
    #Define out (if out is None so we ask user to changes name)
    out = True
    #We try to see if the current video name
    #is already present
    for i in liste:
        if i == str(name_video):
            out = None
        
    return out
