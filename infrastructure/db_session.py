from .database import Session

import contextlib


class SessionGenerator:
    @staticmethod
    @contextlib.contextmanager
    def generate():
        session = Session()
        try:
            yield session
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
