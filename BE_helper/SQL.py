import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import sessionmaker

print (sqlalchemy.__version__)
metadata = MetaData()
books = Table('book', metadata,
  Column('id', Integer, primary_key=True),
  Column('title', String),
  Column('primary_author', String),
)
some_engine = create_engine('mysql+pymysql://root:root@localhost/mysql')
Session = sessionmaker(bind=some_engine)

session = Session()
with some_engine.connect() as con:
    rs = con.execute('select * from mysql.user;')
for data in rs:
    print (data)

session.commit()