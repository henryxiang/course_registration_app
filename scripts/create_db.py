from config import db_engine, Base
import model

Base.metadata.drop_all(db_engine)
Base.metadata.create_all(db_engine)
