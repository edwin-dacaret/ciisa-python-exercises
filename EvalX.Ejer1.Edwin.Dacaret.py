import sqlite3
import datetime
from sqlite3 import Error

def sql_connection():
    try:
        con = sqlite3.connect('DENTAPLUS.db')
        return con
    except Error:
        print(Error)

def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE PACIENTES(RUT_PAC TEXT PRIMARY KEY NOT NULL, NOMBRE TEXT NOT NULL, APELLIDO TEXT "
                      "NOT NULL, EDAD NUMERIC NOT NULL);")
    cursorObj.execute("CREATE TABLE DENTISTAS(RUT_DEN TEXT PRIMARY KEY NOT NULL, NOMBRE TEXT NOT NULL, APELLIDO TEXT "
                      "NOT NULL, FECHA_INGRESO DATE DATE);")
    cursorObj.execute("CREATE TABLE ATENCIONES(ID NUMERIC PRIMARY KEY NOT NULL, RUT_PAC TEXT NOT NULL, RUT_DEN TEXT "
                      "NOT NULL, DESCRIPCION TEXT NOT NULL, FECHA_ATENCION DATE DATE);")

    dataPAC = [("11111111 - 1", "Soledad", "Ferrada", 65),
               ("22222222 - 2", "Margarita", "Gonzalés", 34),
               ("33333333 - 3", "Claudio", "Rifo", 46),
               ("44444444 - 4", "Maria", "Perez", 39),
               ("55555555 - 5", "Cristian", "Lopez", 18),
               ("66666666 - 6","Gladys", "Olivares", 45),
               ("77777777 - 7", "Natalia", "Fritz", 46)
              ]
    cursorObj.executemany("INSERT INTO PACIENTES VALUES(?, ?, ?, ?)", dataPAC)

    dataDEN = [("88888888 - 8", "Javier", "Miranda", datetime.date(2018, 5, 1)),
               ("99999999 - 9", "Patricia", "Manterola", datetime.date(2019, 1, 22)),
               ("12121212 - 1", "Paula", "Gallegos", datetime.date(2017, 9, 1)),
               ("45454545 - 4", "Pablo", "Pereira", datetime.date(2019, 4, 1)),
              ]
    cursorObj.executemany("INSERT INTO DENTISTAS VALUES(?, ?, ?, ?)", dataDEN)

    dataATE = [(1, "11111111 - 1", "88888888 - 8", "Extracción pieza 20", datetime.date(2019, 10, 1)),
               (2, "22222222 - 2", "88888888 - 8", "Limpieza completa", datetime.date(2019, 10, 4)),
               (3, "33333333 - 3", "99999999 - 9", "Tapadura simple pieza 5", datetime.date(2019, 10, 5)),
               (4, "44444444 - 4", "99999999 - 9", "Tapadura simple pieza 30", datetime.date(2019, 10, 6)),
               (5, "55555555 - 5", "12121212 - 1", "Extracción pieza 20", datetime.date(2019, 10, 7)),
               (6, "66666666 - 6", "45454545 - 4", "Tapadura compuesta pieza 30", datetime.date(2019, 10, 10)),
               (7, "77777777 - 7", "45454545 - 4", "Tapadura simple pieza 30", datetime.date(2019, 10, 15))
              ]
    cursorObj.executemany("INSERT INTO ATENCIONES VALUES(?, ?, ?, ?, ?)", dataATE)
    con.commit()

def sql_fetch(con):
    cursorObj = con.cursor()
    cursorObj.execute("SELECT * FROM PACIENTES WHERE EDAD > 30 ORDER BY NOMBRE ASC")
    rowsPa = cursorObj.fetchall()
    print("5) a. Tabla PACIENTES: Lista de todos los pacientes (todos los campos) cuya edad sea mayor a 30 años, ordenado de forma ascendente por el NOMBRE")
    for rowPa in rowsPa:
        print(rowPa)
    print("")

    cursorObj.execute("SELECT * FROM ATENCIONES WHERE RUT_DEN='99999999 - 9'")
    rowsAt = cursorObj.fetchall()
    print("5) b. Tabla ATENCIONES: Lista de todas las atenciones (Todos los campos) realizadas por el Dentista Patricia Manterola.")
    for rowAt in rowsAt:
        print(rowAt)
    print("")


con = sql_connection()
sql_table(con)
sql_fetch(con)
