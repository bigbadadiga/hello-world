from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Calculator API", version="0.1.0")


class CalculationRequest(BaseModel):
    a: float
    b: float
    op: str  # one of: "+", "-", "*", "/"


class CalculationResponse(BaseModel):
    a: float
    b: float
    op: str
    result: float


def perform_calculation(a: float, b: float, op: str) -> float:
    """Pure calculation helper used by the API and tests."""
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b

    raise ValueError(f"Unsupported operation: {op!r}. Use one of '+', '-', '*', '/'.")


@app.get("/")
def read_root() -> dict:
    return {"message": "Calculator API is running. POST to /calculate."}


@app.post("/calculate", response_model=CalculationResponse)
def calculate(request: CalculationRequest) -> CalculationResponse:
    try:
        result = perform_calculation(request.a, request.b, request.op)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))

    return CalculationResponse(a=request.a, b=request.b, op=request.op, result=result)

