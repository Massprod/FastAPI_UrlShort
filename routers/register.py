from fastapi import APIRouter, Request, Depends, Path
from sqlalchemy.orm.session import Session
from schemas.schemas import NewKey, NewKeyResponse, ActivateResponse
from database.database import db_session
from routers_functions.register_functions import add_new_key, activate_new_key
from limiter import req_limiter, register_limit

register_route = APIRouter(prefix="/register",
                           tags=["register"],)


@register_route.post(path="/new",
                     name="register new api-key",
                     response_model=NewKeyResponse,
                     description="Creating new Api-key and sending to provided Email. "
                                 "Can't be used and expire in 1 day if not activated.",
                     response_description="Correct Json response with registration data",
                     )
@req_limiter.limit(register_limit)
async def register_new_key(request: Request,
                           data: NewKey,
                           db: Session = Depends(db_session)
                           ):
    return add_new_key(request, data, db)


@register_route.get(path="/activate/{activation_key}",
                    name="activate registered api-key",
                    response_model=ActivateResponse,
                    description="Change activation status for registered Api-key via "
                                "activation link sent to Email",
                    response_description="Correct Json response with data about activated Api-key",
                    )
@req_limiter.limit(register_limit)
async def activating_new_keys(request: Request,
                              activation_key: str = Path(description="Generated key from sent activation link"),
                              db: Session = Depends(db_session)
                              ):
    return activate_new_key(request, activation_key, db)
