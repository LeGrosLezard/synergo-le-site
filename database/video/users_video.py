import psycopg2

from .config import DATABASE
from .config import USER
from .config import HOST
from .config import PASSWORD


def insertion_video_user(pseudo):
    """Here we insert into the database
    of the current user
    his video uploaded"""

    #We call psycopg2 (database from heroku serveur)
    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()

    cur.execute("""select id, nom, prenom, lieu_habitation, fixe,
                portable, email from users
                where pseudo = '{}';""".format(pseudo))

    conn.commit() 

    rows = cur.fetchall()
    liste = [i for i in rows]

    return liste[0][0], liste[0][1], liste[0][2], liste[0][3],\
           liste[0][4], liste[0][5], liste[0][6]



























