from fastapi import FastAPI, HTTPException
import uvicorn
import math

app = FastAPI()

@app.get("/")
async def main():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def main(name: str):
    return {"message": f"Hello {name}"}

@app.get("/add/{num1}/{num2}")
async def main(num1: int, num2: int):
    answer = num1 + num2
    return {"message": f"Sum = {answer}"}

@app.get("/sub/{num1}/{num2}")
async def main(num1: int, num2: int):
    answer = num1 - num2
    return {"message": f"Difference = {answer}"}

@app.get("/mul/{num1}/{num2}")
async def main(num1: int, num2: int):
    answer = num1 * num2
    return {"message": f"Product = {answer}"}

@app.get("/div/{num1}/{num2}")
async def main(num1: int, num2: int):
    if num2 == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")
    answer = num1 / num2
    return {"message": f"Quotient = {answer}"}

@app.get("/mod/{num1}/{num2}")
async def main(num1: int, num2: int):
    if num2 == 0:
        raise HTTPException(status_code=400, detail="Modulus by zero is not allowed")
    answer = num1 % num2
    return {"message": f"Modulus = {answer}"}

@app.get("/exp/{num1}/{num2}")
async def main(num1: int, num2: int):
    answer = math.pow(num1, num2)
    return {"message": f"Exponentiation = {answer}"}