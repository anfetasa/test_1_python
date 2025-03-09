from fastapi import FastAPI
from app.views import user_view

app = FastAPI()

# Incluir rutas desde la vista
app.include_router(user_view.router)

# Ruta de prueba
@app.get("/")
def home():
    return {"message": "Welcome to FastAPI MVC Project"}
