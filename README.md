# Django HTML5 Boilerplate

## Introduction

This is a starting template for Django website projects using (a slightly modified version of)
[HTML5 Boilerplate](http://html5boilerplate.com).

As of version 0.3 I've migrated to the `virtualenv` way of working with Python projects. If you're unfamiliar, I've found some good reads here:

* http://jmoiron.net/blog/deploying-django-mod-wsgi-virtualenv/
* http://www.clemesha.org/blog/modern-python-hacker-tools-virtualenv-fabric-pip
* http://mathematism.com/2009/07/30/presentation-pip-and-virtualenv/


## Features

* A Django project skeleton
* A slightly modified version of the HTML5 Boilerplate
* django.contrib.staticfiles url conf set up for serving static media
* A `settings_local.py.ex` template file that allows you to set environment-specific settings
* A `test_all.py` script that allows you to run the unit tests for all applications in INSTALLED_APPS
* Included the [960 grid system](http://960.gs), both 12 and 24 column versions. 24 column is integrated with base template.


## How to use the template

Using `pip` and `virtualenv` make it a lot easier to set up a new project using this boilerplate. A handy dandy requirements.txt file is included, 
so when you've downloaded a copy of this boilerplate, just run `pip install -r requirements.txt` from the project directory and away you go.

I've included a few of the Django apps I often use in the requirements file:

* Django==1.3
* Fabric==1.0.1
* PIL==1.1.7
* South==0.7.3
* paramiko==1.7.6
* psycopg2==2.4.1
* pycrypto==2.3
* wsgiref==0.1.2

When you're finished installing requirements, you'll need to set up your settings\_local.py file:

        # set path
        cd <path-to-project>/
        
        # Rename the project folder 
        mv projectname <project_name>
        
        # copy settings_local.py
        cp settings_local.py.ex settings_local.py
        
        # Edit settings_local.py
        vi settings_local.py
        



