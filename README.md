**What is Fitness Dev-Love-Per?**

Fitness Dev-Love-Per is a web application developed using Django, a python based frame work for web applications. This web applications falls under "Fitness and Sports" Theme and first version was developed in February 
2023

**What problem is it solving?**

The Concise problem statement title is "AI Assisted Virtual Fitness Trainer".
In this modern era, users expect almost every service in online mode. Fitness Training is one among them. Keeping the demand in mind, many mobile and web applications have been developed which usually gives information about exercises like Benefits (Why to do) , List (What to do) and Procedure (How to do). All these applications are only information oriented and use simplex mode of communication (One way),
that is, they give guidance about exercises but do not verify whether the user is actually doing them or not. This inability to track user actions when guidance is provided is resulting in poor outcomes.
This problem is solved by this web application

**What is proposed solution?**

Develop a web application which not only provides information about exercises but also track user movements to determine whether the user is exercising correctly or not by estimating pose of the user. This is achieved through integration of Camera with web application powered by AI pose estimation models.
This approach enables Duplex communication (Two way) between the end user and web application that is, an exercise is considered as completed only if user performs it correctly.
Some of our web application features are

Security – facilitates three traits of cyber security: Confidentiality (Encryption), Integrity (Authentication and session manager), Availability

Pose detection – estimates pose of the user to determine whether exercise is performed correctly or not

Chat Bot – a chat bot which assists users with any queries they may have

Gate Keepers – to prevent unauthorized access and CSRF token attacks

Voice Assistance – guidance on exercises 

**Components of Tech Stack?**

Django – Python based web application framework

HTML, CSS, JS – Front end development

Python – Programming Language for backend

Media Pipe – Python Library for pose detection

Open CV – Python Library for camera integration

Smtplib – Module for Sending Emails

Pyttsx3 – Module for text to speech conversion

Nginx, Gunicorn – Request routing after deployment

Google Cloud Platform (GCP) – Virtual instance provider for deployment

**How to Install?**

1. Click on "Code" button
2. Download Zip file of project
3. Unzip the project contents
4. Install all the requirements mentioned in "requirements.txt" file
5. Run the project using "python manage.py runserver" command
