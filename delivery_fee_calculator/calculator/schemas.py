from datetime import datetime

from pydantic import BaseModel, validator, Field

# Default time format for the API
TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"


class Order(BaseModel):
    # The fields are defined in the order they should be in the API documentation
    # ... is used to indicate that the field is required
    # The description is used to generate the API documentation
    # The ge validator is used to validate that the value is greater than or equal to the given value
    cart_value: int = Field(
        ...,
        ge=0,
        description="The value of the cart in cents (e.g. 10000 for 100€)"
    )
    delivery_distance: int = Field(
        ...,
        ge=0,
        description="The distance to the delivery address in meters"
    )
    number_of_items: int = Field(
        ...,
        ge=0,
        description="The number of items in the cart"
    )
    time: str = Field(
        ...,
        description="The time of the order in the ISO format YYYY-MM-DDTHH:MM:SSZ"
    )

    # Pydantic asks for first parameter to be cls instead of self
    @validator("time")
    def time_must_be_valid(cls, v: str):
        try:
            datetime.strptime(v, TIME_FORMAT)
        except ValueError:
            raise ValueError("time must be valid")
        return v
