USERNAME = 'celvalin'
PASSWORD = 'celvalin'
HOSTNAME = 'localhost'
PORT = 5432
DATABASE = 'celvalin'

SQLALCHEMY_DATABASE_URI = "postgresql://{username}:{password}@{host}:{port}/" \
         "{db}".format(username=USERNAME,
                password=PASSWORD,
                host=HOSTNAME,
                port=PORT,
                db=DATABASE)

SECRET_KEY = 'UMAnrHz4bTJVSrejbJuTty2WTWl3IwVe'

SQLALCHEMY_TRACK_MODIFICATIONS = True
