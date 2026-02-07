import requests


class UserClient:

    BASE_URL = "http://localhost:8001"

    def user_exists(self, user_id: str) -> bool:
        response = requests.get(f"{self.BASE_URL}/users/{user_id}")
        return response.status_code == 200
