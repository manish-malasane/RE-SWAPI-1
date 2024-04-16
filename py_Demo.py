from pydantic import BaseModel


class Human(BaseModel):
    name: str
    age: int
    height: float


if __name__ == "__main__":
    data = {"name": "Sanskruti", "age": 22, "height": 160.04}
    result = Human(**data)
    print(result)
