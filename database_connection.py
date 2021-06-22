import config 
import psycopg2 
import pandas as pd


try: 
    conn  = psycopg2.connect(dbname=config.db_name,user=config.username,password=config.password,host = config.host,
    port=config.port)
    print('ok')
except AttributeError:
    print("connection failed")
print(conn)

def send_request(query):
    cursor = conn.cursor()
    try:
        cursor.execute(query)

    except AttributeError:
        print("Invalid query")
    
    query_results = cursor.fetchall()
    res = pd.DataFrame(query_results, columns=[desc[0] for desc in cursor.description])
    conn.close()
    cursor.close()
    return res
    
            

