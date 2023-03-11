from pydantic import BaseModel
from routers_functions.scope_all import expire_date
from datetime import datetime


class RandomShort(BaseModel):
    origin_url: str = "https://www.pythonanywhere.com/"
    short_length: int = 3


class RandomShortResponse(BaseModel):
    origin_url: str = "https://www.pythonanywhere.com/"
    short_url: str = "https://hosting_name/mFh"
    expire_date: datetime = expire_date(days=7)

    class Config:
        orm_mode = True


class CustomShort(BaseModel):
    origin_url: str = "https://github.com/Massprod/UdemyFastAPI"
    custom_name: str = "provision"
    expire_days: int = 10


class CustomShortResponse(BaseModel):
    origin_url: str = "https://github.com/Massprod/UdemyFastAPI"
    short_url: str = "https://hosting_name/provision"
    expire_date: datetime = expire_date(days=10)

    class Config:
        orm_mode = True


class NewKey(BaseModel):
    email: str = "piankovpe@gmail.com"
    username: str = "whitewhale"


class NewKeyResponse(BaseModel):
    email: str = "piankovpe@gmail.com"
    username: str = "whitewhale"
    send: bool = True
    expire_date: datetime = expire_date(days=1)

    class Config:
        orm_mode = True


class ActivateResponse(BaseModel):
    email: str = "piankovpe@gmail.com"
    username: str = "whitewhale"
    activated: bool
    api_key: str = "123456789"

    class Config:
        orm_mode = True
