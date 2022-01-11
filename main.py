from fastapi import FastAPI
import uvicorn
import datetime
app = FastAPI()


@app.get("/")
def message():
    return {"message": "This is a test with Heraku service API"}

@app.get("/now")
def now():
    now = datetime.datetime.now()
    now = now.strftime("Today %d.%m.%Y - now %H:%M")
    return {"Time":now}



if __name__ == "__main__":
    uvicorn.run("main:app")