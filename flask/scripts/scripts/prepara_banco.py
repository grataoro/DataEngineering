import MySQLdb
print('Conectando...')
conn = MySQLdb.connect(
    user='root', 
    passwd='root', 
    host='mysql', 
    port=3306)


#conn.cursor().execute("DROP DATABASE games;")
#conn.commit()

create_table = """

    SET NAMES utf8;
    CREATE DATABASE games;
    USE games;

    CREATE TABLE game (
        id int(11) NOT NULL AUTO_INCREMENT,
        name varchar(50) COLLATE utf8_bin NOT NULL,
        category varchar(40) COLLATE utf8_bin NOT NULL,
        console  varchar(20) NOT NULL,
        PRIMARY KEY (id)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

    CREATE TABLE user (
        id varchar(8) COLLATE utf8_bin NOT NULL,
        name varchar(20) COLLATE utf8_bin NOT NULL,
        password varchar(8) COLLATE utf8_bin NOT NULL,
        PRIMARY KEY (id)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

"""

conn.cursor().execute(create_table)

# inserindo usuarios
cursor = conn.cursor()
cursor.executemany(
      'INSERT INTO games.user (id, name, password) VALUES (%s, %s, %s)',
      [
            ('teste', 'teste', '123'),
            ('nico', 'Nico', '7a1'),
            ('danilo', 'Danilo', 'vegas')
      ])

cursor.execute('select * from games.user')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])

# inserindo jogos
cursor.executemany(
      'INSERT INTO games.game (name, category, console) VALUES (%s, %s, %s)',
      [
            ('God of War 4', 'Acao', 'PS4'),
            ('NBA 2k18', 'Esporte', 'Xbox One'),
            ('Rayman Legends', 'Indie', 'PS4'),
            ('Super Mario RPG', 'RPG', 'SNES'),
            ('Super Mario Kart', 'Corrida', 'SNES'),
            ('Fire Emblem Echoes', 'Estrategia', '3DS'),
      ])

cursor.execute('select * from games.game')
print(' -------------  Jogos:  -------------')
for jogo in cursor.fetchall():
    print(jogo[1])

# commitando senão nada tem efeito
conn.commit()
cursor.close()