
from fastapi import FastAPI

usersname = ["pepe","manolo"]
app = FastAPI()
@app.post("/api/users", response_model = dict)
async def add_user( ):
    new_user = "juani"
    usersname.append(new_user)
    id = range(len(usersname))
    user_dict = dict(zip(id, usersname))
    return user_dict

@app.get("/api/users/{id}", response_model = dict)
async def get_user(id: int):
    user_id = range(len(usersname))
    user_dict = dict(zip(user_id, usersname))

    if id in user_dict:
        return {id: user_dict[id]}

@app.get("/api/users", response_model = dict)
async def get_user_list():
    id = range(len(usersname))
    user_dict = dict(zip(id, usersname))
    return user_dict

@app.put("/api/users", response_model = dict)
def modify_user(user_id: int, new_name: str):
    id = range(len(usersname))
    user_dict = dict(zip(id, usersname))
    if user_id in user_dict:
        user_dict[user_id] = new_name
        return user_dict
@app.delete("/api/users", response_model = dict)
def delete_user(user_id: int):
    id = range(len(usersname))
    user_dict = dict(zip(id, usersname))
    if user_id in user_dict:
        user_dict.pop(user_id)
        return user_dict