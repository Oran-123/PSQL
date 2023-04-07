from sqlalchemy import (
    create_engine, Column, Float, Fore
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions 

db = create_enginge("postgresql:///chinook")
base=declarative_base()

#
class Artist(base):
    _tablename_ = "Artist"
    ArtistID = 
#
#
Session = sessionmaker(db)
#
session = Session()

#

base.metadata.create_all(db)