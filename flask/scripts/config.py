SECRET_KEY = 'key'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{user}:{pssw}@{host}/{db}'.format(
        SGBD = 'mysql+mysqlconnector',
        user = 'root',
        pssw = 'root',
        host = 'mysql',
        db   = "games"
    )