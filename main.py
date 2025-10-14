
from fastapi import FastAPI

listusers = [{"id":"1",
         "name": "pepe",
              "apellido": "gotera"},
           {"id":"2",
            "name": "manolo",
            "apellido": "vargas"},
             {
                 "id":"3",
                 "name": "maria",
                 "apellido": "barca"
             }]
app = FastAPI()


@app.post("/api/users")
async def add_user():
    listusers.append({"id":"3","name": "pepe"})
    return {"users" : listusers}

@app.get("/api/users/{id}")
async def get_user(id: str):
    for user in listusers:
        if user["id"] == id:
            return user
@app.get("/api/users/")
async def get_users_list():
    return listusers
@app.put("/api/users/{id}")
async def put_update_user(id:str):
    for index,user in enumerate(listusers):
        if user["id"] == id:
            listusers[index].update({"id":"4","name":"manoli","apellido":"garcia"})
            return listusers[index]
@app.patch("/api/users/{id}")
async def update_user(id:str):
    for index,user in enumerate(listusers):
        if user["id"] == id:
            listusers[index].update({"name":"manoli"})
            return listusers[index]

@app.delete("/api/users/{id}")
async def delete_user(id:str):
    for index,user in enumerate(listusers):
        if user["id"] == id:
            del listusers[index]
            return listusers

