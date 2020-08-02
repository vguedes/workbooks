# Django and openpyxl example
[![<vguedes>](https://circleci.com/gh/vguedes/workbooks.svg?style=shield)](https://app.circleci.com/pipelines/github/vguedes/workbooks)
___

## Prerequisites
1. docker
1. docker-compose
## Starting the project
1. Clone this repo
1. Run `docker-compose run app python manage.py migrate`
1. Run `docker-compose run app python manage.py creaatesuperuser`
1. Run `docker-compose up`
1. Open `http://localhost:8000/admin/`
