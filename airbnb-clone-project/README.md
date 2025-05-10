## Airbnb Clone Project
Overview
The Airbnb Clone project is a full-stack web application that replicates core features of the Airbnb platform. The goal is to understand web development concepts, backend and frontend integration, API design, database modeling, and DevOps practices.
Tech Stack: Django, PostgreSQL, GraphQL, React, Docker, GitHub Actions.

## Team Roles
Backend Developer: Builds and maintains server-side logic, APIs, and database interactions.

Frontend Developer: Creates interactive user interfaces using modern frontend frameworks.

Database Administrator: Designs, maintains, and secures the database.

DevOps Engineer: Implements CI/CD pipelines and manages deployments using tools like Docker and GitHub Actions.

Project Manager: Oversees task distribution, progress tracking, and ensures deadlines are met.

## Technology Stack
Django: Web framework used to build RESTful APIs and manage backend logic.

PostgreSQL: Relational database for storing structured data like user accounts, listings, and bookings.

GraphQL: API query language for flexible and efficient data fetching.

React: Frontend framework used to build responsive UI components.

Docker: Containerizes the application for consistent deployment across environments.

GitHub Actions: Automates workflows like testing, building, and deployment.

## Database Design
Users

Fields: id, name, email, password, role

Relationships: Can create properties, write reviews, and make bookings.

Properties

Fields: id, owner_id, title, description, price

Relationships: Belongs to a user (owner), has many bookings and reviews.

Bookings

Fields: id, user_id, property_id, start_date, end_date

Relationships: Belongs to a user and a property.

Reviews

Fields: id, user_id, property_id, rating, comment

Relationships: Written by a user for a property.

Payments

Fields: id, booking_id, amount, status, transaction_date

Relationships: Linked to a booking.

Feature Breakdown
User Management: Allows users to sign up, log in, update profiles, and authenticate securely.

Property Management: Users can create, edit, and delete listings, upload images, and set prices and availability.

Booking System: Enables users to view listings, book available properties, and manage reservations.

Review System: Users can rate and review properties, helping others make informed decisions.

Payment Integration: Facilitates secure transactions and maintains payment history per booking.

## API Security
Authentication: Ensures only registered users can access protected endpoints via tokens or sessions.

Authorization: Restricts actions based on user roles (e.g., only owners can manage their listings).

Rate Limiting: Prevents abuse by limiting the number of requests per user or IP.

Data Validation: Prevents injection attacks and ensures input data meets required formats.

Why Security Matters:

Protects sensitive user data like login credentials and payment information.

Ensures fair and correct access control.

Enhances trust in the platform by preventing fraudulent or malicious activities.

CI/CD Pipeline
CI/CD (Continuous Integration/Continuous Deployment) automates testing, building, and deploying the app.

Continuous Integration: Automatically runs tests whenever new code is pushed.

Continuous Deployment: Delivers updated code to production seamlessly using automation tools.

 Tools Used:

GitHub Actions: Automates test and deploy workflows.

Docker: Ensures consistent environments across development, staging, and production.

