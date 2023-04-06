# greysend_website

## Set Up Your Own Development Environment

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

# Meeting minutes

**_Week 1 Thurs Meeting:_**

1.want a project that highlights user engagement
2.leveraging the admin components
3.multiple micro-services - more modular
4.Chop up the project to take on different parts
5.5-week project?
6.Kathrin - interest in testing
7.Asynchronous parts
8.Authorization and database design - Tianci (app architecture)
9.Database design - Nikki
10.UI - katharin / Tom

**Chat Features of Graysend**

1.1:1 chat
2.logging in
3.Identity/user profile
4.messages in text
5.Authorization (Tianci)
6.state of message: Read vs. unread and backlog
7.database design

**Goal for next week:**

1.decide on who is owning what part 2. ~~weigh venv vs. docker vs. poetry~~

**Task:**

~~Blake to create skeleton repo and share with group~~
NIkki and Tianci to draft initial database design statement - with database type
~~Tianci to start awesome Django thread!!!~~
~~Kathrin to share the ADR sample~~
Tom to look into Poetry
ALL look through relevant tutorials

**_Week 2, Monday Pairing:_**

1. Thank you Enric for lending us your smart brain!
2. Blaked drove us through setting up Docker.
3. We ran into a problem where the local browser is 404 yet the container is telling us that the development server is up. We tried switching ports exposure configurations all kinds of ways to no avail. Then we realized that it was an error in the `CMD` section of the Dockerfile, where instead of setting "127.0.0.1:8000" directly, we should've used the generic "0.0.0.0:8000"
4. Enric told us about the magic of `curl` and stripping everything away to reproduce the minimum functionality and then slowly building things back up as a way to debug.

**_DB brainstorm_**
&& - not too important

Users - User_ID, first_name, last_name, nick_name, DOB

[Django might have it] Auth User - User ID, username, email, created_time (phone, etc)

Conversations - ID, created_time, &created_by&, archived(bool), admin_id

convo_participants - convo_id, user_id, tag

Messages - ID, text, sent_time, read_time, deleted, deleted_time, senderID, convo_ID

msgEmojis - Emoji_ID, message_ID, placed_by (userID)

Emojis - Emoji_ID, image

Convo_tags - tag_ID, convo_ID, user_ID

tags - tag_id, tag_text, user_ID(nullable), global(boolean)

Todo - many-to-many [user - convo] [convo - tags]

### Today's meeting

- Poetry
- Version Control
- Data Structure
- ML Extension
- Separating the apps
