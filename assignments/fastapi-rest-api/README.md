# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a beginner-friendly REST API with FastAPI. Students will learn how to define routes, use path and query parameters, validate request data, and manage simple in-memory records.

## 📝 Tasks

### 🛠️ Create the API Skeleton

#### Description
Set up a FastAPI application with a root endpoint and a simple resource endpoint.

#### Requirements
Completed program should:

- Create a `FastAPI` app instance
- Return a welcome message from the root route (`/`)
- Add a `GET` endpoint for a resource collection such as books, tasks, or products


### 🛠️ Implement CRUD Endpoints

#### Description
Add routes that let users create, read, update, and delete items stored in memory.

#### Requirements
Completed program should:

- Support `GET` requests to list all items
- Support `POST` requests to create a new item
- Support `PUT` or `PATCH` requests to update an existing item
- Support `DELETE` requests to remove an item
- Use path parameters to identify a specific item


### 🛠️ Add Validation and Error Handling

#### Description
Use FastAPI request models and response handling to make the API safer and easier to use.

#### Requirements
Completed program should:

- Define a Pydantic model for incoming request data
- Validate required fields before creating or updating an item
- Return a clear error when an item is not found
- Keep the API responses consistent and readable