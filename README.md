# CRUD Application

This project is a simple CRUD (Create, Read, Update, Delete) application implemented in both Node.js and Python using Express and Flask respectively.

## Python Application

The Python part of the application is built using Flask. Below are the details for setting up and running the Python application.

### Setup Instructions

1. **Install Dependencies**: Navigate to the `python` directory and install the required packages using pip:

   ```
   pip install -r requirements.txt
   ```

2. **Run the Application**: Start the Flask application by executing the following command:

   ```
   python app.py
   ```

3. **Access the API**: The API will be available at `http://localhost:5000`. You can use tools like Postman or curl to interact with the API.

### API Endpoints

- **Create Item**: `POST /items`
- **Read Items**: `GET /items`
- **Update Item**: `PUT /items/<id>`
- **Delete Item**: `DELETE /items/<id>`

### File Structure

- `app.py`: Entry point for the Flask application.
- `models.py`: Contains the data model for the items.
- `routes.py`: Defines the routes for the CRUD operations.
- `requirements.txt`: Lists the dependencies for the Python application.

This README provides a brief overview of the Python application within the CRUD project. For more details on the Node.js application, please refer to the Node.js README file.