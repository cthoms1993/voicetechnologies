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
        * [3. Logo](#logo-and-imagery)
        * [5. Wireframing & site functionality per Page](#wireframes)
* [Technology Used](#technology-used)
* [Features](#features)
    * [Future Features](#future-features)
* [Testing](#testing)
    * [Bugs & Fixes](#bugs-and-fixes)    
* [Deployment](#deployment)
* [Credits](#credits-and-acknowledgements)

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

* Contact us page

Similar to the login and register pages , the contact us page contains a django form for completing the users details , in which they fill in there contact details, subject and the reason for their enquiry. 
This is then sent to the admin portal under enquires. this then sends an email to the registered admin email address (This is hidden in an env.py for local use and in variables in heroku.)
There is also a map below the form to give the user an idea of where exactly the business is located. 


<details>
<summary>Contact Us Template Wireframe</summary>
  <p>
      <img height="350" src="https://github.com/cthoms1993/voicetechnologies/blob/master/staticfiles/static/Wireframes/contact-tablet-desktop.png" alt="logout template tablet-desktop wireframe">
 </p>

   <p>
      <img height="350" src="https://github.com/cthoms1993/voicetechnologies/blob/master/staticfiles/static/Wireframes/contact-mobile.png" alt="logout template mobile wireframe">
   </p>
  </details>

***

[back to top](# table-of-contents)

## Technology Used

* HTML
* CSS
* javascript
* python

* <a href="https://www.djangoproject.com/">Django</a> - framework used to create the use of models and templates. 
* <a href="https://www.getbootstrap.com/">Bootstrap</a> - used to create the core layout of the project, using the grid system for responsive functionality.
* <a href="https://www.bootswatch.com/">Bootswatch</a> - used in combination with bootstrap for the initial theme and for components of the site. 
* <a href="https://git-scm.com/">Git</a> - plug in installed in pycharm ide for version control. 
* <a href="https://github.com/">Github</a> - Used to create repository for storing project and linking to heroku for project Deployment.
* <a href="https://www.heroku.com/">Heroku</a> - Used to deploy project into production. 
* <a href="https://www.jetbrains.com/pycharm">Pycharm IDE</a> - pycharm was used as my IDE for this project. 

#### Tools


* <a href="https://www.postgresql.org/">PostgreSQL</a> - PostgreSQL is a powerful, open source object-relational database system with over 30 years of active development that has earned it a strong reputation for reliability, feature robustness, and performance.
this was used to host the information from my applications thast required database functionality.
* <a href="http://whitenoise.evans.io/en/stable/">WhiteNoise</a> - WhiteNoise allows your web app to serve its own static files, making it a self-contained unit that can be deployed.
* <a href="http://eye-dropper.kepi.cz/">Eye Dropper (Color Picker)</a> -Eye Dropper is open source extension which allows you to pick colors from web pages, color picker and your personal color history.
* Google Chrome DevTools ~ Used to check responsiveness and fix any styling errors.
* <a href="https://www.lucidchart.com/">Lucid-chart </a> - Used for the creation of wireframes.
* <a href="https://validator.w3.org/">W3C HTML Validator</a> - Used to check my code is valid. 
* <a href="https://autoprefixer.github.io/">Autoprefixer CSS Online</a> ~ Used to check for possible webkits required in the applications stylesheet ensuring Cross-browser support.
* <a href="https://fontawesome.com/icons?d=gallery">Font Awesome </a> - For social icons and other imagery used throughout the site. 
* <a href="https://aws.amazon.com/s3/">Amazon AWS S3 </a> - Used for hosting images relating to staff and products applications connected to database. 
* <a href="https://www.mapbox.com/">Mapbox</a> - used for displaying location map on contact us page, a simpler option compared to using google maps API.

## Features:

My Projects has many key features:


* User Authorisation and authentication
* Stripe Integration to allow for e-commerce functionality.
* A contact form that can be used by all user levels which sends an email to the Administrator of the application, notifying them of a new Contact form submission. 
* a comments section on the blog where authenticated users can post there options and interact with others.

### future features

* edit and delete for users to change there own blog comments.
* a profile section that shows the user their order history.
* password reset functionality. 
* the company have a whole host of 3rd party products they can provide which are not shown here for copyright reasons, but i would hope to add them all in future to provide a fully operational product store.
* one of the products provided is speech recognition I would hope to incorporate this into future versions of the site eg: form completion.


## Testing

Testing was done manually throughout the production of this project, on multiple devices ( Ipads.,Iphones, Microsoft surface, google pixel-2 and desktop. )
This made sure that any bugs on varying screen resolutions where fixed throughout.
code was passed through validators throughout to make sure it was valid and od good quality. 
The Site was tested on most modern browsers to make sure responsiveness and functionality of the site was good across all browsers.

## bugs and fixes

Throughout production and constant testing both locally and via my deployed site on heroku, a few bugs crept up. 

* When checking the responsiveness of the site there was an error with the footer positioning for the store, log in and log out pages only. 
the footer was jumping up on all occasions and leaving negative space at the bottom of the screen, this seemed to be only an issues with screen withs of 1024px and above. 

This was fixed by adding the below css and adding section tags to the mentioned pages, it forced the footer back to the bottom of the page. by using the -400px it reduced the amount of negative space between the footer and the sign/register cards
section {
    min-height: calc(100vh - 400px);
}

* When I was in a position to deploy my site it was quickly apparent that any images stored in the postgres database for both staff and product apps where not pulling through correctly. once new products where added via the admin portal. images would show but once the page ws refreshed they would no longer appear. 
this was fixed fairly simply my hosting these images in an Amazon AWS S3 bucket. 
This presented another issue however , as the images being used for static use in html and css saved now would not load correctly. Again this was remedied by moving all images used for static purposed to the AWS bucket also. 


## Deployment

This Full Stack Django application was fully developed and version controlled Using Jetbrains Pycharm IDE.
It was version controlled locally via git and online using github.
Any environmental variables that had to be secured where stored in an eny.py file and hidden using a gitignore File to avoid being pushed to the live repo in github. 

These variables hidden in the env.py where translated into the production site in heroku settings under the Config variables section.

 
 this application was deployed by:

* Pushing the code from my IDE to Github via Git and the built-in PyCharm terminal.
* Creating an app on Heroku & deploying it from same.
* Adding any secret environment variables to the Config Vars of Heroku App Settings tab and assigning those the requisite secret values held in the env.py for Live Deployment.
* Installing and Adding Whitenoise to Middleware of project settings.py file to allow our application to serve it's own static files.
* In Heroku 'Deploy tab', deployment method was set to Github with automatic deploys set from the master branch.
* Once the above was done, the app was deployed via this link.

To clone the repository:

* Select the Repository from the Github Dashboard.
* Click on the "Clone or download" green button located above and to the right of the File Structure table.
* Click on the "clipboard icon" to the right of the Git URL to copy the web URL of the Clone.
* Open your preferred Integrated Development Environment (IDE) and navigate to the terminal window.
* Change the directory to where you want to clone the repository too. (In the case of PyCharm the directory path can be found through the "Navigate" tab).
* Paste the Git URL copied from above and click "Ok". (Again in the case of PyCharm once you click "clone", Git Root mapping will be automatically set to the project Root directory).
* Once open create an env.py file and assign the Database URL, Secret Key, Stripe Publishable & Stripe Secret, and finally Emailing variables. Ensure the env.py is living in the root of your project directory and then add it to .gitignore to ensure your Secret details aren't exposed.


## Credits and Acknowledgements:

* <a href="https://djangocentral.com/creating-comments-system-with-django/">Django Central</a> - helped me with comments system for te blog app.  
* <a href="https://github.com/muvatech/Shopping-Cart-Using-Django-2.0-and-Python-3.6">Muvatech</a> - used to assist with the table product display for the cart and checkout app.

* Thanks to code institute for providing me with the learning materials to successfully complete this project and continues support through out the course.
Thanks to my mentor spencer Barriball for all his guidance and support through the entirety of my course.

* lastly I should like to thank my partner who despite having being a mum to my 7 week old baby, has manged to put up with me stressing over this project!  












