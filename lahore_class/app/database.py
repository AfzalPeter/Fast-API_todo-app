# database.py
from contextlib import asynccontextmanager
from app import settings
from sqlmodel import create_engine

# only needed for psycopg 3 - replace postgresql
# with postgresql+psycopg in settings.DATABASE_URL
connection_string = str(settings.DATABASE_URL).replace(
    "postgresql", "postgresql+psycopg"
)

# recycle connections after 5 minutes
# to correspond with the compute scale down
# this function will connect with database )
engine = create_engine(
    connection_string, connect_args={"sslmode": "require"}, pool_recycle=300
)

def create_db_and_tables():
    from models import Todo  # Importing here to ensure tables are created
    SQLModel.metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app):
    print("Creating tables..")
    create_db_and_tables()
    yield
