# FK Performance

FK is the largest car part suplier in Ireland!

The website is hosted on heroku.

The aim of the website is for people to order items.

As a user you can:
- Create an account
- Login in to an account
- Add items to the bag
- Search items
- View items by category
- View items by filter system
- Checkout as a guest or registered user
- And lots more!

This is my fifth portfolio project for Code Institute. I will demonstrate my learnings in Python, HTML, Django, Bootstrap etc.

Live deoployed link on heroku: [FK Performance](https://pp5-fk-ff4c1b683208.herokuapp.com/)

![Am I Responsive?](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1701161969/pp5%20readme/am_i_responsive_qi8qvm.png)

### **Disclaimer if you would like to open any links in a new tab use `Ctrl` and click the link.**

# Table of Contents
  
- <p><a href="#wireframes">Wireframes</a></p>
- <p><a href="#ux">UX</a></p>
- <p><a href="#features">Features</a></p>
- <p><a href="#manual-testing">Manual Testing</a></p>
- <p><a href="#frameworks"> Framework / Programs Used / Technologies</a></p>
- <p><a href="#bugs-and-fixes">Bugs and Fixes</a></p>
- <p><a href="#creation">Creation</a></p>
- <p><a href="#deployment">Deployment</a></p>
- <p><a href="#cloning">Cloning</a></p>
- <p><a href="#forking">Forking</a></p>
- <p><a href="#git-commits">Git Commits</a></p>
- <p><a href="#credits">Credits</a></p>


# Wireframes

I used Google Slides to show my wireframes so it would keep the README clean and tidy.

-[Wireframes](https://docs.google.com/presentation/d/e/2PACX-1vTvq7RfkkhhwUFfnMtxDri4pg1YBxltvv8aLAIw-k5ZMahMDOJz8y8-ix_la1Yn5Y7GHhJPMpyeThCK/pub?start=false&loop=false&delayms=15000) (Google Slides)

# UX

### **User Goals**

I used a Kanban board to outline my progress [view here.](https://github.com/users/CliveC99/projects/3)

- As a ***user*** I can view the page so that I can get the required information.
- As a ***user*** I can register an account so that I can update my profile and check my order history.
- As a ***user*** I can login to the account so that I can can update my profile information and view my orders.
- As a ***user*** I can logout from the website so my personal information isn't left logged in.
- As a ***user*** I can view the privacy policy.
- As a ***user*** I can Create/Read/Update/Delete my profile information.
- As a ***user*** I can click on an item so that I can get the product details.
- As a ***user*** I can view items to add the item to my bag.
- As a ***user*** I can view the bag.
- As a ***user*** I can delete/update the items in the bag.
- As a ***user*** there is a payment authentication for cards.
- As a ***user*** I'm brought to a success page after payment.
- As a ***user*** I can get popup messages.
- As a ***user*** I can sign up to a newsletter in the proifle section.

### **Owner Goals**

- As a  ***Site Admin*** I can install libraries so that the required libraries are installed and ready to use.
- As a ***Site Admin*** I can deploy the website early so that the site can be tested early.
- As a ***Site Admin*** I can Create/Read/Update/Delete products on the site.

### **Returning User**

- As a ***returning user*** I can check my order history.

# Features

## **Exisiting Features**

- Login
- Regisiter
- Logout
- View items by category
- View items by filter system
- Search items
- Add items to the bag
- Checkout as a guest or registered user
- Popup messages
- Update Quantity
- Order Success
- Order History

| Feature        |      |
   | -------------  |:-------------:|
   | Login | ![Login](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1701164024/pp5%20readme/login_vrh5lx.png) |
   | Registration | ![Registration](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1701164024/pp5%20readme/register_ezx6zb.png) |
   | Logout | ![Logout](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1701165981/pp5%20readme/logout_w9nkxu.png) |
   | View items by category | ![View items by category](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1701166086/pp5%20readme/category_ehy0bd.png) |
   | View items by filter system | ![View items by filter system](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1701166170/pp5%20readme/filter_xg3krg.png) |
   | Search Items | ![Search](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1701166190/pp5%20readme/search_yfloyo.png) |
   | Add Items | ![Add Items](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1701166287/pp5%20readme/add_nu5ngi.png) |
   | Checkout Guest/Register | ![Checkout](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1701166324/pp5%20readme/login-save-info_do7biz.png) |
   | Popup Messages | ![Popup](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1701166486/pp5%20readme/popup_oh9zcg.png) |
   | Update Quantity | ![Update Quantity](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1701166519/pp5%20readme/quantity-update_jnnnp1.png) |
   | Order Success | ![Order Success](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1701166536/pp5%20readme/order-success_dlxcoi.png) |
   | Order History | ![Order History](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1701166553/pp5%20readme/order-history_j3hhpa.png) |

## Features to be added

* Comments about a item, review system.

# Manual Testing

   | Feature        |    Expected   | Result       | Test |
   | -------------  |:-------------:| -----:| -----: |
   | Login | Logs the user in | The user is logged in correctly. | Try logging in with username and password |
   | Register   | Registers the user to the site    | The user is registered to the site correctly. | Fill in the required fields. |
   | Logout   | Logs user out   | User is logged out | Click log out user and confirm |
   | View Products | Products show  | Products are there | Views products page |
   | View products by category | Products appear by category   | Prodcuts appear per categorty | Go into each categort |
   | View products by filter   | Products appear by filter | Products appear per filter | Check each filter |
   | Search Items  | Product appears by search | Product appears by search | Search items |
   | Add items to bag  | Items gets added to bag | Item appears in bag | Add items to bag |
   | Checkout as guest or registered  | Option to login or save info | Option is given | Go to checkout logged in and logged out |
   | Popup Messages  | Messages appear | Popups appear for different tasks | Try different task that produce a message |
   | Update Quantity  | Quantity updates | Quantity does update | Add items and remove items |
   | Order Success  | Order completes and shows order success page | Order success page shows | Order some items on the site |
   | Order History  | Shows order history in profile | Failed - Grand total doesn't show - Explained further down | Order some items on the site |
   

   

   | Testing        |    Expected   | Result       | Test |
   | -------------  |:-------------:| -----:| -----: |
   | Browsers | Works as normal. | No issues. | Use Chrome, Safari, Edge and Firefox |
   | Links | Links work. | Links open as they should. | Open each link |
   | Form validation | Fields are required to submit | Fields were required to submit the form | Submit the form with empty fields and with fields filled. |
   | Responsiveness | Should not break at any screen size | Didn't break at any size | Drag the screen down to 320px |
   | Lighthouse | Scores are good | Performance, Accessibility, Best Practice, SEO > 89%  | Chrome Developer Tools Lighthouse |

# Frameworks

- [Django](https://www.djangoproject.com/)
  - Django was used as the framework and logic of the project.
- [Bootstrap](https://getbootstrap.com/)
  - Bootstrap was used for the styling of the site.
- [Git](https://git-scm.com/)
  - Git was used for version control
- [Github](https://github.com/)
  - Github was used for storing the code.
- [Gitpod](https://gitpod.io/workspaces)
  - Gitpod was used for coding.
- [Codeanywhere](https://app.codeanywhere.com/)
  - Switched to Codeanywhere during the project for coding.
- [Heroku](https://id.heroku.com/)
  - Heroku was used for live deployment.
- [Balsamiq](https://balsamiq.com/)
  - Balsamiq was used for wireframes.
- [Google Slides](https://www.google.com/slides/about/)
  - Google Slides was used for storing large images.
- [Gunicorn](https://gunicorn.org/)
  - Gunicorn was used for the server for heroku
- [Cloudinary](https://cloudinary.com/)
  - Cloudinary was used for image storage.
- [Pillow](https://pypi.org/project/Pillow/)
  - Pillow was used for an image libary
- [HTML](https://en.wikipedia.org/wiki/HTML/)
  - HTML was used for the templates.
- [JavaScript](https://www.javascript.com/)
  - Javascript was used to get users info.
- [Python](https://www.python.org/)
  - Python was used for functionality of the site.
- [CSS](https://en.wikipedia.org/wiki/CSS)
  - CSS was used for extra styling.


# Bugs and Fixes

  | Bugs/Errors        |   Explain   | Fix |
   | -------------  |:-------------:| -----: |
   | Searched items wasn't showing | I was having issues with searched item text wasn't showing | There was an indention error  |
   | Delivery price was wrong | I was having issues with the delivery price being wrong | I fixed this by adding ``{{ item.product.price | calculate_total:item.quantity }}`` |
   | Delivery too high | I was having issues with the the delivery being too high | I fixed this by changing the percentage to ``STANDARD_DELIVERY_PERCENTAGE = 0.1`` |
   | Overlapping | I was having issues with overlapping information on mobile | Turns out I had ``{% include 'includes/mobile-top-header.html' %}`` in twice|
   | Home Button | Home button wasn't an option on medium screens | I solved this with adding ``d-lg-none`` |
   | Order History | Order Total, Delivery Total and Grand total not updating | Unresolved - Explained below. |

## Unresolved Bugs

* Order History
  - This was unresolved.
  - After talking with tutor support and running out of weekly hours we couldn't find a fix sadly. After checking Slack, checking Google and debugging its unresolved.
  - Unfortunately this bug didn't exist on my local enviorment. Order Histort works as it should locally (Still does) but on the deployed version this is bug.
