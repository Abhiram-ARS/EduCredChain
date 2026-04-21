"""
Project Title : EduCredChain
Description   : Blockchain-Based Certificate Verification System

File Name     : API_ECC.py
Description   : FastAPI backend server handling certificate issuance, verification, fetching, and revocation via API endpoints

Author(s)     : ABHIRAM_S, AMARNATH MOHAN, MOHAMMED YASEEN

Last Modified : 18-04-2026
"""
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

import BlkChain_ECC


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

bk = BlkChain_ECC.BlkChain_funct()


def issue(data,key):
    if key == "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918":
        report = bk.issue_certificate(data)
        return (report)
    
    else:
        return{"status":0,
               "Error":"E01",
               "Message": "Invalied Key"}
    
def fetch(certid):
    report = bk.fetch_certificate(certid)
    return (report)

def verify(data):    
    report = bk.verify_certificate(data)
    return (report)


def revoke(data,key):    
    print(data)
    print("Key Matching Status :", key == "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918")
    if key == "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918":
        report = bk.revoke_certificate(data)
        return (report)
    
    else:
        return{"status":0,
               "Error":"E01",
               "Message": "Invalied Key"}
    


@app.post("/receive")
async def receive_data(request: Request):
    print('-'*50)
    data = await request.json()
    print("Calling   => ",data)

    if data['operation']=="issue":
        value = issue(data['data'],data["issuercode"])
        print("Returning => ",value)
        return value
    
    
    elif data['operation']=="fetch":
        value = fetch(data["data"]["certid"])
        print("Returning => ",value)
        return value
    
    elif data['operation']=="verify":
        value = verify(data['data'])
        print("Returning => ",value)
        return value
    
    elif data['operation']=="revoke":
        value = revoke(data['data'],data["issuercode"])
        print("Returning => ",value)
        return value
    print('-'*50)
    return {"message": "Data received successfully"}

if __name__ == "__main__":
    print(  """  
    ╔═╗ ┌┬┐ ┬ ┬  ╔═╗ ┬─┐ ┌─┐ ┌┬┐  ╔═╗ ┬ ┬ ┌─┐ ┬ ┌┐┌
    ║╣   ││ │ │  ║   ├┬┘ ├┤   ││  ║   ├─┤ ├─┤ │ │││
    ╚═╝_─┴┘_└─┘__╚═╝_┴└─_└─┘_─┴┘__╚═╝_┴ ┴_┴ ┴_┴_┘└┘
          
    """)
    uvicorn.run(app, host="0.0.0.0", port=5000)
