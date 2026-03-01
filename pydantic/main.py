from pydantic import BaseModel, EmailStr, validator

class User(BaseModel):
    name: str
    age: int
    email: str

    @validator('age')
    def age_must_be_positive(cls, v):
        if v < 0:
            raise ValueError('Age must be positive')
        return v

# test
user = User(name="Alice", age=25, email="alice@example.com")
print(user)

# erreur
try:
    bad_user = User(name="Bob", age=-5, email="bob@example.com")
except Exception as e:
    print(e)