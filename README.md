

# Set Up Your Own Development Environment - Docker Versio

1. Clone this repository, copy the repo url and run `git clone [repo url]` on your terminal in your local directory of choice.
2. Install the Docker extension on your VScode, which allows you to monitor the state of the containers.
3. In your working directory, run `docker build .` to build the image from Dockerfile.
4. If successful, run `docker compose up` to build the containers from the image.

Hopefully, your terminal will look like this:
![Screen Shot 2023-04-03 at 5 25 58 PM](https://user-images.githubusercontent.com/69414708/229631325-f12b8bb5-d070-4882-a708-8f55188af362.png)
And your localhost:8000 will look like this:
![Screen Shot 2023-04-03 at 5 25 18 PM](https://user-images.githubusercontent.com/69414708/229631427-c1b723d4-3473-47e3-9f7a-d0525fcc2ed2.png)

5. Now, let's make [migrations](https://docs.djangoproject.com/en/4.1/topics/migrations/).
   In a new terminal, run `docker exec -it [containerID] bash`, where `-i` keeps the shell from exiting immediately, and `-t` allocates a pseudo TTY.
   Here is a more detailed [reference for the commands](https://docs.docker.com/engine/reference/commandline/exec/).
   Alternatively, go to the docker extension tab on the left of VSCode. Under the "container" tab, rightclick the "graysend website" container and click "attach shell",
   which will give us a container-specific terminal.

6. In the container-specific terminal, run `python manage.py showmigrations`, which will give us all the generated database changes which we will be able to apply to the db.
   Your terminal should look like this after `showmigrations`: <img width="961" alt="Screen-Shot-2023-04-03-at-3 41 20-PM" src="https://user-images.githubusercontent.com/69414708/229645366-4c8f4ad5-43e5-44fd-92c1-875c343defda.png">

7. Run `python manage.py migrate`, which will apply these changes to our Postgres DB. A lots of green checks aboard!
   <img width="741" alt="Screen-Shot-2023-04-03-at-3 43 17-PM" src="https://user-images.githubusercontent.com/69414708/229645435-ebd6e6f1-d1c1-4ca1-9154-ed65b3d0daf8.png">

8. Now, we have applied the changes that Django's built-in admin/sessions interface needs to make to the DB. One last thing we need to do is to create a superuser, so we can be omnipotent in our respective dev environment.
   To do so, run `python manage.py createsuperuser`, and set the user/password for the superuser to your liking, like so:
   <img width="479" alt="Screen-Shot-2023-04-03-at-3 44 10-PM" src="https://user-images.githubusercontent.com/69414708/229646103-1dc02cd2-2dd9-4b91-98b4-6461d8af41e0.png">

Local Development
=================

This guide will help you set up the local development environment using SQLite3, which eliminates the need to rebuild the Docker container.

Prerequisites
-------------

*   Python 3
*   pip

Setup Instructions
------------------

1.  **Clone the repository**: Copy the repo URL and run `git clone [repo url]` in your terminal, within your desired local directory.
    
2.  **Install dependencies**: In the project directory, run the following command to install the required packages:
    
    `pip install -r requirements.txt`
    
3.  **Migrate the database**: Run the following command to apply the necessary migrations:
    
    `python3 manage.py migrate`
    
4.  **Start the development server**: Run the following command to start the development server on port 8002:
    
    ```bash
    python3 manage.py runserver 8002
    ```
    
5.  **Access the application**: Open your web browser and navigate to the following URL:

    
    ```bash
    http://127.0.0.1:8002/
    ```
    

Now you should be able to view and interact with the application in your local environment.

# Meeting minutes

## Week 1 Thursday Meeting:
### Agenda:
- want a project that highlights user engagement  
- leveraging the admin components  
- multiple micro-services - more modular  
- Chop up the project to take on different parts  
- 5-week project?  
- Kathrin - interest in testing  
- Asynchronous parts  
- Authorization and database design - Tianci (app architecture)  
- Database design - Nikki  
- UI - katharin / Tom  

### Dids&Conclusions:
- 1:1 chat
- logging in 
- Identity/user profile 
- messages in text 
- Authorization (Tianci) 
- state of message: Read vs. unread and backlog 
- database design 

### Todos:
- decide on who is owning what part 2. ~~weigh venv vs. docker vs. poetry~~
- Blake to create skeleton repo and share with group 
- NIkki and Tianci to draft initial database design statement - with database type
- Tianci to start awesome Django thread!!!~
- Kathrin to share the ADR sample
- Tom to look into Poetry
- ALL look through relevant tutorials

## Week 2, Monday Docker Pairing:

- Thank you Enric for lending us your smart brain!
- Blaked drove us through setting up Docker.
- We ran into a problem where the local browser is 404 yet the container is telling us that the development server is up. We tried switching ports exposure configurations all kinds of ways to no avail. Then we realized that it was an error in the `CMD` section of the Dockerfile, where instead of setting "127.0.0.1:8000" directly, we should've used the generic "0.0.0.0:8000"
- Enric told us about the magic of `curl`.


## Week 2, Thursday Meeting:
### Agenda:
- Poetry 
- Version Control
- Data Structure
- ML Extension
- Separating the apps

### Dids & Conclusions:
- We like poetry and will do poetry
- Kathrin showed us github workflow
- We moved repo to an organization on Github (Thanks Abraham)
- We like the current DB design
- Many-to-many intermediary tables are named as statements
- We are all admins on the repo and will break things

### Todos:
- Enric: CI/CD angel
- Tom: Implement Poetry
- Abraham: Automatic Vulnerability Scanner
- Kathrin & Tom & Elizabeth: UI/UX 
- Kathrin: Dummy data for our local DB instance
- Blake & Iggee: Set up free-tier S3 & RDS instance
- Richie: Custom user class
- Blake & Elizabeth: ML-extension, what library?
- Iggee: Think aloud for how to split apps; populate models.py in current app.
