## README

# Rule Engine with Abstract Syntax Tree (AST)

### Overview

This project consists of a rule engine application that uses SQLite for storing rules and Flask for providing a web interface. The rule engine allows users to create, modify, and evaluate rules based on input data.

### Design Choices

- **SQLite Database**: Chosen for simplicity and ease of use, suitable for lightweight applications.
- **Flask Web Framework**: Provides a simple interface for interacting with the rule engine via a web browser.
- **Rule Engine**: Implements a basic Abstract Syntax Tree (AST) to parse and evaluate rules.

### Setup Instructions

#### Prerequisites

- Python 3.x
- SQLite
- Flask

#### Dependencies

Install the required Python packages using pip:

```bash
pip install flask
```

#### Database Setup

1. Ensure the directory `/Users/yanalaraghuvamshireddy/Downloads` exists or modify the path in `setup_database.py` as needed.
2. Run `setup_database.py` to create the SQLite database and initialize the `rules` table with sample data:

```bash
python setup_database.py
```

#### Running the Application

1. Start the Flask application by running `app.py`:

```bash
python app.py
```

2. Open your web browser and navigate to `http://127.0.0.1:5000` to access the rule engine interface.

### Usage Instructions

- **Create Rule**: Enter a rule in the text input field and submit to add it to the database.
- **Evaluate Rule**: Provide data in JSON format to evaluate against the combined rules.

### Docker Setup (Optional)

To run the application in a Docker container, follow these steps:

1. **Dockerfile**: Create a Dockerfile with the following content:

    ```dockerfile
    FROM python:3.x-slim
    WORKDIR /app
    COPY . .
    RUN pip install flask
    CMD ["python", "app.py"]
    ```

2. **Build Docker Image**:

    ```bash
    docker build -t rule-engine .
    ```

3. **Run Docker Container**:

    ```bash
    docker run -p 5000:5000 rule-engine
    ```

### Additional Notes

- **Security Warning**: The current implementation uses `eval()` for parsing JSON data, which is insecure. Replace it with `json.loads()` in production.
- **Debugging**: The Flask app runs in debug mode for development purposes. Disable it in production by setting `debug=False` in `app.run()`.
