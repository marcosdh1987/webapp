# WebAPP - dashboard  template

## Project summary

This is a template to create Django webapp for dashboarding.

Includes:

- login module
- dashboard example

## Prerequisites

- Python 3.6
- Cookiecutter

## Create your copy of the project via cookiecutter

```
$ pip install cookiecutter
```

clone the template
```
$ cookiecutter https://github.com/marcosdh1987/webapp.git
```

# Local Usage
## Create virtual environment

### for windows:
```
python -m venv env
./Scripts/activate
```

### for ubuntu/mac:
```
$ sudo apt-get install python3-pip

$ sudo pip install virtualenv 

$ virtualenv venv 

$ source venv/bin/activate
```

## Install Requirements

```
pip install -r requirements.txt
```

### Pre-run steps

```
$ python manage.py collectstatic
$ python manage.py migrate
$ python manage.py createsuperuser

```

## Run de aplicacion in a dev mode (use debug = true)

```
python manage.py runserver
```

# Using docker

## Prerequisites

- Docker

```
$ docker build -t imagename .
$ docker run -d -p 8000:8000 imagename
```


# Deployment result

![Login](static/img/1.png)
![Dashboard](static/img/2.png)







