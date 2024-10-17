from fastapi import FastAPI , Header

app = FastAPI()             # app is instance of FastAPI

@app.get("/")               # request method        # if only "/", its root end
def read_root():            
    return {"Hello":"World"}    # return hello world


@app.get("/sum")
def sum_add(num1:int, num2:int):
    add = num1 + num2
    return {"addition":add}


@app.get("/multiplication")
def sum_mult(num1:int, num2:int):
    mult = num1 * num2
    return {"multiplication":mult}


@app.get("/division")
def sum_div(num1:int, num2:int):
    div = num1 / num2
    return {"division":div}


@app.get("/factorial")
def fact(num1:int):
    fact1 = 1
    for i in range(1,num1+1):
        fact1 = fact1 * i
    return {"factorial":fact1}


@app.get("/Pelindrome")
def pel(num1:int):
    orig = num1
    rev = 0
    while num1>0:
        rem = num1 % 10
        rev = rev * 10 + rem
        num1//=10
    if orig == rev:
        return {"Number is Pelindrome"}
    else:
        return {"Number is not a Pelindrome"}
    

@app.get("/fibonacci")
def fibonacci(i:int):
    f1 = 0
    f2 = 1
    list1 = []
    while i>0:
        list1.append(f1)
        f = f1 + f2
        f1 = f2
        f2 = f
        i-=1
    return list1


@app.get("/greetings")
def greetings(name:str):
    return {f"hello {name} how are you doing??"}


# PATH parameters

@app.get("/sum/{num1}/{num2}")
def sum_add(num1:int, num2:int):
    add = num1 + num2
    return {"addition":add}


@app.get("/multiplication/{num1}/{num2}")
def sum_mult(num1:int, num2:int):
    mult = num1 * num2
    return {"multiplication":mult}


@app.get("/division/{num1}/{num2}")
def sum_div(num1:int, num2:int):
    div = num1 / num2
    return {"division":div}


@app.get("/factorial/{num1}")
def fact(num1:int):
    fact1 = 1
    for i in range(1,num1+1):
        fact1 = fact1 * i
    return {"factorial":fact1}


# HEADER parameter

@app.get("/Pelindrome_h")
def pel(num1:int = Header()):
    orig = num1
    rev = 0
    while num1>0:
        rem = num1 % 10
        rev = rev * 10 + rem
        num1//=10
    if orig == rev:
        return {"Number is Pelindrome"}
    else:
        return {"Number is not a Pelindrome"}
    

@app.get("/fibonacci_h")    
def fibonacci(i:int = Header()):
    f1 = 0
    f2 = 1
    list1 = []
    while i>0:
        list1.append(f1)
        f = f1 + f2
        f1 = f2
        f2 = f
        i-=1
    return list1