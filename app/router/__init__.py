from config import app
from . import home

app.register_blueprint(home.bp)
