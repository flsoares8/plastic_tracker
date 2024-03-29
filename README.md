# CS50 Final Project

This is our repository for the CS50 course Final Project

## Plastic Tracker

The project's goal is to introduce a way to control your plastic footprint everytime you shop.

### WHY

Striving for a more conscious World, awareness of our footprint is essential. Getting past last century materials is walking in that direction.

### _WHAT_

We are developping a tool to track and regulate plastic consumption. This tool shall register individuals or households granting them a free of charge plastic balance.
In collaboration with shops and retailers, the plastic weight of products included in one shopping transaction is subtracted from the current balance.
For this process to be accurate, every selling item shall be registered in a knowledge base.

### _HOW_

We've decided to create a Web App using Django and a PostGres database.
The idea is the user to interact with a GUI fetching its data or executing some operations that will represent CRUD operations in the DB.

---

## **How to run** 🐍

Running the project from the beggining

1. Create a user postgres if it does not exist
   `createuser -s postgres`

2. Create a DB named plastic_tracker
   `createdb plastic_tracker`

3. Apply the migrations to your DB  
   `python manage.py migrate`  
   You will need to have installed python libraries **django**, **python-dotenv**, **django-materializecss-form** and **psycopg2**

4. Run the webserver  
   `python manage.py runserver`

---

## Description

The application allows two flows:

    - Creating a user & check user details
    - Register a user's shopping list

The user creation takes you to a form where one has to introduce user's data, including a unique identifier (per example, a social number)
It is possible to check the User Details (where the current plastic balance is displayed) through a search by ID.
Each registred client can acces its own page anytime and check the current monthly plastic balance.

There is a shop page that is responsible for registring a client's shopping list.
To register a shopping list, one has to introduce a registered User ID.
A page to register the shopping items is displayed as well as a "payment" button that will sum all the items plastic weight and subtract it from the User's balance.
Each item has a price as well as a plastic weight, which is accumulated with all the monthly shopping and optionally taxed according to a pre-defined table

---

## Possible Future features & developments

- Create a more fair initial plastic balance taking in consideration families
- Define fees for different levels of plastic "debt"

---
