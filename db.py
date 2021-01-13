import psycopg2

def createtable():
    conn = psycopg2.connect("dbname='data2' user='postgres' password='1234' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE data(rollno INTEGER, name TEXT, marks REAL)")
    conn.commit()
    conn.close()

def insert(roll,nam,mark):
    conn = psycopg2.connect("dbname='data2' user='postgres' password='1234' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("INSERT INTO data VALUES(%s,%s,%s)", (roll, nam, mark))
    conn.commit()
    conn.close()

insert(4, 'pugghero', 100)


