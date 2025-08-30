Okay, I'll update and fix the `README.md` file for you. I've corrected the `curl` command in the "How to Test" section to reflect the actual endpoint and the required data fields you discovered.

-----

# RandomAPI: The Modern Dockerized API Project 🚀

RandomAPI is a robust, production-ready template for building and deploying APIs with a modern, containerized architecture. This project provides a complete setup using Docker Compose, integrating FastAPI for a high-performance Python API and MongoDB for a powerful NoSQL database.

The focus is on simplicity and scalability, ensuring your application is ready to run in any environment with a single command.

-----

### ✨ Features

  * **Dockerized Stack**: Uses `docker-compose` to manage both the FastAPI application and the MongoDB database.
  * **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.
  * **MongoDB**: A flexible and scalable NoSQL database, ideal for handling a variety of data structures.
  * **Auto-reloading**: The FastAPI server automatically reloads on code changes, speeding up development.
  * **API Documentation**: Automatic interactive API documentation (Swagger UI) available at `/docs`.

-----

### 🚀 Getting Started

These instructions will get a copy of the project up and running on your local machine.

#### 1\. Clone the repository

```bash
git clone https://github.com/ShayanGolmezerji/RandomAPI.git
cd RandomAPI
```

#### 2\. Prerequisites

Make sure you have Docker and Docker Compose installed on your system.

  * [Install Docker](https://docs.docker.com/get-docker/)
  * [Install Docker Compose](https://docs.docker.com/compose/install/)

#### 3\. Run the Project

This single command will build the Docker images and start both the FastAPI and MongoDB containers, creating a private network for them to communicate on.

```bash
sudo docker-compose up --build
```

-----

### 🧠 How to Test

With the containers running, you can test the API and database integration directly.

1.  **Open API Docs**: Navigate to the interactive API documentation at `http://localhost:8000/docs`. Here you can see all available endpoints and test them directly from your browser.

2.  **Test a `POST` Request (Database Interaction)**: Use `curl` to send a request to your API's `/data` endpoint. This will insert a new entry into the MongoDB database. Make sure to include the required fields: `user_id`, `event_type`, and `value`.

    ```bash
    curl -X POST "http://localhost:8000/data" -H "Content-Type: application/json" -d '{"user_id": "test_user", "event_type": "page_view", "value": 1}'
    ```

3.  **Verify the Data**: After the `POST` request, send a `GET` request to the same endpoint to retrieve all data from the database.

    ```bash
    curl -X GET "http://localhost:8000/data"
    ```

    You should see a JSON response containing the data you just sent.

-----

### 📜 License

This project is licensed under the [DON'T BE A DICK PUBLIC LICENSE](https://github.com/ShayanGolmezerji/RandomAPI/blob/main/LICENSE.md).

-----

### 👨‍💻 Author

Made with ❤️ by [Shayan Golmezerji](https://github.com/shayangolmezerji)
