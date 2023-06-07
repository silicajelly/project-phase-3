import os
from alembic import context
from sqlalchemy import create_engine
from logging.config import fileConfig
from models import Base

# Load the database URL from an environment variable or specify it directly
db_url = os.getenv('DATABASE_URL') or 'sqlite:///autoparts.db'

# Configure Alembic to use SQLAlchemy
config = context.config
config.set_main_option('sqlalchemy.url', db_url)

# Interpret the config file for Python logging
fileConfig(config.config_file_name)

# Connect to the database and generate the Alembic metadata
engine = create_engine(db_url)
target_metadata = Base.metadata

# Run the Alembic migrations
with engine.connect() as connection:
    context.configure(
        connection=connection,
        target_metadata=target_metadata
    )

    with context.begin_transaction():
        context.run_migrations()
