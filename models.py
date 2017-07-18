import sqlite3 as sql


def insert_alert(name,location):
    with sql.connect("test.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO alert (name, location) VALUES (?,?)", (name, location))
        con.commit()


def query_alerts():
    with sql.connect("test.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM alert")
        data = cur.fetchall()
        print data
        return data

#def update_hits(key):
#    with sql.connect("database.db") as con:
#        cur = con.cursor()
#        cur.execute("UPDATE link SET hits = (hits + 1) WHERE key=key")
#        con.commit()





