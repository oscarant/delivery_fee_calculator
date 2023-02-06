from datetime import datetime

from pydantic import BaseModel, validator


class Order(BaseModel):
    cart_value: int
    delivery_distance: int
    number_of_items: int
    time: str

    # Pydantic asks for first parameter to be cls instead of self
    @validator("cart_value")
    def cart_value_must_be_positive(cls, v):
        if v < 0:
            raise ValueError("cart_value must be positive")
        return v

    @validator("delivery_distance")
    def delivery_distance_must_be_positive(cls, v):
        if v < 0:
            raise ValueError("delivery_distance must be positive")
        return v

    @validator("number_of_items")
    def number_of_items_must_be_positive(cls, v):
        if v < 0:
            raise ValueError("number_of_items must be positive")
        return v

    @validator("time")
    def time_must_be_valid(cls, v):
        try:
            datetime.fromisoformat(v)
        except ValueError:
            raise ValueError("time must be valid")
        return v
