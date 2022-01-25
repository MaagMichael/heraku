from fastapi import FastAPI, Request
import uvicorn
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles 
from fastapi.responses import HTMLResponse # only for case 2

import datetime
app = FastAPI()

# depending on your working directory of your virtual enviroment ! here "BMIcalcJinJa2"
templates = Jinja2Templates(directory="./templates")
app.mount("/static", StaticFiles(directory="./static"), name="static")

@app.get("/")
def message():
    return {"message": "This is a test with Heraku service API"}

# Get current date and time from Server
@app.get("/now")
def now():
    now = datetime.datetime.now()
    now = now.strftime("Today %d.%m.%Y - now %H:%M")
    return {"Time":now}

# Create BMI calc, request as "/bmicalconly?height=2&weight=77"
@app.get("/bmicalconly")
async def calc_bmi(height: float, weight: float) -> float: 
    bmi = round(weight/ (height*height),2)
    return {"data": "The calculated BMI is: {}".format(bmi)} # no html page rendered as response !

#++++++++++++++++++ HTML response +++++++++++++++++++++++++++++++ request as "/bmicalchtml/2,77"

@app.get("/bmicalchtml/{height},{weight}", response_class=HTMLResponse)
async def calc_bmi(request: Request, height: float, weight: float):
    result = round(weight/ (height*height),2)
    return templates.TemplateResponse("bmi_result.html", {"request": request, "bmi": result})

if __name__ == "__main__":
    uvicorn.run("main:app")