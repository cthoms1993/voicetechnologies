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

### Functionality
This project was made using a django framework and certain database methods, in post production I used  Sqlite, a database management system for local testing.
once i was ready to move my project into production I began using a Postgres database to make sure data stored was now visible in my deployed application.

A combination of the django framework and database management system, allows the user to have full control of records being used - in this case for products, staff and blog posts.they can access these records, and create,edit and delete them all from a sophisticated django powered admin panel.

My project is version controlled using Git and Github, and the live application is deployed Via Heroku.
all variables that require security are stored within an Env.py file and hidden using gitignore. 

This Application uses stripe for processing payments and can be tested using the below details:
* card number: 4242424242424242 (must be 16 digits long)
* Security number(CVV): any 3 digit combination.
* expiry date: any future month and year combination.

## user experience

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
* AS the business owner, I want to make sure customers can easily find view and purchase the products that I offer. 

### Design
Designing this project was fun for me as the application is modelled on my current employer, so getting the opportunity to take there current site and try and do something completely different was challenging and exciting. 
I was keen to try and use the idea of minimalism through out the site and using only a few bold colours really bring the site to life. 
This was made easier since the two primary colours of our logo are purple and orange, so i decided to use these bold colours to really make the site eye catching. 

#### font
Sticking with the idea of minimalism the site has one font through out of <a href="https://fonts.google.com/specimen/Lato">Lato</a> which compliments the style of the branding logo nicely. 

#### Colour Scheme
As I have mentioned this project was modelled on my current employer Voice technologies.they have an existing live site already which has a neutral white background, using flashes of the orange and purple branding colours as highlights. 
since the original site was plain white in background and uses minimal colour.
I thought I would see how it would look if the site was reversed using the striking purple colour used in the branding as the primary background colour of the site, with orange as the secondary colour with white text and a white and grey image used for the footer and heading backgrounds. 



#### colours used:
* ![#562b5e](https://placehold.it/15/562b5e/000000?text=+)  `#562b5e`- Primary color
* ![#ff8200](https://placehold.it/15/ff8200/000000?text=+) `#ff8200` - Secondary color
* ![#f8f6f6](https://placehold.it/15/f8f6f6/000000?text=+) `#f8f6f6` - Secondary color
* ![#efefee](https://placehold.it/15/efefee/000000?text=+) `#efefee` - Supplementary color
   
The Primary colour of ![#562b5e](https://placehold.it/15/562b5e/000000?text=+) `#562b5e` is used as the primary background colour for the body of thr site, navigation bar and footer links. 
It is a strikingly bold colour that draws the users eye but has a smotthness to it that makes it calming and easy to view for a long period of time. 

The secondary colour ![#ff8200](https://placehold.it/15/ff8200/000000?text=+) `#ff8200` is ued through out the site to help highlight certain texts and make aspects of the site stand out ie - used for hover feature in navbar and footer. 
It is also used for all the call to actions on the site to stand out for the customer to have a clear idea of where to click. 

#### Logo and imagery 
the Logo and imagery (Examples Below) through out the site was supplied by my CEO at voice technologies, using these as guides it allowed me to pinpoint the exact colour scheme for the site, To do this I used <a href="https://chrome.google.com/webstore/detail/eye-dropper/hmdcmlfkchdmnmnmheododdhjedfccka?hl=en">Eye dropper</a> which is a google tool for picking colours from images and websites.
<p>
<img src="https://ms4ecommerce.s3.eu-west-2.amazonaws.com/media/images/voice-technologies_positive_MONO.png" alt="Voice tech logo">
</p>

<p>
<img src="https://ms4ecommerce.s3.eu-west-2.amazonaws.com/media/images/VTheader.png" alt="Voice tech logo">
</p>




















