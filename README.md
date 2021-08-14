# Youtube-API

This is a project to create an API to fetch the videos , on a predefined query (query used here is "official"), which are uploaded on YouTube. The results are sorted in reverse chronological order of their publishing datetime.

It makes use of the [YouTube API v3](https://developers.google.com/youtube/v3/docs/search/list) to fetch the results in an asynchronous manner, and store it in an sqlite database.
To fetch and store the results in async manner, [django-cron](https://django-cron.readthedocs.io/en/latest/introduction.html) is used to create a cron job for the requirement.
The API is based on [Django REST Framework(DRF)](https://www.django-rest-framework.org)

## Setup Guide

This project assumes you have a working python environment, which supports virtual environments. It is assumed that `pip` is used virtual environment handling, but `conda` can also be used. User then need to handle the package installations, as applicable.

* Clone the project.
* Create and activate a pip virtualenv.
* Install all required dependencies using `pip install -r requirements.txt`
* In `youtube_api.settings.py`, you need to add the API keys, in the list specified under the variable `API_KEYS`.
* Initialize the database using the commands: `python manage.py makemigrations api` and `python manage.py migrate`
* Start the cron job using `python manage.py runcrons`
* Start the server on http://127.0.0.1:8080 using `python manage.py runserver`

## Future Scope
* Create a nice frontend to display the responses
* Use Celery+Redis instead of django-cron to fetch the results[(WIP branch)](https://github.com/sashank27/Youtube-API/tree/celery_redis)

## Author
* Sashank Mishra ([@sashank27](https://github.com/sashank27))

## Screenshots

[Link](https://github.com/sashank27/Youtube-API/tree/master/media)