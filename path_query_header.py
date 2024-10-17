#path_query_header.py
from fastapi import FastAPI, Header
from typing import Optional

app = FastAPI()    # app is instance of fastapi

# Example 1: Path Parameter
@app.get("/numbers/{number1}")
async def read_item(number1: int):
    return {"number1": number1}

# Example 2: Query Parameter (optional)
@app.get("/items/")
        #number 1 is optional with default value 0 and number 2 with default value 10
async def read_items(number1: Optional[int]=0, number2: int = 10):   # when using optional we must use default value 
    return {"number1": number1, "number2": number2}

# Example 3: Header Parameter             Header() = value required
@app.get("/req_headers/")
def req_header_param(number1: str = Header(...)): #... for required value 
    return {"number1": number1}


@app.get("/optional_headers/")
def optional_header_param(number1: str = Header(None)):# None for optional value 
    return {"number1": number1}