# DOCKER-DJANGO-MICROSERVICE-BOILERPLATE
A Django boilerplate to make the process of creating serializers, views, and urls EASIER.

# Getting Started
## Prerequisites
What things you need to install the software and how to install them
1. [Git](https://git-scm.com/)
2. [Python](https://www.python.org/)


### CLONING 
 ```bash 
    git clone https://github.com/RadySonabu/DJANGO-MICROSERVICE-BOILERPLATE
 ```
### CREATING AN APP
1. Create a folder inside of APPS
2. Instead of using
```python
   python manage.py startapp <name_of_you_app>
```
Use
```python
   python manage.py startapp apps apps/<name_of_you_app>
```

3. Add it to the settings.py (config/base)

# After creating a model run
```python
   python manage.py viewset <name_of_your_app>
```
to generate serializers, viewsets, and urls


### Add the urls to the main.urls
