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



def recup_video_user(pseudo):
    
    #We call psycopg2 (database from heroku serveur)
    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()

    cur.execute("""select * from VIDEO where pseudo='{}'""".format(pseudo))

    conn.commit() 

    rows = cur.fetchall()
    liste = [i for i in rows]
    liste_video = []
    for i in liste:
        liste_video.append(liste[0][1])

    return liste_video
    #In real word -> give me from the video table from
    #database the lign where current user nmae is present ty































