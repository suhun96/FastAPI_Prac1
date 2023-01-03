from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}".format(
    DB_USERNAME = 'Hoon',
    DB_PASSWORD = '9292455z',
    DB_HOST = "127.0.0.1",
    DB_PORT = '3306',
    DB_DATABASE = 'FastAPI',
))


db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

def get_db():
    db = db_session()
    try:
        yield db
    finally:
        db.close()