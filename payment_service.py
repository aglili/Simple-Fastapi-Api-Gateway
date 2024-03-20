from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
import httpx,uvicorn



app = FastAPI()


@app.get("/{path_name}")
async def payment_service(path_name: str):
    response_data = {"path_name": path_name}
    return response_data     





if __name__ == "__main__":
    uvicorn.run(app, port=8001)

