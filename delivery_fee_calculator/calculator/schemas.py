from pydantic import BaseModel, ValidationError


class order(BaseModel):
    cart_value: int
    distance: int
    number_of_items: int
    time: str
