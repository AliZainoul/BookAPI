# BookAPI Project README

The BookAPI project is a RESTful API that allows users to manage a collection of books. It provides endpoints for creating, reading, updating, and deleting books. This README provides an overview of the project and outlines the steps involved in setting up and running the BookAPI.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Project Setup](#project-setup)
3. [Running the Application](#running-the-application)
4. [API Endpoints](#api-endpoints)
5. [Testing the API](#testing-the-api)
6. [Contributing](#contributing)
7. [License](#license)

## Prerequisites
Before setting up the BookAPI, ensure that you have the following prerequisites installed on your system:
- Java Development Kit (JDK) 11 or higher
- PostgreSQL Database
- Apache Maven
- Git

## Project Setup
Follow the steps below to set up the BookAPI project on your local machine:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/AliZainoul/BookAPI.git
   cd BookAPI
   ```

2. **Database Configuration:**
   - Create a PostgreSQL database named `bookdb`.
   - Update the database connection details in the `application.properties` file located at `src/main/resources`.

3. **Build the Project:**
   ```bash
   mvn clean install
   ```

## Running the Application
After successfully setting up the project, you can run the BookAPI using the following command:

```bash
mvn spring-boot:run
```

The application will start on `http://localhost:8080`.

## API Endpoints
The BookAPI provides the following RESTful endpoints for managing books:

1. **Create a Book:**
   - HTTP Method: POST
   - Endpoint: `/api/books`
   - Request Body: JSON object with `title` and `author` fields.

2. **Get All Books:**
   - HTTP Method: GET
   - Endpoint: `/api/books`
   - Response: List of all books in JSON format.

3. **Get Book by ID:**
   - HTTP Method: GET
   - Endpoint: `/api/books/{id}`
   - Response: Book with the specified ID in JSON format.

4. **Update a Book:**
   - HTTP Method: PUT
   - Endpoint: `/api/books/{id}`
   - Request Body: JSON object with updated `title` and/or `author` fields.

5. **Delete a Book:**
   - HTTP Method: DELETE
   - Endpoint: `/api/books/{id}`

## Testing the API
To test the API, you can use the provided Python script `curlTest.py`. Before running the script, make sure you have Python and the required libraries (requests and faker) installed. You can install the dependencies using `pip`:

```bash
pip install requests faker
```

After installing the dependencies, run the script:

```bash
python curlTest.py
```

The script will create random books, perform various API operations, and display the results.

## Contributing
Contributions to the BookAPI project are welcome! If you find any issues or want to add new features, feel free to open an issue or submit a pull request. Please follow the existing code style and include appropriate tests for new functionalities.

## License
The BookAPI project is open-source and distributed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code as per the terms of the license.

---
Congratulations! You've successfully set up the BookAPI project and learned how to run the application, interact with the API endpoints, and contribute to the project. Happy coding!