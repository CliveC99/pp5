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

![Am I Responsive?](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1704443913/pp5%20readme/am_i_responsive_hmgcgb.png)

### **Disclaimer if you would like to open any links in a new tab use `Ctrl` and click the link.**

# Table of Contents
  
- <p><a href="#wireframes">Wireframes</a></p>
- <p><a href="#ux">UX</a></p>
- <p><a href="#models">Custom Models</a></p>
-  <p><a href="#SEO">SEO & Web Marketing</a></p>
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
- As a ***user*** I can sign up to a newsletter in the my account dropdown section.
- As a ***user*** I can contact the site to get the information I require.
- As a ***user*** I can apply for a job to further my career.
- As a ***user*** I can recive confirmation emails after I make a purchase.

### **Owner Goals**

- As a  ***Site Admin*** I can install libraries so that the required libraries are installed and ready to use.
- As a ***Site Admin*** I can deploy the website early so that the site can be tested early.
- As a ***Site Admin*** I can Create/Read/Update/Delete products on the site.

### **Returning User**

- As a ***returning user*** I can check my order history.
- As a ***returning user*** I can check have my information saved to my profile for a quicker checkout experience.


# Models
## Custom Models

***These can be viewed inside the 'My Account' dropdown, users have to be logged in for these options.***

1. For my first custom models I decided to make a contact page for a site user to get in contact with the site admins. This can be viewed on the admin panel when users interact.
   - ``full_name = models.CharField(max_length=50, null=False, blank=False)``
   - `` email = models.EmailField(max_length=254, null=False, blank=False)``
   - ``description = models.TextField()``
2. For my second custom models I decided to make a newsletter form for a site user to subscribe to. The emails registered can be viewed in the admin panel when a user subscribes.
   - ``email = models.EmailField(max_length=254, null=False, blank=False)``
  3. For my third custom model I decided to make a job application form for interested site users to apply for a job. The applications can be viewed in the admin panel when a user applys for a selected job through the dropdown choice box in the form.
     - `` full_name = models.CharField(max_length=50, null=False, blank=False)``
     - ``job_choices = [
        ("Store Manager", "Store Manager"),
        ("Sales Manager", "Sales Manager"),
        ("Delivery Driver", "Delivery Driver"),
        ("Delivery Driver (International)", "Delivery Driver (International)"),
    ]``

     - ``job = models.CharField(choices=job_choices, null=True, blank=False, max_length=50)``
     - `` email = models.EmailField(max_length=254, null=False, blank=False)``
     - `` phone_number = models.CharField(max_length=20, null=False, blank=False)``
     - ``country = CountryField(blank_label='Country *', null=False, blank=False)``
     - ``postcode = models.CharField(max_length=20, null=True, blank=True)``
     - ``town_or_city = models.CharField(max_length=40, null=False, blank=False)``
     - ``street_address1 = models.CharField(max_length=80, null=False, blank=False)``
     - ``street_address2 = models.CharField(max_length=80, null=True, blank=True)``
     - ``county = models.CharField(max_length=80, null=True, blank=True)``
  
  The reason I decided to use these models for my site is that I belive it can benifit an ecommerce website massively.


# SEO
* SEO & Web Marketing
  
 ## Business Model
FK Performance operates on an e-commerce platform for car enthusiasts selling car parts and car accessories. Our business model focuses on the online sale and distribution of car parts and car accessories. We offer a range of car parts, enabling customers to find the correct extras to add to their cars! Our revenue is generated through direct sales of these car parts. We maintain community engagement approach, giving the user the ability to give feedback and get in contact through a newsletter and social media.

 ## Web Marketing Strategies

 * Facebook
 ![FK Facebook](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1701170850/pp5%20readme/1_llugue.png)
  ![FK Facebook](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1701170844/pp5%20readme/2_mq9niy.png)
   ![FK Facebook](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1701170850/pp5%20readme/3_xda4ff.png)
   - Facebook is the number one way for a business to get their name out there. It also helpes the site get mentioned through word of mouth/sharing of posts.


* Newsletter
![Newsletter](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1704444044/pp5%20readme/newsletter_kcbpfi.png)

- This newsletter can allow the site owner to send out emails with deals, this would boost people coming back to the site and spread the world around.

* SEO
  - There is a robots.txt and sitemap.xml for search engine crawlers and proper indexing.




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
- Contact Section
- Job Application Section
- Confirmation email after a purchase

| Feature        |      |
   | -------------  |:-------------:|
   | Login | ![Login](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1701164024/pp5%20readme/login_vrh5lx.png) |
   | Registration | ![Registration](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1701164024/pp5%20readme/register_ezx6zb.png) |
   | Logout | ![Logout](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1701165981/pp5%20readme/logout_w9nkxu.png) |
   | View items by category | ![View items by category](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1704444191/pp5%20readme/categories_xmzvtj.png) |
   | View items by filter system | ![View items by filter system](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1701166170/pp5%20readme/filter_xg3krg.png) |
   | Search Items | ![Search](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1701166190/pp5%20readme/search_yfloyo.png) |
   | Add Items | ![Add Items](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1701166287/pp5%20readme/add_nu5ngi.png) |
   | Checkout Guest/Register | ![Checkout](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1701166324/pp5%20readme/login-save-info_do7biz.png) |
   | Popup Messages | ![Popup](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1701166486/pp5%20readme/popup_oh9zcg.png) |
   | Update Quantity | ![Update Quantity](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1701166519/pp5%20readme/quantity-update_jnnnp1.png) |
   | Order Success | ![Order Success](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1701166536/pp5%20readme/order-success_dlxcoi.png) |
   | Order History | ![Order History](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1701166553/pp5%20readme/order-history_j3hhpa.png) |
   | Contact Section | ![Contact Section](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1704444314/pp5%20readme/contact_re592k.png) |
   | Job Application Section | ![Job Application Section](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1704444443/pp5%20readme/job_application_nwf9dq.png) |
  | Confirmation Email | ![Confirmation Email](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1711576020/pp5%20readme/confirmation_email_ndctep.png) |

## Features to be added

* Comments about a item, review system, favourite items (Wishlist)

# Manual Testing

   | Feature        |    Expected   | Result       | Test |
   | -------------  |:-------------:| -----:| -----: |
   | Login | Logs the user in | The user is logged in correctly. | Try logging in with username and password |
   | Register   | Registers the user to the site    | The user is registered to the site correctly. | Fill in the required fields. |
   | Logout   | Logs user out   | User is logged out | Click log out user and confirm |
   | View Products | Products show  | Products are there | Views products page |
   | View products by category | Products appear by category   | Prodcuts appear per categorty | Go into each category |
   | View products by filter   | Products appear by filter | Products appear per filter | Check each filter |
   | Search Items  | Product appears by search | Product appears by search | Search items |
   | Add items to bag  | Items gets added to bag | Item appears in bag | Add items to bag |
   | Checkout as guest or registered  | Option to login or save info | Option is given | Go to checkout logged in and logged out |
   | Popup Messages  | Messages appear | Popups appear for different tasks | Try different task that produce a message |
   | Update Quantity  | Quantity updates | Quantity does update | Add items and remove items |
   | Order Success  | Order completes and shows order success page | Order success page shows | Order some items on the site |
   | Order History  | Shows order history in profile | Failed - Grand total doesn't show - Explained further down | Order some items on the site |
   | Contact Section  | Shows user is subscribed | Shows user subscribed - Email is logged to Admin Panel | Enter an email and press subscribe |
   | Job Application Section  | Applied for the job when the form submits | Shows user applied - Details is logged to Admin Panel | Fill out the form and submit |
   
   ## Examples of testing features
  ### Order History
  ![Order History](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1709427993/pp5%20readme/order_history_gd1eh2.png)
  ### Order Success
  ![Order Success](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1709427993/pp5%20readme/order_success_ikg3dj.png)
  ### Pop Up Messages
  ![Pop Up Message](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1709427993/pp5%20readme/pop_up_messages_ejbbsb.png)
  ### Contact Us
  ![Contact Us](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1709427993/pp5%20readme/contact_us_section_uac7me.png)
  ### Update Quantity
  ![Update Quantity](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1709427993/pp5%20readme/updated_quantity_iamtan.png)
  ### Add Items to bag
  ![Add items](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1709427993/pp5%20readme/items_added_to_bag_auakve.png)
  ### Products Filtering
  ![Products Filtering](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1709427993/pp5%20readme/products_low_to_high_tcdton.png)



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
- [Django-Countries](https://pypi.org/project/django-countries/)
  - Django-Countries for using 2 letter terms.
- [Stripe](https://stripe.com/ie)
  - Stripe for card payments.
- [AWS](https://aws.amazon.com/?nc2=h_lg)
  - AWS for storing static files.
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
  - Boto3 for static files.
- [S3 Transfer](https://aws.amazon.com/s3/transfer-acceleration/)
  - S3 Transfer for static files.
- [Gmail](https://mail.google.com/)
  - Gnail for sending verifaction emails.
   
  

# Bugs and Fixes

  | Bugs/Errors        |   Explain   | Fix |
   | -------------  |:-------------:| -----: |
   | Searched items wasn't showing | I was having issues with searched item text wasn't showing | There was an indention error  |
   | Delivery price was wrong | I was having issues with the delivery price being wrong | I fixed this by adding ``{{ item.product.price  calculate_total:item.quantity }}`` |
   | Delivery too high | I was having issues with the the delivery being too high | I fixed this by changing the percentage to ``STANDARD_DELIVERY_PERCENTAGE = 0.1`` |
   | Overlapping | I was having issues with overlapping information on mobile | Turns out I had ``{% include 'includes/mobile-top-header.html' %}`` in twice|
   | Home Button | Home button wasn't an option on medium screens | I solved this with adding ``d-lg-none`` |
   | DB Issue | When I changed to codeanywhere my DB file didn't transfer over from gitpod | With the help of tutor support. I had to pull the info from my DB and put it in a json file using ``python3 manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json`` |
   | Order History | Order Total, Delivery Total and Grand total not updating | I solved this by fixing a typo re: ``self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0`` |
   | Stripe Keys | I was having issues with my webhooks | I had stored the wrong secret key, I updated the key and the issue was solved.  |
   | Local and Postgres DB | I was having issues with my Postgres DB. 11 migrations had not been passed to my Postgres DB. | I solved this by clearing my Postgres DB and making migrations and migrating everything  |

## Unresolved Bugs

* No issues.

# Deployment
## Project Creation (Github)

   1. Head over to [CI Template](https://github.com/Code-Institute-Org/gitpod-full-template)
   2. Press 'Use this template'
   3. Create a new repository.
   4. Select a name.
   5. Click create.
   6. Click gitpod.
   7. In the terminal install Django and Gunicorn
      - `pip3 install django gunicorn`
   8. Install the required libaries
      - `pip3 install dj_database_url==0.5.0 psycopg2`
   9. Install Cloudinary libaries
      - `pip3 install dj3-cloudinary-storage`
  10. Create requirements file
      - `pip3 freeze --local > requirements.txt`
  11. Create Project
      - `django-admin startproject your_project_name .`
  12. Create App
      - `python3 manage.py startapp your_app`
  13. In settings.py add your app name inside "Installed apps" and save the file
  14. Migrate your changes
       - `python3 manage.py migrate`
  15. To run the server use `python3 manage.py runserver`
  16. Inside of settings.py in the "Allowed hosts" field add your server address

## DataBase

  1. Head over to [Elephantsql](https://www.elephantsql.com/)
  2. Create an account
  3. Click "Create New Instance"
  4. Set up your free plan
  5. Select your region
  6. Press "Review"
  7. Copy your databse url, this can be stored as an enviorment variable to match "DATABASE" variable in settings.py


## Heroku App Creation
  1. Head over to [Heroku](https://dashboard.heroku.com/)
  2. After logging in, click "New" at the top right of the page.
  3. Click "Create New App"
  4. Choose a name, select your region and click "Create New App" 

## Heroku Setup (Deployment)

  1. Head over to [Heroku](https://dashboard.heroku.com/)
  2. Open "Settings" and click "Reveal Config Vars"
  3. Inside Config Vars:
      - `SECRET_KEY` - Use the one stored in `settings.py` or `env.py`
      - `DATABASE_URL` - This is the url provided by ElephantSQL
      - `AWS_ACCESS_KEY_ID` - This is found in your S3 bucket
      - `AWS_SECRET_ACCESS_KEY` - Found in AWS
      - `EMAIL_HOST_PASS` - Email host password
      - `EMAIL_HOST_USER` - Email host address
      - `STRIPE_PUBLIC_KEY` - Stripe public key
      - `STRIPE_SECRET_KEY` - Stripe secret key
      - `USE_AWS` - This should be set to `True`
  4. Once all this is filled in
      1. Head over to the deploy section on Heroku
      2. Connect your Github repository.
      3. Select if you want manual or automatic deploys
  5. After all this is finished
      - Push a deployment and press "Open App" and check everything is working correctly

## AWS Setup
  ### S3
  1. Head over to [AWS](https://aws.amazon.com/)
  2. Create an account
  3. Open S3 Services
  4. Create a bucket - Create a name and select your region
  5. Select "ACLs enabled" and "Bucket owner preferred" when prompted
  6. Select "Static Website Hosting" and enable it.
      - CORS:
      `[
  {
    "AllowedHeaders": ["Authorization"],
    "AllowedMethods": ["GET"],
    "AllowedOrigins": ["*"],
    "ExposeHeaders": []
  }
]`
      - Configure bucket policy as needed
      - Select "List" and enable for everyone

### IAM
  1. Find the IAM section in the console.
  2. Under "User Group", create a new one - Insite "Policies" create a new one
  3. Apply the policy to the group
  4. Select "Security Credentials"
  5. Click "Create access key" and download the ".csv" file

### Media Folders
  1. Inside your bucket - Create a new folder called "media"
  2. Move all your images to this folder

# Cloning

1. Open up the repository [FK Performance](https://github.com/CliveC99/pp5)
2. Above the list of files click "Code".
3. Click if you would like to clone as "HTTPS", "SSH", or "GitHub CLI".
4. Once selected press copy.
5. Open Git Bash.
6. Change the directory to where you want the clone to appear.
7. Paste in the link you copied in step 4. (This is the line for my repository): <br>
  `$ git clone https://github.com/CliveC99/pp5.git`
8. Press enter and the clone will happen.

# Forking

1. Open up the repository [FK Performance](https://github.com/CliveC99/pp5)
2. Locate the fork button at the top right.
3. Select an owner and repository name.
4. Add a description (optional).
5. Click "Create fork".
6. The repository should appear in your repositories now.

# **Git Commits**

- I structured my git commits whenever I would add, change or update code.
- I did this by using:

   1. ``git status``
   2. ``git add (file name)``
   3. ``git commit -m (message)``
   4. ``git push``
  ![Git Commits](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1701168971/pp5%20readme/commits_twvgct.png)


# Credits

- I got help and inspiration from Boutique-Ado
  - [Boutique-Ado](https://github.com/Code-Institute-Solutions/Boutique-Ado)
- I got help with form succession page from [Django docs](https://docs.djangoproject.com/en/4.2/topics/forms/)
- I got help from [Pillow](https://pypi.org/project/Pillow/), [Cloudinary Python SDK](https://cloudinary.com/documentation/django_integration), [Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/introduction/) etc.
- I used [Am I Responsive?](https://ui.dev/amiresponsive) to check was the site responive.
- This project would not be possible without the help of my mentor (Rory_Patrick), my friends, and my facilitator (Chris Quinn) and Tutor Support.
- I would also like to thank the private "Novemeber 2022-UCD" group on slack for the all the support.

 <p><a href="#table-of-contents">Back to table of contents.</a></p>
