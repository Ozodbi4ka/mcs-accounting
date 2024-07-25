# MCS Accounting

## Overview
MCS Accounting is a robust accounting system built using modern Python web development frameworks and design principles. The project leverages **FastAPI** for the web framework, **SQLAlchemy** for database interaction, **Alembic** for migrations, and follows **Domain-Driven Design (DDD)** and **Clean Architecture (CA)** principles for a well-organized codebase.

## Features
- **FastAPI:** High-performance web framework for building APIs.
- **SQLAlchemy:** SQL toolkit and ORM for database interactions.
- **Alembic:** Database migrations for schema management.
- **DDD and CA:** Organized code with a clear separation of concerns.

## Getting Started

### Prerequisites
- Docker
- Docker Compose
- Python 3.x

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/OzodbekPyDev/mcs-accounting.git
   cd mcs-accounting
   ```

2. **Set up the environment:**
   - Create a `.env` file for environment variables based on `.env-test`.

3. **Build and run the Docker container:**
   ```bash
   docker-compose up --build
   ```

### Usage
Access the application via `http://localhost:8000`.

### API Overview
- **/api/v1/users:** Manage users, authentication, and authorization.
- **/api/v1/transactions:** Handle financial transactions and records.
- **/api/v1/reports:** Generate accounting reports.

### Development and Testing
- **Linting and Formatting:** Uses Flake8 for linting. Run `flake8` to check code style.
- **Testing:** To run tests, use the following command:
  ```bash
  pytest
  ```

## Contributing
Contributions are welcome! Please open issues or submit pull requests.

## License
This project is licensed under the MIT License.
```

To use this, create a `README.md` file in your project's root directory, paste the above content, save the file, and then commit and push it to your repository. This will create a comprehensive README for your project.
