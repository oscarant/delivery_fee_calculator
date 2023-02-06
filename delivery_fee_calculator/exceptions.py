from typing import Sequence

from pydantic import BaseModel, ValidationError
from pydantic.error_wrappers import ErrorList


class RequestValidationError(ValidationError):
    def __init__(self, errors: Sequence[ErrorList], model: BaseModel) -> None:
        super().__init__(errors, model)  # noqa
