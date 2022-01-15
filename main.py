from fastapi import FastAPI
import uvicorn
import datetime
app = FastAPI()


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


if __name__ == "__main__":
    uvicorn.run("main:app")
