from fastapi import FastAPI
from datetime import datetime
from app.servicos.read_db import read_empresa

app = FastAPI()

@app.get("/api/v1/empresas/{empresa}")
async def consultar_empresa(empresa: str):
    empresa_info = read_empresa(empresa)

    if empresa_info is not None:
        return {"datetime": datetime.now(), "data": empresa_info, "status": 200}
    else:
        return {"datetime": datetime.now(), "message": "Empresa não encontrada", "status": 404}
