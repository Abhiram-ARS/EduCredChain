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

"""def log_data(t,entry):
    typ="IN___- "
    if t==1:
        typ = "OUT__- "
    
    data = typ+" * "
    for i in entry:
        data+= i+":"+entry[i]
    with open("log_ECC.txt",'a') as f:
        f.write(data)"""

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
    print(key, key == "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918")
    if key == "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918":
        report = bk.revoke_certificate(data)
        return (report)
    
    else:
        return{"status":0,
               "Error":"E01",
               "Message": "Invalied Key"}
    


@app.post("/receive")
async def receive_data(request: Request):
    data = await request.json()
    #log_data("0",data)
    
    if data['operation']=="issue":
        value = issue(data['data'],data["issuercode"])
        #log_data(1,value)
        return value
    
    
    elif data['operation']=="fetch":
        value = fetch(data["data"]["certid"])
        #log_data(1,value)
        return value
    
    elif data['operation']=="verify":
        value = verify(data['data'])
        #log_data(1,value)
        return value
    
    elif data['operation']=="revoke":
        value = revoke(data['data'],data["issuercode"])
        #log_data(1,value)
        return value

    return {"message": "Data received successfully"}

if __name__ == "__main__":
    print(  """  
    ╔═╗ ┌┬┐ ┬ ┬  ╔═╗ ┬─┐ ┌─┐ ┌┬┐  ╔═╗ ┬ ┬ ┌─┐ ┬ ┌┐┌
    ║╣   ││ │ │  ║   ├┬┘ ├┤   ││  ║   ├─┤ ├─┤ │ │││
    ╚═╝_─┴┘_└─┘__╚═╝_┴└─_└─┘_─┴┘__╚═╝_┴ ┴_┴ ┴_┴_┘└┘
          
    """)
    uvicorn.run(app, host="0.0.0.0", port=5000)
