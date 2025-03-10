# Software Requirements Specification (SRS) - Task Tracker

## 1. Introduction

### 1.1 Purpose

Task Tracker is a web application to help users manage tasks efficiently with secure access and activity tracking.

### 1.2 Scope

The app allows users to register/login, create/edit/delete tasks, set priorities, and view activity logs. It’s built with Django and Bootstrap for personal use.

### 1.3 Definitions

- Task: A unit of work with title, description, due date, and priority.
- User: Registered individual with an email and password.

## 2. Overall Description

### 2.1 System Features

- User authentication (login/register).
- Task CRUD operations.
- Activity tracking (create/update/delete logs).
- Responsive web interface.

### 2.2 User Classes

- Registered Users: Manage their tasks after logging in.

### 2.3 Operating Environment

- Backend: Django 5.1.6, Python 3.13.1.
- Frontend: Bootstrap 5.3.3.
- Database: SQLite (development).

## 3. Specific Requirements

### 3.1 Functional Requirements

- R1: Users can log in with email and password.
- R2: Users can add tasks with title, description, due date, and priority.
- R3: Users can view tasks sorted by due date.
- R4: Users can edit or delete tasks.
- R5: Users can set task priority (High/Medium/Low).
- R6: System logs task activities.

### 3.2 Non-Functional Requirements

- R7: Authentication must be secure (password hashing).
- R8: UI must be responsive across devices.

### 3.3 Interface Requirements

- Web-based UI with navbar, task cards, and activity section.

## 4. Supporting Diagrams

### 4.1 Use Case Diagram
