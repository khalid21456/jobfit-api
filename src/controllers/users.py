from fastapi import APIRouter

from src.config.database import DBSession
from src.services.users import UserService


class UserController:

    def __init__(self, service: UserService | None = None):
        self.service = service or UserService()
        self.router = APIRouter(prefix="/api/users", tags=["users"])
        self.router.add_api_route("", self.list_users, methods=["GET"])

    def list_users(self, db: DBSession):
        return self.service.get_users(db)
