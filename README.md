Collection of test problems (copf) is created on Django, DRF, Postgresql

Thanks for viewing the copf, it was created for learning and practice. Copf - a simple pet project

Build Status

Copf version 1.1

INSTALLATION

Please make sure the release file is unpacked under a Web-accessible directory. You shall see the following files and directories:

account/
payments/
posts/
starnavi/
.gitattributes
.gitignore
Dockerfile
docker-compose.yml
manage.py
requrements.txt


REQUIREMENTS

The minimum requirement by Copf is that your Web server supports Django 3.04 or above. Copf has been tested with the Django developmentserver in Manjaro Linux with Docker. Please access the following URL to check if your Web server reaches the requirements by Copf:

http://localhost:8080 (by default, it can be changed)

QUICK START

Copf starts from its root folder. The first you need to install migrations (django-admin.py migrate), then run server (manage.py runserver)
If you use Docker, just launch the command docker-compose up from the project directory
Constantine Yachnytskyi yachnytskyi1992@gmail.com
