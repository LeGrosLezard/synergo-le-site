import psycopg2

from .config import DATABASE
from .config import USER
from .config import HOST
from .config import PASSWORD



def current_user_video(pseudo, video_name):
    """We insert video/user"""
    
    #We call psycopg2 (database from heroku serveur)
    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()

    cur.execute("""
                INSERT INTO VIDEO
                (video_name, pseudo)
                VALUES(%s, %s);
                """, (str(video_name), str(pseudo)))

    conn.commit() 
    #In real word -> we insert in the table of the database
    #who's called VIDEO the name of video and of user







##    rows = cur.fetchall()
##    liste = [i for i in rows]
##
##    print(liste)
































