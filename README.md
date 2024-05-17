# Rebaz Motorcycle Blog

Join Rebaz and his passion for motorcycles in this amazing blog where he and his users share stories and pictures related to motorcycles. 
This Django based blog allows users to create their own account so that they can leave blog posts, comments and likes. 
This simple and easy to use blog is for the creator and users to share memories.

![Home Screen](media/images/responsive.jpg)

[View Rebaz Motorcycle Blog Live Website Here]()
---

## Table of Contents
### [User Experience](#user-experience-ux)
* [Project Goals](#project-goals)
* [Agile Methodology](#agile-methodology)
* [Target Audience](#target-audience)
* [First time user](#first-time-user)
* [Registered user](#registered-user)
* [Admin user](#admin-user)
### [Design](#design-1)
* [Color Scheme](#color-scheme)
* [Images](#images)
* [Database Scheme](#database-scheme)
* [Data Models](#data-models)
* [User Journey](#user-journey)
### [Security Features](#security-features-1)
* [User Authentication](#user-authentication)
* [Login Decorator](#login-decorator)
* [CSRF Protection](#csrf-protection)
### [Features](#features-1)
* [Existing Features](#existing-features)
* [Features Left to Implement](#features-left-to-implement)
### [Technologies Used](#technologies-used-1)
* [Languages Used](#languages-used)
* [Databases Used](#databases-used)
* [Frameworks Used](#frameworks-used)
* [Programs Used](#programs-used)
* [Installed Packages](#installed-packages)
### [Deployment and Local developement](#deployment-and-local-developement-1)
* [Local Developement](#local-developement)
* [ElephantSQL Database](#elephantsql-database)
* [Cloudinary](#cloudinary)
* [Heroku Deployment](#heroku-deployment)
### [Testing](#testing-1)
### [References](#references-1)
* [Docs](#docs)
* [Content](#content)
* [Acknowledgments](#acknowledgments)
---

## User Experience (UX)

Join Rebaz in this blog where he share motorcycle pictures and memories with the users. The user experience is simple and easy to use for all ages. A place where everyone can share their 
passion for motorcycles and adventures.

### Project Goals

The goal with this project is to share motorcycle pictures and memories through text and pictures. Engage with readers through creating blog posts and comments. Also give the ability for users to comment and like posts.

### Agile Methodology

Agile Methodology was used to help prioritize and organize tasks, writing the user stories and using project boards on github. Template was created to help write user stories and epics.

* Epics were written containing possible user stories and based on that the blog was made.
* User stories were created by looking at epics and through iterations the project was advancing.
* Project board is set to public.
* Project board was used to track progression of the task through the todo, in progress and done columns.
* Labels were added to sort the issues based on the importance.

<details>
<summary> Epic Template
</summary>

![Epic Template](media/images/epictemplate.jpg)
</details>

<details>
<summary> User Stories Template
</summary>

![User Stories Template](media/images/userstorytemplate.jpg)
</details>

<details>
<summary> User Stories, Issues
</summary>

![User Stories, Issues](media/images/userstoriesissues.jpg)
</details>

<details>
<summary> Project Board
</summary>

![Project Board](media/images/projectboard.jpg)
</details>

#### Epics
1. User interaction with posts
2. User engagement with content
3. Account management
4. Content creation and management
5. Deployment

#### User Stories
1. View post list
* Given more than one post in the database, these multiple posts are listed
* When a user opens the main page a list of posts is seen
* Then the user sees all post titles with pagination to choose what to read
2. Open a post
* When a blog post title is clicked a detailed view of the post is seen
3. View comments
* Given one or more comments the user and admin can view them
* A site user can click on the comment thread to read the conversation
4. Account registration
* Given an username and password a user can register an account
* The user can log in
* When the user is logged in they can add post and comment posts
5. Comment on post
* User can comment on posts
* User can reply the comments
6. Modify and delete comment on a post
* A logged in user can modify and delete their comment
7. Manage posts
* Admin and users can create, read, update and delete blog posts
8. Likes
* User can view likes on posts
* User can add like and unlike to posts
9. Author image
* Author image is visible in the post
10. Finish Readme and Testing
* User can view the completed readme from github repo
* User can view the completed testing from github repo
11. Deployment
* Finish the blog and deploy to Heroku

Detailed look can be found in the [Project Board](https://github.com/users/rebazp/projects/8/views/1)

### Target Audience

* People seeking to connect with other motorcyclists.
* People seeking to share motorcycle memories and pictures.

### First Time User

* Simple and intuitive blog with easy navigation.
* Easy Registration process.
* Simple to use on any device.


### Registered User

* Seamless login process with a secure and personalized user account.
* Browsing through posts and see related comments.
* Give comments and likes.
* Option to log out.

### Admin User

* Secure and separate login portal for admin users with appropriate access control.
* Access to an admin dashboard for managing users, posts and comments
* Ability to add, edit, or delete user, posts and comments.

## Design

The blog is easy to read and navigate through. The navbar contains the links to guide the user through the blog. The footer is visible and connects the user to social media.

### Color Scheme

[coolors.co](https://coolors.co/0a1128-001f54-034078-1282a2-fefcfb)

![screenshot](media/images/palette.jpg)

### Images

All images used in these blog posts are my own.

### Database Scheme

![Database](media/images/DatabaseSchemeMCBlog.jpeg)

### Data Models

1. AllAuth User Model
    * Django Allauth, the User model is the default user model provided by the Django authentication system.
    * The User entity has a many-to-many relationship with the blog posts. This means that a User can have many blog posts and interact with other blog posts through likes, comments, edits, deletes etc.
---
3. Post Model
    * As a user you can create blog posts.
    * Admin can add, delete and update posts through djangos admin panel.
    * Only Admin can change the data in the backend.
    * User can see the posts created by other users.
    * Tools to be used in posts are: title, body, slug, author, featured-image, author-image, excert, updated-on, created-on, status, likes and id.
    * Full CRUD functionality is available to the user.
---
4. Comment Model
    * As a user you can create blog comments.
    * Admin can add, delete and update comments through djangos admin panel.
    * Only Admin can change the data in the backend.
    * Tools to be used in comments are: post, name, user, email, body, created-on, approved and id.
    * Full CRUD functionality is available to the user.

### User Journey 

![User Journey](media/images/UserJourney.jpeg)

## Security Features

### User Authentication

* Django Allauth is a popular authentication and authorization library for Django, which provides a set of features for managing user authentication, registration, and account management.

### Login Decorator

* add_category, add_comment, add_post, article_details, delete_post and update_post: These views allows user to interact with the blog and requires user authentication.
* This ensures that only authenticated users can access these views.

### CSRF Protection

* Django provides built-in protection against Cross-Site Request Forgery (CSRF) attacks. CSRF tokens are generated for each user session, and they are required to submit forms or perform state-changing actions. When a user logs out, the session and associated CSRF token are invalidated, making it difficult for an attacker to forge a valid request using a copied URL.
