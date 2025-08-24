# database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL =  "postgresql://neondb_owner:CeDyTMfmad79@ep-bitter-shadow-a5idvvdj.us-east-2.aws.neon.tech/neondb?sslmode=require"
# "postgresql://postgres:Hammad@7762131@db.erqsptnkadkzogyvxesz.supabase.co:5432/postgres"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
