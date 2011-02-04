# Django HTML5 Boilerplate

## Introduction

This is a starting template for Django website projects using (a slightly modified version of)
[Paul Irish's HTML5 Boilerplate](http://html5boilerplate.com).


## Features

* A Django project skeleton
* A slightly modified version of the HTML5 Boilerplate
* Custom development url patterns that allow Django to serve static media files in development
* A `settings_local.py.ex` template file that allows you to set environment-specific settings
* A `test_all.py` script that allows you to run the unit tests for all applications in INSTALLED_APPS
* Included the [960 grid system](http://960.gs), both 12 and 24 column versions. 24 column is integrated with base template.


## HTML5 Boilerplate Modifications

Following are the modifications I've made from the original HTML5 Boilerplate (v0.9.5).
Some modifications are for Django-specific reasons, others are just personal preference.

* Upgraded jQuery to v1.5
* Upgraded Modernizr to v1.6
* Removed the profiling JavaScript code (since I don't often make use of it)
* Removed the `plugins.js` and `scripts.js` file and replaced with `projectname.js`.
* I've included the `crossdomain.xml` file for Flash but serving it needs to be configured. I don't work with Flash so haven't bothered.
* Removed `nginx.conf` and `web.config` since I run Apache for my production environment.
* Removed `.htaccess` from the template only. I include it in my production environment deployment though.
* Renamed the `style.css` file to `reset.css` since that's essentially how I'm treating it - as a CSS reset. For readability/navigability in development I'd rather have it in a separate file.


## How to use the template

This template assumes that your 3rd party, project-specific application code will reside in the `src/` folder. You would then place symbolic links to the app code in the `lib/` folder. 
It will still work with code living elsewhere on your `PYTHONPATH` but the idea is that your development environment shouldn't be tied to a specific version of Django (or any other app for that matter).
This setup allows you to have project-specific versions of 3rd party code included in the project's repository.

1. Download a copy of the django-html5-boilerplate template to your development environment
1. Download a copy of the Django framework and place it in the `src/` folder.
1. Place a symlink to the Django app folder in your `lib/` folder.
    
        cd <path_to_project>/lib
        ln -sf ../src/<django_folder_name>/django
        
1. Set your PYTHONPATH environment variable

        export PYTHONPATH=.:..:../lib/:$PYTHONPATH

1. Follow the rest of this script:
    
        # set path
        cd <path-to-project>/
        
        # Rename the project folder 
        mv projectname <project_name>

        # copy settings_local.py
        cp settings_local.py.ex settings_local.py

        # Edit settings_local.py
        vi settings_local.py

        DATABASES = {
            'default': {
                'ENGINE': '',                           # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
                'NAME': '',                             # Or path to database file if using sqlite3.
                'USER': '',                             # Not used with sqlite3.
                'PASSWORD': '',                         # Not used with sqlite3.
                'HOST': '',                             # Set to empty string for localhost. Not used with sqlite3.
                'PORT': '',                             # Set to empty string for default. Not used with sqlite3.
            }
        }
    
        # Run the tests. Make sure they all pass
        ./test_all.py
    
        # start dev server
        ./manage.py runserver 0:8000



