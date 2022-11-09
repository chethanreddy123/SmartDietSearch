import model
from fastapi import FastAPI, Request, Query
from fastapi.middleware.cors import CORSMiddleware
import json
from fastapi.encoders import jsonable_encoder
import pandas as pd

app = FastAPI()

data = pd.read_csv("Final_Data.csv")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/getInformation")
async def getInformation(info : Request):

    print(await info.body())

    req_info = await info.json()
    selected = dict(req_info)["SearchedString"].strip()

    Type = dict(req_info)["Type"].strip()

    KeyWords_Math = model.autocomplete.search(word=selected, max_cost=3, size=10)
    
    FinalList = []

    for i in KeyWords_Math:
        word = str(i[0])
        currVal = list(data.loc[data['Food'] == word ][Type])[0]
        FinalList.append((word,currVal))

    if Type != "GoogleTrends":
        FinalList.sort(key = lambda x: x[1])
        

    return {"searched" : FinalList}

