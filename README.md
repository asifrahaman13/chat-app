# chat-bot

This is a full stack chat bot application like chat GPT with enhanced capability to give you results based on read time data. You can ask current affairs questions along with the general question. It has also in built memory.


![alt text](<Screenshot from 2024-02-15 22-30-50.png>)

## How to run the application:

First, clone the repository

```
git clone https://github.com/asifrahaman13/chat-app.git
```
Next, open the terminal and enter into the backend folder. 

```
cd backend/
```
Next, create a virtual environment. 

```
virualenv venv
```

Activate the  virtual environment. The following code works for UNIX based system( Linux and Max OS)

```
source venv/bin/activate
```

Install all the dependencies.

```
pip install -r requirements.txt
```

Change the name of .env.example to .env and enter the env variables.

Next, run the backend server.

```
uvicorn main:app --reload
```
Now in another terminal open the front end.

```
cd frontend/
```

Install the dependencies

```
yarn install
```
Change the name of .env.example to .env and enter the env variables.

Start your development server

```
yarn start
```

