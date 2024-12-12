# Choice of tech stack

In this project, I have decided to use various programming tools to reach the desired goal of the assignment brief. To achieve this, I have used HTML, CSS and JavaScript. Firstly, HTML is used as the front end of the website and controls how the website is structured. Next, CSS applies the styling and presentation; this helps with the design and overall look of the website. Lastly, JavaScript adds interactivity to the website, allowing moving images, sticky headers, functional searching and much more. Together, these are the powerhouse of Web Development and are core technologies used in most real-life scenarios. With this, it makes learning HTML CSS and JavaScript practical, as they're used a lot in the web. Furthermore, with it being quite a well-known profession, there are many libraries and frameworks that can assist you when making websites; these examples include Bootstrap for CSS and React for JavaScript.

When mentioning these frameworks such as Bootstrap for CSS, they can be compared to other CSS frameworks such as Tailwind CSS. Firstly, Bootstrap is great for mobile design as well as web design, with its main proirity being a mobile-first design framework. Bootstrap uses both elements of CSS and JavaScript components which mainly focus on buttons, navigation menus and forms. This makes Bootstrap an excellent choice of framework as these are all essential within the project I made. In addition, Bootstrap has a large community with many repositories on Github which can help when first using the framework and guide newer CSS users on how to use CSS. On the other hand, Tailwind has some similarities to Bootstrap in the fact that they both help with user interface. On the contrary, Tailwind offers more of a teaching instead of a template or pre-built component like what Bootstrap offers; this benefits the users who wish to design their own website to a concept they have had made or is in their mind. Additionally, with that information, we can infer that Tailwind is for more expert-level CSS users and Bootstrap is for more beginner-level CSS. Lastly, when it comes down to choosing what framework to use, you have to ask yourself, "Do I want an entirely custom design?" "What is the timeframe?" and "How big is the project?"

Tailwind is a great tool for those with a good knowledge of CSS, a design in mind for a custom website and a medium-sized project. Whereas Bootstrap is good for beginners, quick projects and a pre-made library of simple components of a website. When it came time for me to choose, Bootstrap ticked all the boxes for me.

A new addition from the second part of the assignment is the inplementation of a database. After narrowing dowwn my options I was left with two options MySQL or MongoDB

MongoDB is a NoSQL database that uses document orientated formatting called BSON (binary JSON). Each document has different structures meaning that parts can be removed as well as added without complication with the other documents in the database. Additionally, MongoDB is a lot more beginner-friendly with its web approach and simple design which is one reason I chose it over MySQL. Another reason I chose MongoDB over MySQL is because data can be added from a flask form and it will create the database and make the record whereas MySQL needs to have a table already made for the location of the record.
# Version Control

Hello, Welcome to my repository for Tech Stack Assessment 2.

Here is the link to my repsoitory: (https://github.com/ThomasJohnstone8/4113-Assignment2)


# Project Overview

In this project, I aim to create a fully functioning website using HTML, CSS and JavaScript. In this website, I will include user registration and authentication. The user will be able to sign up, login and manage the account. Another feature I will add is the ability to upload a profile picture, update it and list their interests in the profile. I will add more, smaller features such as a drop-down menu to help navigate the website, an About Us page that gives the user insight to the website and its uses, a Contact Us page that gives the user options to contact us, user reviews so the user can leave reviews of the place, a simple homepage that directs the user in different directions and lastly, a search for AI tools section (product page). Furthermore, another goal of my website is to include a page where users can interact and collaborate. This is achieved by making posts and viewing previous posts.

In the second half of the project, I aim to implement a MongoDB database to my website that collects user login, user registration, tool creation and more.


# Installation Instuctions

Step 1: Unzip the file from Moodle.

Step 2: Add the unzipped file to VS code

![openfolder](/static/Images/openfolder.png)

Step 3: Ensure you have all the extensions needed for this project which are the following: MongoDB for VS code, Python, Pylance, Python Debugger

![extensions](/static/Images/extensions.png)

![allExtentions](/static/Images/allExtensions.png)

Step 4: Now ensure you have a version of python install on your computer

![pythonDL](/static/Images/pythonDL.png)


Step 5: open a new terminal and type the following in:

pip install pymongo

pip install Flask


Step 6: Once you have everything downloaded, you are ready to go. go to the app_login.py file and press the run button in the top right. If that doesnt work, use the command below in the terminal.


flask --app app_login.py run

# Technical Challenges

There were many technical challenges that I was faced with and with little communication with my tutors it was hard to overcome these. I dealt with various errors such as 300s 400s and a few flask errors within my python. The python syntax errors were quick to fix as my python skills have developed severely since starting this course. On the other hand, the connection issues were a thorn in my side.


# Project Plan

Below is my Gantt chart that I used to help track and manage my time throughout the first part of the project. The Gantt chart has been updated to reflect the change to the deadline as well. The Gantt chart includes all the correct fields such as choice of tech stack, legal and ethical consideration. A few changes were made to the Gantt chart to adapt to the change in submission and it allowed me to spend more time fleshing out the website and improving the overall look of it using HTML and CSS features. As well as this, it allowed me to manage my time better and space out spending a day on each of the documentation.

![ganttchart](/static/Images/ganttchart.png)

# User Guide

Below are instructions on how to navigate the website through a flowchart; this dictates the flow of the website and how the user can navigate it.

![flowchart](/static/Images/flowchart.png)

# Legal and ethical consideration

When it comes to my website, many legal and ethical considerations must be identified, one of which being privacy and data protection. The website must follow the rules and regulations of the current GDPR data collection schemes and data privacy laws that take place. All practices of this must be written and have the user's knowledge of it; this could be done through a consent form in which they read and accept the terms and conditions of how the website handles data privacy. Another legal practice to consider is copyright and ensuring all content (text, video, image, templates) are used legally, are licensed, paid and acknowledged, or references have been made to the original author or owner. This is to avoid copyright infringement and ensure proper credit is given to those who made it. There are laws that force the website to align with disabilities and ensure it is accessible to all users including disabled ones. This is used to create a safe and collaborative environment that allows for all individuals to use the website. Another legal practice to ensure is avoiding harm. The liability of the services I provide are on my shoulders and I should consider what product the website sells and ensure they display no harm, be that physical or emotional as this can impact the website negatively. Lastly, the website needs to be transparent with the terms and conditions; this will lead to a better relationship with the users and thus a better website.


# Risk assessment

There are various risks to consider when approaching my website. As it is a website with user interaction, there can be a chance of phishing attacks. A policy to follow to avoid this would be to warn all users about the link that they are clicking. My website can ensure this by implementing a pop-up before a link is clicked; however, this would be a future improvement to make to the website. Another risk involved is weak passwords; this can be avoided by making data validation to confirm that the password is strong. For example, including an uppercase character, a minimum of 1 symbol and over 12 characters. A final risk to consider in my website would be ensuring the protection of our stored data so hackers cannot gain access to it and possibly sell the data or use it in a social-engineering attack on the user. This can be mitigated with a MFA (multi-factor authentication) check as well as a strong and realiable database host that will keep the data private.

To avoid some of these issues, in the 2nd part of this project, I was tasked with implementing a database on my website. A database holds many risks and therefore, I implemented a few countermeasures to mitigate them. First is Werkzeug password hashing. This keeps the security in the database hashed and protected. Meaning that if the database were to get breached, the passwords of the users would not be leaked or taken. Additionally, MongoDB the database provider I am using has already implemented security in the fact that only certain IP addresses can connect to the database and see the records.


# Real World Application

One real world application of a social media platform such as Instagram. In these types of platforms, users can create accounts, post content, like and share posts and more. This can be handled by Flask in the backend dealing with user posts, managing profiles and routing them. MongoDB can be used to store the user data, comments, followers and more.


# Future considerations

My future considerations for this project would be to include a scalable host and a backend to the server. This backend database will allow the user to login and register an account; this interactivity will allow the user to interact with the website more by locking the features behind a login. Another improvement I will make is adding a cart and better product system; this will allow the user to navigate the product page better, as well as adding and removing products in a cart, which would help the user when purchasing multiple items. A scalable host would allow the website to expand in the future and allow for more features and expansions. Returning to the product page, at the moment of the website being made, the likes and dislikes are native to your personal computer. In the future, I would like to expand this and allow the likes and dislikes to be stored in a database and the product to be ranked from top to bottom based on the likes and dislikes. This would be a complicated expansion; however, in the future it is a doable task. To conclude my future improvements, I will develop the template more and change it. In the assignment I used a template and in the future I will consider changing this and starting from scratch. This can be achieved with a better understanding of HTML, CSS and JavaScript.

A few of these considerations have been met, but a few haven't. One consideration I still wish to change is the use of a template in both parts of the assignment.


# In code documentation

I have added comments throughout my code to help the user navigate the code and understand it.


# References

Egil J (2020, December). W3.CSS Website Templates. W3Schools. https://www.w3schools.com/w3css/w3css_templates.asp

N/A. N/A. Freepik Icons. Freepik. https://www.freepik.com/icon/group_681494

N/A. N/A. Flaticon Icons. Flaticon. https://www.flaticon.com/free-icon/shopping-cart_1413908

N/A. N/A. Flaticon Icons. Flaticon. https://www.flaticon.com/free-icon/conversation_538896

Codehal. (2023, June 18). Login Form in HTML & CSS. Youtube. https://www.youtube.com/watch?v=hlwlM4a5rxg&t=290s

N/A. N/A. W3.CSS Examples. W3 Schools. https://www.w3schools.com/w3css/w3css_examples.asp

Otto M. (2023, January 17). BootStrap Forms. BootStrap. https://getbootstrap.com/docs/5.3/forms/overview/

Aleko D (2023, September 3). Login-Form-By-Dan-Aleko. Github. https://github.com/danaleko/Login-Form-By-Dan-Aleko

Ikechukwu V (2024 Febuary 13). Best CSS Frameworks. freecodecamp. https://www.freecodecamp.org/news/best-css-frameworks-for-frontend-devs/

__Beginnerscode__ (2021, August 16). How to ￼code an On click Counter - HTML CSS and JavaScript Tutorial - Front End Project. Youtube. https://www.youtube.com/watch?v=9LcbJWhUAoo






