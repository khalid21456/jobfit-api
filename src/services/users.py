from sqlalchemy import select

from src.config.database import DBSession
from src.models.models import User


class UserService:

    def get_users(self, db: DBSession):
        users = db.scalars(select(User)).all()
        return [
            {"id": u.id, "name": u.name, "email": u.email}
            for u in users
        ]
