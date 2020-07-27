[![Build Status](https://travis-ci.com/cthoms1993/voicetechnologies.svg?branch=master)](https://travis-ci.com/cthoms1993/voicetechnologies)

# Voice Technologies E-commerce project
## Contents:
* [What does the project and what what requirements does it need to fulfill?](#what-does-it-do-and-what-does-it-need-to-fulfill)
* [Functionality](#functionality)
* [User Experience](#user-experience)
    * [User Stories](#user-stories)
    * [Design](#design)
        * [1. Font](#font)
        * [2. Color Scheme](#colour-scheme)
        * [3. Logo](#logo)
        * [5. Wireframing & site functionality per Page](#wireframes)
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
the Logo and imagery (Example Below) through out the site was supplied by my CEO at voice technologies, using these as guides it allowed me to pinpoint the exact colour scheme for the site, To do this I used <a href="https://chrome.google.com/webstore/detail/eye-dropper/hmdcmlfkchdmnmnmheododdhjedfccka?hl=en">Eye dropper</a> which is a google tool for picking colours from images and websites.

<p>
<img src="https://ms4ecommerce.s3.eu-west-2.amazonaws.com/media/images/VTheader.png" alt="Voice tech logo">
</p>

#### Wireframes 

* Base template:

The base template contains the components that are consistent across all pages of the site.
These are the navigation bar and the footer. the navigation bar as you will see from thew following wireframes.
the navigation bar has 5 standard links to the left - home, about us, products,store and blog. on the right the cart icon is always available. 
if the user isn't logged in they will see navlinks for "register" and "log in".
if they have logged in they will see an icon for "log out" and a piece of navbar text to say they have logged in as their chosen username.

The footer is a contrasting colour from the navbar to highlight the social icons contact us buttons.

* Home page:

This is our primary landing page and the first thing the customer see's. the main image presented (depending on screen size)
will present the company logo, below that is a simple three card design to navigate the user to aspects of the site - about us, products, and blog. 

 <details>
   <summary>Home (Index) Template Wireframe</summary>

   <p>
      <img height="350" src="https://github.com/cthoms1993/voicetechnologies/blob/master/staticfiles/static/Wireframes/homepage%20-mobile-view%20.png" alt="Home (Index) template mobile wireframe">
   </p>

   <p>
      <img height="350" src="https://github.com/cthoms1993/voicetechnologies/blob/master/staticfiles/static/Wireframes/homepage%20-%20tablet%20-desktop%20.png" alt="Home (Index) template tablet-desktop wireframe">
   </p>
   </details>

***

* About us page:

The about us page gives an overview of the business, its ethos and what it does.
below this description is a section for meeting some of the staff which gives the user a feel or the type of people the company employs.
This is pulled from the staff application and managed via the admin panel. 

<details>
   <summary>About us Template Wireframe</summary>

   <p>
      <img height="350" src="https://github.com/cthoms1993/voicetechnologies/blob/master/staticfiles/static/Wireframes/about%20us%20-%20mobile-view.png" alt="about us  template mobile wireframe">
   </p>

   <p>
      <img height="350" src="https://github.com/cthoms1993/voicetechnologies/blob/master/staticfiles/static/Wireframes/about%20us%20-%20tablet_desktop.png" alt="about us template tablet-desktop wireframe">
   </p>
   </details>

***

* Store page:

This page as the title suggests is the main store page fro the site.
This page allows users to view the products on offer, check the costs and add a quantity of there choosing the cart. 
the products on this page are pulled from the products application.these are managed directly from the admin panel and are shown here.

<details>
<summary>Store Template Wireframe</summary>
 <p>
      <img height="350" src="https://github.com/cthoms1993/voicetechnologies/blob/master/staticfiles/static/Wireframes/Store-mobile-view.png" alt="cart template mobile wireframe">
 </p>

   <p>
      <img height="350" src="https://github.com/cthoms1993/voicetechnologies/blob/master/staticfiles/static/Wireframes/store-tablet-desktop.png" alt="cart template tablet-desktop wireframe">
   </p>
   </details>

***

* Product pages

These pages give a description and more in depth look at the products the business sells, and some key points on the product. 
each product page then has a call to action button at the bottom directing the user to the store to purchase the product. 

<details>
<summary>Products Template Wireframe</summary>
 <p>
      <img height="350" src="https://github.com/cthoms1993/voicetechnologies/blob/master/staticfiles/static/Wireframes/product-mobile.png" alt="product template mobile wireframe">
 </p>

   <p>
      <img height="350" src="https://github.com/cthoms1993/voicetechnologies/blob/master/staticfiles/static/Wireframes/products-tablet-desktop%20(1).png" alt="product template tablet-desktop wireframe">
   </p>
   </details>

***

* Blog/Blog detail pages

 blog page: This page is used to display a simplified version of the blog posts uploaded by the admin via the admin panel and pulled from the blog application. 
 using bootstrap cards to display each post, with a picture attached to the post, a condensed summary of the post, post tile and published date. 
 each card will have a call to action on it allowing the user to read the full post on a separate page.
 
 Blog detail page:
 Once the user clicks the call to action button on the simplified post, they are redirected to the full post where they can see the full article, read comments left on the post and add their own comments if they are a registered user and have logged in.
 
 
 <details>
<summary>Blog Template Wireframe</summary>
 <p>
      <img height="350" src="https://github.com/cthoms1993/voicetechnologies/blob/master/staticfiles/static/Wireframes/Blog-tablet-desktop.png" alt="blog template tablet-desktop wireframe">
 </p>

   <p>
      <img height="350" src="https://github.com/cthoms1993/voicetechnologies/blob/master/staticfiles/static/Wireframes/blog%20-%20mobile.png" alt="blog template mobile wireframe">
   </p>
    <p>
      <img height="350" src="https://github.com/cthoms1993/voicetechnologies/blob/master/staticfiles/static/Wireframes/Blog-detail-tablet-desktop.png" alt="blog template tablet-desktop wireframe">
    </p>

   <p>
      <img height="350" src="https://github.com/cthoms1993/voicetechnologies/blob/master/staticfiles/static/Wireframes/blog-detail-mobile.png" alt="blog template mobile wireframe">
   </p>
   </details>

***
 
 
* Cart page

This page is used to display the items and the quantity of each item selected from the store page.
if the cart is empty a short message will appear to let the user know that the cart is empty and a call to action button ti visit the store to select items. 
if items are selected from the store the cart will show that item, and give a total costing of all the items selected, there will also be a display beside the cart image inthe navigation bar to show the quantity of items in thr cart. #

The cart page contains a table to show the items in it, and two call to action buttons, one to return to store to continue shopping and another to checkout which will redirect the user to the checkout template to complete there purchase.

<details>
<summary>Cart Template Wireframe</summary>
 <p>
      <img height="350" src="https://github.com/cthoms1993/voicetechnologies/blob/master/staticfiles/static/Wireframes/cart-%20tablet-desktop.png" alt="store template tablet-desktop wireframe">
 </p>

   <p>
      <img height="350" src="https://github.com/cthoms1993/voicetechnologies/blob/master/staticfiles/static/Wireframes/cart-mobile.png" alt="store template mobile wireframe">
   </p>
  </details>

***

* Checkout Page

The checkout page is only accessible to logged in users and from the cart page if the cart has items in it. , when a user selects checkout on the cart page, if they are not logged in they will be redirected to the log in page with a message stating you must be logged in to make purchases. 
The page will again show a table with the products selected by the user and added to the cart. It was also contain two django forms. one for contact details and another for payment details. 
once the user has correctly filled in the forms the user must hit submit payment to complete the process. if this is successful they will be redirected to a completion page stating there purchase was successful.this page will contain a call to action button to return to home screen. 
If the forms are filled in incorrectly Eg - card number is incorrect , the user will receive a flash message warning them there has been an error. 

<details>
<summary>Checkout Template Wireframe</summary>
 <p>
      <img height="350" src="https://github.com/cthoms1993/voicetechnologies/blob/master/staticfiles/static/Wireframes/checkout%20-%20tablet-desktop.png" alt="checkout template tablet-desktop wireframe">
 </p>

   <p>
      <img height="350" src="https://github.com/cthoms1993/voicetechnologies/blob/master/staticfiles/static/Wireframes/checkout%20-%20mobile%20.png" alt="checkout template mobile wireframe">
   </p>
  </details>

***
 
* login/register pages

The login/register pages are both fairly straight forward.they both simple have the page title, and a card centre page containing either the log in form or registration form.
These are both produced via django forms. the login form takes two input - username and password which the user would ave created in the registration form.
The login form then searches the pool of created users in the postgres database to match against these, if tey are found the user is logged in, if the detail are incorrect an error message will appear. 

The registration form has a similar style with more fields to complete, again the users details will be checked against the postgres database to make sure the data is not already present, if this is the case then an error message will display beneth the input that has incorrect or duplicate information. 

Both pages contain links to the opposite pages for defensive design, if user selects the login page instead of register they will have the option to navigate via a call to action button to navigate to the register page and vise versa. 

<details>
<summary>Login/Logout Template Wireframe</summary>
 <p>
      <img height="350" src="https://github.com/cthoms1993/voicetechnologies/blob/master/staticfiles/static/Wireframes/login-tablet-desktop.png" alt="login template tablet-desktop wireframe">
 </p>

   <p>
      <img height="350" src="https://github.com/cthoms1993/voicetechnologies/blob/master/staticfiles/static/Wireframes/login-mobile%20.png" alt="login template mobile wireframe">
   </p>
   <p>
      <img height="350" src="https://github.com/cthoms1993/voicetechnologies/blob/master/staticfiles/static/Wireframes/register-desktop-mobile.png" alt="logout template tablet-desktop wireframe">
 </p>

   <p>
      <img height="350" src="https://github.com/cthoms1993/voicetechnologies/blob/master/staticfiles/static/Wireframes/register-mobile.png" alt="logout template mobile wireframe">
   </p>
  </details>

***



















