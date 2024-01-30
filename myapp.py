from fastapi import FastAPI, Query
from modules.parser import getIp

app = FastAPI()

@app.get("/")
def get_current_time(full_name: str = Query("Горбунова Анна Сергеевна", title="Фамилия Имя Отчество")):
    ip_address = getIp()

    return {"Текущий IP-Адрес": ip_address, "Полное Имя": full_name}
