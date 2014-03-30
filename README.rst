.. {% comment %}

========================
Django HTML5 Boilerplate
========================

#TODO: add a link to Starting a Django-1.6 Project...
This modification of Mike360's django-html5-boilerplate app incorporates
certain 'best practices' from Jeff Knupp's tutorial "Starting a Django-1.6 Project
the Right Way". The following modifications were made:

   - a fabric file was added (this is in generic form, and should be modified
     for your individual project).

   - INSTALLED_APPS was broken up into three app directories, for default,
     third-party and local apps, respectively.

   #TODO: add links for fabric and south.
   - fabric and south were added into the third-party directory (although
     commented out, to allow them be synced properly). The south module is
     useful for data migrations, while the fabric module helps with deployment.

   - a test file was added within the project module, also in generic form.
     It is named test_project_name.py; you will hanve to rename it manually to
     test_(whatever your project_name is).


This is a starting template for Django website projects with `HTML5 Boilerplate <http://html5boilerplate.com>`__ integrated. To get started, create a ``virtualenv``, install Django, and then use Django's ``startproject`` command and specify the template (replace project_name with the name of your project) ::

    virtualenv project_name
    source project_name/bin/activate
    pip install Django
    django-admin.py startproject --extension=py,ex,rst --template=https://github.com/mike360/django-html5-boilerplate/zipball/master project_name

After creating the project you can start up the development server right away. ::

    python manage.py runserver 0:8000

Now you'll need to configure your database. Open up ``settings/dev.py`` and configure your local settings (database, etc.) I go into more detail about the way settings are handled in the Settings Module.

The Settings Module
-------------------

In this settings module setup, all settings are stored and versioned under the ``settings/`` folder in the root of the project folder. All of the global and common settings are stored in ``settings/base.py`` and anything environment specific should be in a separate file that imports from base. There is a ``settings/dev.py`` file included, and it is the default `DJANGO_SETTINGS_MODULE` as specified in the ``wsgi.py`` file.

A template for subsequent environments (e.g. staging, production) is included in ``settings/environment.py.ex``. In order to make use of those files you'll need to override the ``DJANGO_SETTINGS_MODULE`` environment variable set in ``wsgi.py`` and ``manage.py`` in your specific server environment. This is handled in various ways depending on your environment. It is a good practice to keep the other environments' settings files versioned as well.

This method of handling settings is great for the solo developer who needs to manage multiple deployment environments. It's ready out of the box to run well this way. When a project has multiple developers, each developer should maintain their own local settings file and exclude it from source control. This template can handle that with a couple of tweaks.

=======

.. note:: The text following this comment block will become the README.rst of the new project.

-----

.. {% endcomment %}

{{ project_name }}
======================

Quickstart
----------

To bootstrap the project::

    virtualenv {{ project_name }}
    source {{ project_name }}/bin/activate
    cd path/to/{{ project_name }}/repository
    pip install -r requirements.txt
    manage.py syncdb

