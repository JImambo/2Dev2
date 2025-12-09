""" END POINT AVEC PATH PARAMETER """

from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id : int) : 
    return {
        "user_id" : user_id,
        "message" : "Voici l'utilisateur voulu"
    }