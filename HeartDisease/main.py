from typing import Union
from fastapi import FastAPI
from ml_model.model_utils import get_result


import sqlite3
from database.db_utils import insert_data, get_all_data

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/heart/")
async def read_item(
        age: str ,
        gender: str,
        cp: str,
        trestbps: str,
        chol: str,
        fbs: str,
        restecg: str,
        thalach: str,
        exang: str ,
        oldpeak: str ,
        slope: str,
        ca: str ,
        thal: str):
    target = int(get_result(int(age), int(gender),	int(cp), float(trestbps), float(chol),	int(fbs), float(restecg), float(thalach), int(exang), float(oldpeak), int(slope), int(ca), int(thal))[0])
    conn = sqlite3.connect('./database/patients.db')
    insert_data(conn, 'patients',
                {'age': age,
                 'gender': gender,
                 'cp': cp,
                 'trestbps': trestbps,
                 'chol': chol,
                 'fbs': fbs,
                 'restecg': restecg,
                 'thalach': thalach,
                 'exang': exang,
                 'oldpeak': oldpeak,
                 'slope': slope,
                 'ca': ca,
                 'thal': thal,
                 'target': target})
    conn.close()
    return target


@app.get("/patients/")
async def get_patients():

    conn = sqlite3.connect('./database/patients.db')
    stts = get_all_data(conn, 'patients')
    conn.close()

    return {"patients": stts}
