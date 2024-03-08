import sqlite3

# este fragmento inicializara una base de datos SQLite3 si no existe ** sin tablas **
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

RUTADB = "instance/data.db"
db = sqlite3.connect(RUTADB, check_same_thread=False)                #si no existe la base de datos se crea en este punto
db.row_factory = dict_factory

# cursor para ejecutar consultas
cursor = db.cursor()

# este fragmento inserta tablas si no existen ...
cursor.execute("CREATE TABLE IF NOT EXISTS cafe (\
    id             INTEGER       PRIMARY KEY,\
    name           VARCHAR (250) NOT NULL\
                                 UNIQUE,\
    map_url        VARCHAR (500) NOT NULL,\
    img_url        VARCHAR (500) NOT NULL,\
    location       VARCHAR (250) NOT NULL,\
    has_sockets    BOOLEAN       NOT NULL,\
    has_toilet     BOOLEAN       NOT NULL,\
    has_wifi       BOOLEAN       NOT NULL,\
    can_take_calls BOOLEAN       NOT NULL,\
    seats          VARCHAR (250),\
    coffee_price   VARCHAR (250)\
);\
")

# consultas ~~~ artesanales ~~~
def QUERY_buscaTodosLosCafes()->[]:
    res = cursor.execute("SELECT\
                          cafe.id               AS cafe_id,\
                          cafe.name             AS cafe_name,\
                          cafe.map_url          AS cafe_map_url,\
                          cafe.img_url          AS cafe_img_url,\
                          cafe.location         AS cafe_location,\
                          cafe.has_sockets      AS cafe_has_sockets,\
                          cafe.has_toilet       AS cafe_has_toilet,\
                          cafe.has_wifi         AS cafe_has_wifi,\
                          cafe.can_take_calls   AS cafe_can_take_calls,\
                          cafe.seats            AS cafe_seats,\
                          cafe.coffee_price     AS cafe_coffee_price\
                        FROM cafe")
    return res.fetchall()

def QUERY_insertaNuevoCafe(name, map_url, imgUrl, location, sockets, toilet, wifi, calls, seats, coffeePrice)->[]:
  cursor.execute("\
  INSERT INTO cafe(\
    name,\
    map_url,\
    img_url,\
    location,\
    has_sockets,\
    has_toilet,\
    has_wifi,\
    can_take_calls,\
    seats,\
    coffee_price\
  )\
  VALUES(?,?,?,?,?,?,?,?,?,?)", (name, map_url, imgUrl, location, sockets, toilet, wifi, calls, seats, coffeePrice,))
  db.commit()

def QUERY_eliminarCafe(id)->[]:
    res = cursor.execute("\
    DELETE FROM cafe\
    WHERE\
    id = ?",(id,))
    db.commit()
