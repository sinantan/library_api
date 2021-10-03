from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import Config

engine=create_engine(Config.SQLALCHEMY_DATABASE_URI,
    echo=True
)

Base=declarative_base()
SessionLocal=sessionmaker(bind=engine)

#Base.metadata.create_all(engine)