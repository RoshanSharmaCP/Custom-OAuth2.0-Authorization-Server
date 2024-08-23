# Custom OAuth2.0 Authorization Server
<img width="561" alt="Screenshot 2024-08-23 at 8 19 34 PM" src="https://github.com/user-attachments/assets/e11f4c7f-5fd2-4a29-a5ca-104eae01fb41">



This project is a custom OAuth2.0 authorization server built using Python, FastAPI, SQLAlchemy, JWT, Docker. The server provides user registration, client registration, authorization code generation, access token issuance, and protected resource access.

## Features

- **User Registration**: Allows new users to sign up.
- **Client Registration**: Allows OAuth clients to register with redirect URIs.
- **Authorization Endpoint**: Generates authorization codes for clients after user authorization.
- **Token Endpoint**: Issues JWT access tokens in exchange for valid authorization codes.
- **Protected Resource Access**: Demonstrates accessing a user's protected resources using a valid access token.

## Prerequisites

- Docker and Docker Compose
- Python 3.9 or higher (for local development)

