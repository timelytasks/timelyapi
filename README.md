[![Maintainability](https://api.codeclimate.com/v1/badges/79daa362a5568b87ebd8/maintainability)](https://codeclimate.com/github/timelytasks/timelyapi/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/79daa362a5568b87ebd8/test_coverage)](https://codeclimate.com/github/timelytasks/timelyapi/test_coverage)

| branch  | status |
|---------|--------|
| master  | [![Build Status](https://travis-ci.com/timelytasks/timelyapi.svg?branch=master)](https://travis-ci.com/timelytasks/timelyapi)|
| dev | [![Build Status](https://travis-ci.com/timelytasks/timelyapi.svg?branch=development)](https://travis-ci.com/timelytasks/timelyapi)|

# timelyapi

A to do list API with timer (WIP) and calendar (WIP) integration (something like gantt)

## Project setup

### Via docker

```shell
docker-compose up
```

### Via pip

```shell
pip install -r requirements.txt
```

### Run development

```shell
invoke run
```

### Lints and tests

```shell
invoke t
```

# Planning

## Project

- Title
- List of tasks - [Task, Task, ...]
- Assignees
- Date created
- Due date

## Task

- Title
- Assignee
- Creator
- Date created
- Priority
- Time needed
- Time spent https://stackoverflow.com/questions/5259882/subtract-two-times-in-python/38245441#38245441
- Reminder
- Due Date
- Comments

https://docs.python.org/3/library/datetime.html
https://docs.python.org/3/library/time.html

## User

- name
- username
- email
- Password

## Timer

- task
- time
- countdown
- distractions

# Interesting reads

https://stackoverflow.com/questions/49482453/generics-vs-viewset-in-django-rest-framework-how-to-prefer-which-one-to-use

https://stackoverflow.com/questions/46125398/how-to-display-only-values-in-django-serializers

https://www.peterbe.com/plog/efficient-m2m-django-rest-framework

https://stackoverflow.com/questions/46125398/how-to-display-only-values-in-django-serializers

https://hakibenita.com/django-rest-framework-slow
