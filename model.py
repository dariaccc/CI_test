from pydantic import BaseModel, Field
from typing import List, Optional
import json

class User(BaseModel):
    id: int
    email: str
    username: str
    is_active: bool = True
    tags: List[str] = Field(default_factory=list)
    age: Optional[int] = None

if __name__ == "__main__":
    # Print example user object
    data = {
        "id": 1,
        "username": "pixi_user",
        "email": "user@example.com",
        "tags": ["developer", "tester"]
    }
    user = User(**data)

    # Print JSON schema of the User model
    print(json.dumps(User.model_json_schema(), indent=2))
