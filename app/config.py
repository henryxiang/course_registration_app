from os.path import dirname, realpath
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask
from flask_restful import Api
import logging

logging.basicConfig(level=logging.DEBUG)

app_dir = dirname(realpath(__file__))
template_folder = f'{app_dir}/templates'

db_uri = 'mysql+mysqlconnector://root:mysql@localhost/course_registration'
db_engine = create_engine(db_uri, echo=True)
db_session = Session(db_engine)
Base = declarative_base()

app = Flask('Course Registration App')
api = Api(app)
