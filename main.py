from fastapi import FastAPI,Request
import httpx,uvicorn


app = FastAPI()

PAYMENT_SERVICE_URL = "http://localhost:8001"
SHIPPING_SERVICE_URL = "http://localhost:8002"


@app.api_route("/payment/{path_name}",methods=["GET","POST","PUT","DELETE","OPTIONS"])
async def payment_service(request: Request, path_name: str):
    async with httpx.AsyncClient() as client:
        response = await client.request(
            request.method, f"{PAYMENT_SERVICE_URL}/{path_name}", headers=request.headers.raw, data=await request.body()
        )
        return response.content
    


@app.api_route("/shipping/{path_name}",methods=["GET","POST","PUT","DELETE","OPTIONS"])
async def shipping_service(request: Request, path_name: str):
    async with httpx.AsyncClient() as client:
        response = await client.request(
            request.method, f"{SHIPPING_SERVICE_URL}/{path_name}", headers=request.headers.raw, data=await request.body()
        )
        return response.content
    


if __name__ == "__main__":
    uvicorn.run(app, port=8000)