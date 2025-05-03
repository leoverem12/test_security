from typing import Optional, List,Union
from pyndantic_models import UserModel, UserModelResponce

from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, HTTPBasic, HTTPBasicCredentials
from fastapi.concurrency import asynccontextmanager
from sqlalchemy import select, insert,update
from sqlalchemy.orm import Session
import uvicorn


from models import get_db, User, database


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()


oauth2_schema = OAuth2PasswordBearer(tokenUrl="/token/")
app = FastAPI(lifespan=lifespan)



async def get_user(token: str = Depends(oauth2_schema), db: Session = Depends(get_db)):
    if token != "1234":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    user = db.query(User).where(User.id==1).one()
    return user

@app.post("/token/")
async def get_token(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username == "user" and form_data.password == "pass":
        return dict(access_token="1234", token_type="bearer")
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)


@app.get("/user/me/")
async def get_user_me(current_user: User = Depends(get_user)):
    return current_user



@app.post("/users/")
async def add_user(user_model: UserModel, db: Session = Depends(get_db)):
    user = User(**user_model.model_dump())
    db.add(user)
    db.commit()

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8001)