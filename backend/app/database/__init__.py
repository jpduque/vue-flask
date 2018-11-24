""" API Blueprint Application """

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from .config import connection_strings

__all__ = ["DatabaseConnection", "DatabaseSession"]

connection_string = connection_strings.get("main")

engine = create_engine(connection_string)

class DatabaseConnection:

    def __enter__(self):
        # make a database connection and return it
        self.conn = engine.connect()
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        # make sure the dbconnection gets closed
        self.conn.close()


class DatabaseSession:

    def __enter__(self):
        self.session = Session(engine)

        # NB: following line is not needed if instances of SQL entities are replaced with other classes,
        # before passing results to business logic and above layers (which is recommended!)
        # Here for simplicity, data access layer entities are passed above to business logic;
        self.session.expire_on_commit = False

        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
        self.session = None