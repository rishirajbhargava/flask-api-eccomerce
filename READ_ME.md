## Prerequisites

        Python 3.6+
        Flask
        SQLAlchemy

## Setup

    1.Clone the repository.
    2.cd into the directory.

    3.Create a virtual environment with python3 and activate it by running the following commands:
    ``` 
    python3 -m venv env
    env/Scripts/activate
    ```
    4.Install the dependencies by running the following command:
    ```
    pip install -r requirements.txt
    ```
    5.Run the application by running the following command:
    ```
    python app.py
    ```

    6.Database will automatically created.
   

## API Documentation

### 1. Create a new user

    POST /users
    Request Body
    {
        "name": "John Doe",
        "email": "johndoe@gmailo.com",
    }
    Response
    {
        "id": 1,
        "name": "John Doe",
        "email": "johndoe@gmailo.com",
    }

### 2. Get all users

    GET /users
    Response
    [
      {
        "id": 1,
        "name": "John Doe",
        "email": "johndoe@gmailo.com",
    },

    ]

### 3. Get a user

    GET /users/<id>
    Response
    {
        "id": 1,
        "name": "John Doe",
        "email": "johndoe@gmailo.com",
    }

## 4 Create a order

    POST /orders
    Request Body
    {
        "product_name": "Mobile",
        "quantity": 1,
        "total_price": 1000,
    }
    Response
    {
        "id": 1,
        "user_id": 1,
        "product_name": "Mobile",
        "quantity": 1,
        "total_price": 1000,
         "created_at": "2021-01-01",
    }

## 5 Get all orders

    GET /orders
    Response
    [
        {
            "id": 1,
            "user_id": 1,
            "product_name": "Mobile",
            "quantity": 1,
            "total_price": 1000,
            "created_at": "2021-01-01",
        },
    ]

## 6 Get a order

    GET /orders/<id>
    Response
    {
        "id": 1,
        "user_id": 1,
        "product_name": "Mobile",
        "quantity": 1,
        "total_price": 1000,
        "created_at": "2021-01-01",
    }


