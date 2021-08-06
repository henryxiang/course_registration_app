from sqlalchemy.schema import CreateTable
from config import db_engine, Base
import model

tables = Base.metadata.tables

for t in tables:
    table = tables[t]
    ddl = CreateTable(table).compile(db_engine)
    ddl = str(ddl).strip() + ";\n"
    print(ddl)
