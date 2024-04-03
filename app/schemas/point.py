from typing import Optional

from pydantic import BaseModel, Field, Extra, field_validator

from app.core.config import settings


class PointBase(BaseModel):
    name: Optional[str] = Field(
        None,
        min_length=settings.min_name_len,
        max_length=settings.max_name_len
    )
    description: Optional[str]
    address: Optional[str] = Field(
        None,
        min_length=settings.min_address_len,
        max_length=settings.max_address_len
    )


class Config:
    extra = Extra.forbid


class PointCreate(PointBase):
    name: str = Field(
        ...,
        min_length=settings.min_name_len,
        max_length=settings.max_name_len
    )
    address: str = Field(
        ...,
        min_length=settings.min_address_len,
        max_length=settings.max_address_len
    )


class PointUpdate(PointBase):
    @field_validator('name')
    def name_cannot_be_null(cls, value):
        if value is None:
            raise ValueError(settings.name_error)
        return value

    @field_validator('address')
    def address_cannot_be_null(cls, value):
        if value is None:
            raise ValueError(settings.address_error)
        return value


class PointDB(PointBase):
    id: int

    class Config:
        orm_mode = True
