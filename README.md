# Project Name

Brief description of your project.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
  - [Node API](#node-api)
  - [Django App](#django-app)
- [Usage](#usage)


## Introduction

Provide a brief introduction to your project.

## Prerequisites

List any prerequisites or dependencies needed to run your project.

## Setup

Explain how to set up the project. Divide this section into subsections for each part of your project (e.g., Node API and Django App).

### Node API

1. Navigate to the `service_api` directory.
2. Install dependencies: `npm install`
3. Start the API: `npm start`
4. The API should be accessible at [http://localhost:3000](http://localhost:3000)

### Django App

1. Navigate to the `billing` directory.
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Apply migrations: `python manage.py migrate`
6. Run the development server: `python manage.py runserver`
7. The Django app should be accessible at [http://localhost:8000](http://localhost:8000)

## Usage

The serivce api generates random user usage & the django app calls the api, sorts and stores the data. It also does bill 
calculation but that isn't currently displayed in the admin userportal.

