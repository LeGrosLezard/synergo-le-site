import psycopg2

from config import DATABASE
from config import USER
from config import HOST
from config import PASSWORD


def creation_database():
    """Here we creating the main database."""

    #We call psycopg2 (database from heroku serveur)
    #We can call orm but i found it more simple...
    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()


    #TABLE VIDEO
    cur.execute("""
                CREATE TABLE VIDEO(
                    id serial PRIMARY KEY,
                    video_name VARCHAR(100),
                    pseudo VARCHAR(100)
                );
                """)

    conn.commit() 






if __name__ == "__main__":
    
    creation_database()
    


