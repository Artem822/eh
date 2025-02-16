from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

try:
    engine = create_engine('sqlite:///mobile/app/src/assets/mobile_db.sqlite3')
    Base = automap_base()
    Base.prepare(autoload_with=engine)


    News = Base.classes.models_news  # Replace with your table name
    Events = Base.classes.models_event
    Employees = Base.classes.models_employee

    Session = sessionmaker(bind=engine)
    session = Session()
except:
    engine = create_engine('sqlite:///app/src/assets/mobile_db.sqlite3')
    Base = automap_base()
    Base.prepare(autoload_with=engine)


    News = Base.classes.models_news  # Replace with your table name
    Events = Base.classes.models_event
    Employees = Base.classes.models_employee

    Session = sessionmaker(bind=engine)
    session = Session()



