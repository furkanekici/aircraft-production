
# Aircraft Production Application

## Table of Contents
1. [Overview](#overview)
2. [Application Requirements](#application-requirements)
3. [Technologies Used](#technologies-used)
4. [Installation](#installation)
5. [Environment Configuration](#environment-configuration)
6. [Running the Application](#running-the-application)
7. [Models Overview](#models-overview)
8. [API Documentation](#api-documentation)
    - [Swagger Integration](#swagger-integration)
9. [Frontend Functionality](#frontend-functionality)
10. [Extra Features](#extra-features)

---

### 1. Overview

The Aircraft Production Application allows teams to manage the production of aircraft by creating, listing, and recycling parts. The application is built using Django and PostgreSQL, and features a REST API to enable team-based management of parts and assembly of aircraft.

---

### 2. Application Requirements

- **Parts**: Wing, Fuselage, Tail, Avionics
- **Aircraft**: TB2, TB3, AKINCI, KIZILELMA
- **Teams**: Wing Team, Fuselage Team, Tail Team, Avionics Team, Assembly Team

#### Core Functionality

- Personnel login screen.
- Each personnel can belong to one or more teams.
- Teams can create, list, update, and delete their respective parts.
- The Assembly Team can combine parts to assemble an aircraft.
- Aircraft-specific parts (e.g., a TB2 wing cannot be used for a TB3).
- Warnings when parts are missing for aircraft assembly.
- Once used in an aircraft, parts are marked as used or removed from stock.

---

### 3. Technologies Used

- **Backend**: Django (Python)
- **Database**: PostgreSQL
- **API**: Django Rest Framework (DRF)
- **API Documentation**: Swagger (via DRF-YASG)
- **Deployment**: Docker
- **Frontend**: Django Templates

---

### 4. Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/furkanekici/aircraft-production.git
   ```

2. **Set up a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Create a `.env` file** at the root of your project:
   ```bash
   # Django environment variables
   DEBUG=1
   SECRET_KEY=secret_key
   DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0

   # PostgreSQL database configuration
   DB_NAME=db_name
   DB_USER=db_user_name
   DB_PASSWORD=db_password
   DB_HOST=db
   DB_PORT=5432

   # PostgreSQL superuser password (for container initialization)
   POSTGRES_PASSWORD=db_password
   ```

4. **Build and run the app using Docker**:
   ```bash
   docker compose up -d --build
   ```

5. **Create a superuser** for accessing the admin panel:
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

---

### 7. Models Overview

#### **Aircraft**
- `aircraft_type`: CharField (choices: TB2, TB3, AKINCI, KIZILELMA)
- `wing`: OneToOneField (related to Part)
- `fuselage`: OneToOneField (related to Part)
- `tail`: OneToOneField (related to Part)
- `avionics`: OneToOneField (related to Part)
- `assembled`: BooleanField
- `created_at`: DateTimeField

#### **Part**
- `part_type`: CharField (choices: wing, fuselage, tail, avionics)
- `aircraft_type`: ForeignKey (related to Aircraft)
- `team`: ForeignKey (related to Team)
- `created_at`: DateTimeField

#### **Team**
- `team_type`: CharField (choices: Wing Team, Fuselage Team, etc.)
- `personnel`: ManyToManyField (related to Personnel)

---

### 8. API Documentation

This application provides a REST API for interacting with the parts, teams, and aircrafts.

#### **Swagger Integration**

The Swagger UI provides interactive API documentation, making it easy to test API endpoints.

- **Swagger UI** is available at:
  ```
  http://127.0.0.1:8000/swagger/
  ```

This automatically generates API documentation for your models and DRF views. You can interact with the API directly through the Swagger UI.

---

### 9. Frontend Functionality

- **Login**: Personnel can log in via the `/login/` page.
- **Part Creation**: Teams can create new parts based on their responsibilities.
- **Aircraft Assembly**: The Assembly Team can assemble an aircraft by selecting parts via `/aircrafts/assemble/`.

---

### 10. Extra Features

- **Swagger Documentation**: Available at `/swagger/` for exploring API functionality.
- **Docker**: Application can be containerized using Docker.
- **Unit Tests**: Basic unit tests included for models and views.
