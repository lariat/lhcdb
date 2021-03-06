from flask.ext.sqlalchemy import SQLAlchemy

from lhcdb import app

db = SQLAlchemy(app)

db_session = db.session

Base = db.Model

def init_db():
    import lhcdb.models
    db.create_all()

#from sqlalchemy import create_engine
#from sqlalchemy.orm import scoped_session, sessionmaker
#from sqlalchemy.ext.declarative import declarative_base
#
#engine = create_engine('postgresql://localhost/lhcdb', echo=False)
#
#db_session = scoped_session(
#    sessionmaker(autocommit=False, autoflush=False, bind=engine)
#    )
#
#Base = declarative_base()
#Base.query = db_session.query_property()
#
#def init_db():
#    import lhcdb.models
#    Base.metadata.create_all(bind=engine)
