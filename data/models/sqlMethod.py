import psycopg2 
# from ..config import *
PASSWORD = "1122banforChild_"
USER = "postgres"
PORT = 8000

def psql():
    conn = psycopg2.connect(database = 'postgres',
                            user = USER, 
                            password = PASSWORD,
                            port = PORT,)
    cur = conn.cursor()
    
    # cur.execute('''CREATE TABLE spisok (id serial PRIMARY KEY,
    #             username VARCHAR(20),
    #             balance INTEGER,
    #             is_baned bool);''')
    
    cur.execute('''INSERT INTO spisok (username,balance) VALUES ('ADMIN',0 );''')
    
    cur.execute('''SELECT * FROM spisok;''')
    print(info := cur.fetchall())
    
    
       
if __name__ == '__main__':
    psql()