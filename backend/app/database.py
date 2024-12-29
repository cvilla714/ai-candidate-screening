from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from .config import settings
import sys

# Determine if running in test mode
is_test_mode = "pytest" in sys.modules

# Set up the SQLAlchemy engine
engine = create_engine(settings.get_database_uri(is_test=is_test_mode))

# Configure the session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()
