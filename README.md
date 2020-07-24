[![Build Status](https://travis-ci.com/cthoms1993/voicetechnologies.svg?branch=master)](https://travis-ci.com/cthoms1993/voicetechnologies)

# Voice Technologies E-commerce project
## Contents:
* [What does the project and what what requirements does it need to fulfill?](#what-does-it-do-and-what-does-it-need-to-fulfill)
* [Functionality](#functionality)
* [User Experience](#user-experience)
    * [User Stories](#user-stories)
    * [Design](#design)
        * [1. Font](#1-font)
        * [2. Color Scheme](#2-color-scheme)
        * [3. Logo](#3-logo)
        * [4. Geometry](#4-geometry)
        * [5. Wireframing & Proposed/Implemented Functionality per Page](#5-wireframing--proposedimplemented-functionality-per-page)
* [Technology Used](#technology-used)
* [Database](#database)
* [Features](#features)
    * [Future Features](#future-features)
    * [Defensive Design](#defensive-design)
* [Testing](#testing)
    * [Found Bugs & Fixes](#found-bugs--fixes)    
* [Deployment](#deployment)
* [Credits](#credits)
    * [Special Thanks & Acknowledgements](#special-thanks--acknowledgements)

***
## What does it do and what does it need to fulfill?
This project was created to fulfill the brief given to me for my milestone 4 full stack development course with the code institute.
This full stack django framework project is the combined use of all the modules i have learned throughout the course.
This E-commerce application will allow users to purchase products from <a href="https://voicetechnology.herokuapp.com/">Voice Technologies</a> a SMB specialising in documentation processes and speech recognition. They will also be able to create comments on blog posts. 
At Administration level the user will be able to create,read,edit and delete aspects of the site such as - products available, staff members, blog posts and manage blog comments. 

###Functionality
This project was made using a django framework and certain database methods, in post production I used  Sqlite, a database management system for local testing.
once i was ready to move my project into production I began using a Postgres database to make sure data stored was now visible in my deployed application.

A combination of the django framework and database management system, allows the user to have full control of records being used - in this case for products, staff and blog posts.they can access these records, and create,edit and delete them all from a sophisticated django powered admin panel.

My project is version controlled using Git and Github, and the live application is deployed Via Heroku.
all variables that require security are stored within an Env.py file and hidden using gitignore. 

This Application uses stripe for processing payments and can be tested using the below details:
* card number: 4242424242424242 (must be 16 digits long)
* Security number(CVV): any 3 digit combination.
* expiry date: any future month and year combination.

##user experience

### User Stories:
Visiting customer:
* As a visiting customer, I want to be abel to view the site from a range of devices ie , desktop, tablet and mobile.
* As a visiting customer, I want to have the ability to view information about the business and who the key members of staff are.
* As a visiting customer, I want to be able to view the products the business sells and check the cost of these items.
* As a visiting customer, I want to have the ability to create an account. 
* As a visiting customer, I want to be able to contact the business to request any further information via the website.
* As a visiting customer, I want to be abel to see the latest news, and case studies from the business. 
* As a visiting customer, I want to be able to add change quantity and delete products in a cart and review this cart before considering purchasing.


Registered customer:
* As a registered customer, i want to be able to login to the site using the details i registered with.
* As a registered customer, I i want to be able to comment on blog posts. 
* as a registered customer, I want to be able to review my cart and be directed to a checkout page to complete my purchase.
* As a registered Customer, I want the ability to log out of the application.

Admin user:
* As an admin user, i want to be abel to have access to the admin panel by logging in with my details. 
* As an admin user, I want to have the ability to update aspects of the web page ie , staff , products and blog posts.
* As an admin user, I want to have control over which blog comments are displayed to avoid spam posts. 

Business Owner:
* As the business owner, I want to make sure the site is readable and flows well so customers can navigate the site easily.
* AS the business owner, I want to make sure customers can easily find view and purchase the procucts that I offer. 

###Design










