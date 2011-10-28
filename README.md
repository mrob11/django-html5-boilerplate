# Django HTML5 Boilerplate

## Introduction

This is a starting template for Django website projects using (a slightly modified version of)
[HTML5 Boilerplate](http://html5boilerplate.com).



## Features

* A Django project skeleton
* A <span style="text-decoration: line-through">slightly</span> now less modified version of the HTML5 Boilerplate
* django.contrib.staticfiles url conf set up for serving static media
* A `settings_local.py.ex` template file that allows you to set environment-specific settings
* A `test_all.py` script that allows you to run the unit tests for all applications in INSTALLED_APPS
* Requirements files for pip (details below)


## How to use the template

Using `pip` and `virtualenv` makes it a lot easier to set up a new project using this boilerplate. If you're unfamiliar with virtualenv, I've found a [few](http://jmoiron.net/blog/deploying-django-mod-wsgi-virtualenv/) [good](http://www.clemesha.org/blog/modern-python-hacker-tools-virtualenv-fabric-pip) [reads](http://mathematism.com/2009/07/30/presentation-pip-and-virtualenv/) explaining the concept.

Start by creating your virtual environment (I'm using [Doug Hellman's virtualenvwrapper](http://www.doughellmann.com/projects/virtualenvwrapper/)), by the way:

        mkvirtualenv projectname --no-site-packages

I've included two separate requirements files: 

* `requirements_min.txt` contains the minimum requirements to get this up and running
* `requirements_plus.txt` contains a few extra Python packages that I use in most of my projects (South, PIL, etc.)


Install one of the requirements files:

        pip install -r <requirements_min.txt or requirements_plus.txt>


When you're finished installing requirements, you'll need to set up your settings\_local.py file:

        # set path
        cd <path-to-project>/
        
        # Rename the project folder 
        mv projectname <project_name>
        
        # copy settings_local.py
        cp settings_local.py.ex settings_local.py
        
        # Edit settings_local.py
        vim settings_local.py
        

After you configure your local settings (database, etc.) you're ready to run `syncdb`:

        python manage.py syncdb

Once that's completed you can boot up the dev server:

        python manage.py runserver

Then open up your browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000) -- if all went well you should see the "It works!" page.


