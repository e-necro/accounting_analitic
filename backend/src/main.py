from typing import Dict

from fastapi import FastAPI, Request, Response, status
from fastapi.middleware.cors import CORSMiddleware
import json
from pydantic import BaseModel
from mysql.connector import Error

from .MysqlConnect import MysqlConnect

from .lib.checker import  *

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# connection = MysqlConnect().connectDb

@app.get("/")
async def home():
  try:
    connection = MysqlConnect.connectDb()  
    mycursor = connection.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM auto")
    res = mycursor.fetchall()
    connection.close()
    return res
      
  except Error as e:
      return e
  # return "Hello, World!!!!"

class UserReg(BaseModel):
  '''
    {
      email,
      username,
      password
    }
  '''
  user: Dict

@app.post("/register", status_code = 200)
async def register(userData: UserReg, response: Response):
  # TODO: сгенерить токен, добавить юзера и токен к нему, вернуть данные
  res = checkRegister(userData)
  if (res[0] == True):
    #зарегать юзера и вернуть данные и токен
    try:
      connection = MysqlConnect.connectDb()  
      mycursor = connection.cursor(dictionary=True)
      mycursor.execute("SELECT _id FROM users WHERE email = %s", (userData.user['email'],) )
      res = mycursor.fetchall()
      if (len(res) != 0):
        return RequestError(response, {'MySQL', 'User already registered'})

      mycursor.execute(
        'INSERT INTO users (name, email, password) VALUES (%s, %s, %s)',
        (userData.user['username'], userData.user['email'], userData.user['password'])
      )
      connection.commit()
      _id = connection.lastrowid
      connection.close()
      return _id
        
    except Error as e:
        response.status_code = 419  # вывод ошибок, точнее формат сделать нормальным! 
        errors = { 'errors': {
            'MySQL': e #  выдает Object object ... wtf?
          }
        }
        return errors


    userData.user['_id'] = 'userId'
    userData.user["token"] = 'token example'
    return userData
  else:
    # ошибочка
    return RequestError(response, res[1])
    # response.status_code = 419  # вывод ошибок, точнее формат сделать нормальным! 
    # errors = { 'errors': {
    #     res[1]
    #   }
    # }
    # return errors
  #request: Request
  # request.data.user.token = 'token example'

    
  # return await request.json()