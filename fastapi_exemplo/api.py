from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# definimos uma classe para serializar os dados.
class LinuxTips(BaseModel):
    canal: str
    msg: str
    dia: int


@app.get("/", response_model=LinuxTips)
async def linuxtips():  # Callable
    return LinuxTips(
        canal="LinuxTips",
        msg="Vaiiii",
        dia=25
    )
