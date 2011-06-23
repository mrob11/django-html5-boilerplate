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
* A <span style="text-decoration: line-through">slightly</span> now less modified version of the HTML5 Boilerplate
* django.contrib.staticfiles url conf set up for serving static media
* A `settings_local.py.ex` template file that allows you to set environment-specific settings
* A `test_all.py` script that allows you to run the unit tests for all applications in INSTALLED_APPS


## How to use the template

Using `pip` and `virtualenv` make it a lot easier to set up a new project using this boilerplate. A handy dandy requirements.txt file is included, 
so when you've downloaded a copy of this boilerplate, just run `pip install -r requirements.txt` from the project directory and away you go.

When you're finished installing requirements, you'll need to set up your settings\_local.py file:

        # set path
        cd <path-to-project>/
        
        # Rename the project folder 
        mv projectname <project_name>
        
        # copy settings_local.py
        cp settings_local.py.ex settings_local.py
        
        # Edit settings_local.py
        vi settings_local.py
        



