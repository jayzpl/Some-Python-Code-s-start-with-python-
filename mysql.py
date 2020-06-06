#pip install MySQL
import MySQLdb
db=MySQLdb.connect("sql.losto.net","00051799_kolko1","kolko123","00051799_kolko1")
kursor=db.cursor()
sql="DROP TABLE IF EXISTS kk"
kursor.execute(sql)
sql="CREATE TABLE kk(id INT(6) AUTO_INCREMENT NOT NULL, imie char(16), nazwisko char(16), wiek int(2), PRIMARY KEY (id))"
kursor.execute(sql)
sql="INSERT INTO kk VALUES('1','Jan','Kowalski','16')"
kursor.execute(sql)
sql="INSERT INTO kk VALUES('2','Adam','Nowak','12')"
kursor.execute(sql)
sql="INSERT INTO kk VALUES('3','Misia','Ela','6')"
kursor.execute(sql)
db.commit()
sql="SELECT * FROM kk"
try:
    kursor.execute(sql)
    rezultat=kursor.fetchall()
    for row in rezultat:
        id=row[0]
        imie=row[1]
        nazwisko=row[2]
        wiek=row[3]
        print("ID: %s imie: %s nazwisko: %s wiek: %s" % (id, imie, nazwisko, wiek) )
except:
    print("Blad bazy danych")


db.close()