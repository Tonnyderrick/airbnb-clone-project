Airbnb Clone – Backend

This project is a backend clone of the Airbnb platform, designed to simulate core functionalities such as user authentication, property listings, bookings, and payments. It's built with scalability and modularity in mind, using Django and RESTful API standards.

Project Objectives

Recreate key features of Airbnb for learning and prototyping.

Build a secure, scalable backend for a booking platform.

Support APIs for frontend integration and mobile clients. Key Features

User Management: Register, login, and manage profiles securely.

Property Listings: Create, update, delete, and browse properties.

Booking System: Book stays, cancel, and view history.

Payment Processing: Simulate payments and transaction records.

Reviews: Leave and manage property reviews and ratings.

REST API: Fully documented endpoints with OpenAPI/Swagger.

Team Roles Tonny Derick - Backend developer

Responsibilities:
Design and implement RESTful API endpoints.
Develop business logic for bookings, user management, payments, etc.
Ensure API security, scalability, and performance.
Collaborate closely with frontend and database teams.

## Technology Stack

This project utilizes a modern and scalable technology stack to deliver robust backend functionality and seamless data handling.

### Django
- **Purpose**: Django is a high-level Python web framework used to rapidly build secure and maintainable web applications. In this project, Django serves as the core framework for handling HTTP requests, defining models, managing user sessions, and more.

###  Django REST Framework (DRF)
- **Purpose**: DRF extends Django to make it easier to build RESTful APIs. It handles serialization, authentication, and view logic to enable smooth interaction between the frontend and backend.

###  PostgreSQL
- **Purpose**: A powerful open-source relational database system used to store structured data such as users, property listings, bookings, and reviews.

###  GraphQL
- **Purpose**: GraphQL is used as an alternative to REST for more flexible and efficient data querying. It allows clients to request exactly the data they need in a single API call.

###  Celery
- **Purpose**: Celery is used for handling asynchronous tasks like sending confirmation emails, processing payments, or scheduling background jobs.

###  Redis
- **Purpose**: Redis is used alongside Celery for task queue management and as a cache to improve response times and reduce database load.

###  Docker
- **Purpose**: Docker helps package the application and its dependencies into containers, ensuring consistency across development, testing, and production environments.

###  CI/CD Pipelines (e.g., GitHub Actions)
- **Purpose**: CI/CD automates testing, building, and deployment of the application whenever changes are made, improving developer productivity and software quality.

