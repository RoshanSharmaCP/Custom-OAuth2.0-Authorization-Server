# Custom OAuth2.0 Authentication Server

## Overview

This project is a custom OAuth2.0 authentication server built using Python, FastAPI, SQLAlchemy, Redis, Docker, and JWT (JSON Web Tokens) for token management. It provides an OAuth2.0 compliant authentication mechanism, allowing clients to securely obtain access tokens to interact with protected resources.

### Key Features
- **OAuth2.0 Protocol**: Supports various OAuth2.0 grant types, including Authorization Code and Client Credentials.
- **JWT Tokens**: Uses JWT for secure, stateless authentication.
- **Third-Party Client Registration**: Enables the registration of third-party clients that can request access tokens.
- **User Authentication**: Allows users to authenticate and obtain access tokens via the OAuth2.0 flow.
- **Redis Integration**: Leverages Redis for token storage and session management.
- **Dockerized**: The entire application is containerized using Docker, making it easy to deploy and run in any environment.

## Use Case

This OAuth2.0 server can be integrated into any system that requires secure user authentication and authorization. For example, a web application could use this server to handle user login, then issue JWT tokens that clients can use to access protected APIs.

### Example Flow

1. **Client Registration**: 
   - A third-party application (client) registers with the OAuth2.0 server to receive a `client_id` and `client_secret`.

2. **User Authentication**: 
   - The user authenticates with the server, typically through a login page.

3. **Authorization Code Grant (Example)**:
   - The user is redirected to the OAuth2.0 server to approve the third-party application.
   - If approved, the OAuth2.0 server issues an authorization code to the client.
   - The client then exchanges the authorization code for an access token.

4. **Access Protected Resources**:
   - The client uses the access token to authenticate requests to protected resources on behalf of the user.

## Running the Application

### Prerequisites

- **Docker**: Ensure Docker is installed on your system.
- **Docker Compose**: Make sure Docker Compose is installed.

### Steps to Run

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/oauth2-server.git
   cd oauth2-server
2. **Build the Docker image**

    ```bash
    docker-compose build
3. **Run the Application**

    ```bash
    docker-compose up

## Example Request
1. **Register a Client**:

    ```bash
    curl -X POST http://localhost:8000/clients/register -d '{"client_name": "example_client"}'

2. **Obtain Authorization Code**:

    ```bash
    http://localhost:8000/auth?client_id=your_client_id&response_type=code&redirect_uri=http://localhost:8000/callback

3. **Exchange Authorization Code for Access Token**:

    ```bash
    curl -X POST http://localhost:8000/token -d 'client_id=your_client_id&client_secret=your_client_secret&code=your_authorization_code&grant_type=authorization_code'


4. **Access Protected Resources**:

    ```bash
    curl -H "Authorization: Bearer your_access_token" http://localhost:8000/protected-resource


**Stopping the Application**

    docker-compose down

