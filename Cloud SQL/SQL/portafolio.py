import pandas as pd

from google.cloud.sql.connector import Connector, IPTypes
import sqlalchemy

connector = Connector()

def getconn() -> sqlalchemy.engine.base.Connection:
    conn: sqlalchemy.engine.base.Connection = connector.connect(
        "sb-prototipos-xops:us-central1:motor-coberturas",
        "pg8000",
        user="postgres",
        password='motor-coberturas',
        db="postgres",
        ip_type=IPTypes.PUBLIC,  # Use IPTypes.PRIVATE for private IP
    )
    return conn

# Create SQLAlchemy engine
engine = sqlalchemy.create_engine(
    "postgresql+pg8000://",
    creator=getconn,
)

df = pd.read_csv('/home/juanfe/muestra_portafolio_v2.csv')#, sep='|')
df.to_sql('portafolio', engine, if_exists='replace', index=False)


