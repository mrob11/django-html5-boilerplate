# Django HTML5 Boilerplate

## Introduction

This is a starting template for Django website projects with [HTML5 Boilerplate](http://html5boilerplate.com) integrated.

## How to use the template

Using `pip` and `virtualenv` makes it a lot easier to set up a new project using this boilerplate. If you're unfamiliar with virtualenv, I've found a [few](http://jmoiron.net/blog/deploying-django-mod-wsgi-virtualenv/) [good](http://www.clemesha.org/blog/modern-python-hacker-tools-virtualenv-fabric-pip) [reads](http://mathematism.com/2009/07/30/presentation-pip-and-virtualenv/) explaining the concept.

Start by creating your virtual environment (I'm using [Doug Hellman's virtualenvwrapper](http://www.doughellmann.com/projects/virtualenvwrapper/)):

```
mkvirtualenv projectname
```

Replace 'projectname' with your desired environment name.

Install Django:

```
pip install Django
```

When you're finished installing Django, create a new project using the `startproject` command with the --template argument:

```
django-admin.py startproject <project_name> --template=https://github.com/mike360/django-html5-boilerplate/tarball/master
```

The above command will work, but GitHub's automatic tarballing of a repository is going to cause the project to be created in an ugly subfolder. To avoid that, you can clone a copy of this repo and then pass the path of the cloned repo to `startproject`:

```
git clone https://github.com/mike360/django-html5-boilerplate/
django-admin.py startproject <project_name> --template=django-html5-boilerplate/
```

After creating the project you can boot up the development server right away:

```
python manage.py runserver
```

Then open up your browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000) -- if all went well you should see the "Hello world!" page.

Now you'll need to configure your database. Open up `settings/dev.py` and configure your local settings (database, etc.) I go into more detail about the way settings are handled in the Settings Module 

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}
```

Now you're ready to run `syncdb`. This will set up your database, and since the Django Admin is included by default in this template, you'll go through the initial super user setup.

```
python manage.py syncdb
```

Once that's completed you can boot up the dev server again:

```
python manage.py runserver
```

The Django Admin is automatically included with this project, so now you can head to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and log in using the credentials you created in the `syncdb` step.

* * * 

## The Settings Module

After some reading and tinkering, I've abandoned the old `settings_local.py` file that was ignored in the repo in past versions of django-html5-boilerplate. Too many things can go wrong when your settings aren't version controlled. This new way of handling settings is much more manageable in my opinion, and in the opinion of [a](http://lincolnloop.com/django-best-practices/projects.html#settings) [few](http://rdegges.com/the-perfect-django-settings-file) [others](http://ericholscher.com/blog/2011/jan/10/handling-django-settings-files/). I've based the settings module after the opinions found in those links, with some tweaks of my own.

In this new settings module, all settings are stored and versioned under the `settings/` folder in the root of the project folder. All of the global and common settings are stored in `settings/base.py` and anything environment specific should be in a separate file that imports from base. There is a `settings/dev.py` file included, and it is the default `DJANGO_SETTINGS_MODULE` as specified in the `wsgi.py` file.

A template for subsequent environments (e.g. staging, production) is included in `settings/environment.py.ex`. In order to make use of those files you'll need to override the `DJANGO_SETTINGS_MODULE` environment variable set in `wsgi.py` and `manage.py` in your specific server environment. This is handled in various ways depending on your environment. It is a good practice to keep the other environments' settings files versioned as well.

This method of handling settings is great for the solo developer who needs to manage multiple deployment environments. It's ready out of the box to run well this way. When a project has multiple developers, each developer should maintain their own local settings file and exclude it from source control. This template can handle that with a couple of tweaks.
