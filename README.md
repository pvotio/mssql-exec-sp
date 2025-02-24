# MSSQL Exec SP

MSSQL Exec SP is a lightweight Python application designed to execute stored procedures in Microsoft SQL Server. It provides seamless integration with Azure Active Directory for authentication and supports Docker-based deployments.

## Features

- Executes stored procedures on MSSQL databases.
- Supports Azure Active Directory authentication.
- Dockerized for easy deployment.
- Configurable via environment variables

## Installation


1. Clone the repository:
    ```bash
    git clone https://github.com/pvot-io/mssql-exec-sp.git
    cd mssql-exec-sp
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Set up environment variables:
    Copy `.env.sample` to `.env` and configure values.

4. Run the application:
    ```bash
    python main.py
    ```

## Configuration

This application relies on environment variables for database connection settings. Add the following to your `.env` file:

```bash
MSSQL_SERVER=your-db-server
MSSQL_DATABASE=your-database
MSSQL_USERNAME=your-username
MSSQL_PASSWORD=your-password
SP_NAME=your-stored-procedure
MSSQL_AD_LOGIN=False
```
If MSSQL_AD_LOGIN=True, the application will use Azure Identity for authentication.

## Contributing
- Fork the repository.
- Create a feature branch: git checkout -b feature-branch
- Commit changes: git commit -m "Add new feature"
- Push to the branch: git push origin feature-branch
- Open a Pull Request.
