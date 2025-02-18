from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
import os

engine = create_engine('sqlite:///mobile_db.sqlite3')
Base = automap_base()
Base.prepare(autoload_with=engine)


News = Base.classes.models_news  # Replace with your table name
Events = Base.classes.models_event
Employees = Base.classes.models_employee

Session = sessionmaker(bind=engine)
session = Session()




