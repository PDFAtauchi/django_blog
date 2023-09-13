# Django Blog Website

Our project aims to create a dynamic and engaging blog website that caters to a diverse audience interested in various topics. Whether you're passionate about travel, food, technology, or any other subject, our blog website will provide a platform for authors to share their insights, experiences, and expertise.

# Setup


## Pre-requisites
```markdown
- Install python >= 3.8
- Install pip >= 22
- Install poetry
- Install [docker](https://docs.docker.com/engine/install/ubuntu/)
- Optional, Install [docker desktop](https://docs.docker.com/desktop/install/linux-install/)
```

# Pre-initial
clone project
```console
$ git clone https://github.com/PDFAtauchi/django_blog.git
```

Install in system [Pre-commit](https://pre-commit.com/#3-install-the-git-hook-scripts)
```console
$ pip install pre-commit
$ pre-commit install
```

Install [Commit-msg](https://pre-commit.com/#pre-commit-for-commit-messages)

```console
$ pre-commit install --hook-type commit-msg
```

## Development

 To build images
```console
$ docker-compose up -d --build
$ docker-compose -f docker-compose.prod.yml up -d --build
```


To Start App
```console
$ docker-compose up -d
$ docker-compose down | -v
```

To execute Lint (Pylint)
```console
$ docker-compose exec web poetry run pylint_runner --rcfile=.pylintrc
```

To check format(black)
```console
$ docker-compose exec web poetry run black . --check  -v --diff --color
```

To check sort import (isort)
```console
$ docker-compose exec web poetry run isort . --check-only --settings-path pyproject.toml
```

To Check security in requirements (safety)
```console
$ docker-compose exec web poetry run safety check
```

To Check securities issues (bandit)
```console
$ docker-compose exec web poetry run bandit --ini .bandit -r -x="apps/tests"
```

To run tests (pytest)
```console
$ docker-compose exec web poetry run pytest apps/tests
```

pytest-xdist (concurrency)
```console
$ docker-compose exec web poetry run pytest -n auto apps/tests
```

pytest-rerun (to check flaky tests)
```console
$ docker-compose exec web poetry run pytest -n auto apps/tests --reruns 10
```


To run Coverage (pytest-coverage)
```console
$ docker-compose exec web poetry run pytest --cov=. --junitxml=test-results/junit.xml
$ docker-compose exec web poetry run pytest html
```

## Additionals
Conventional commits
```markdown
$  For commits use this [convention](https://www.conventionalcommits.org/en/v1.0.0/)
```

To see cyclomatic complexity
 ```console
$ docker-compose exec web poetry run radon cc apps/blog/views.py
```

To enter container
 ```console
$ sudo docker exec -ti container_name sh
```

To enter container
Default and django-extensions shell
 ```console
$ docker-compose exec web python manage.py shell
$ docker-compose exec web python manage.py shell_plus
```
# Populating Data

## users
- docker-compose exec web python manage.py runscript populate_data


# Debugging
## Command line

### In Test Code
To enter container
 ```console
- pytest.set_trace()  (breakpoint)
- docker-compose exec web poetry run pytest path_test --pdb | path_test can be:
    - file e.g. apps/tests/test_assert_examples.py -
    - class e.g.  apps/tests/test_assert_examples.py::TestClassName
    - specific test inside a class e.g. apps/tests/test_assert_examples.py::TestClassName::test_specific_function
    - specific test e.g. apps/tests/test_assert_examples.py::test_specific_function
```

## In python code:
 ```console
- change import pytest; pytest.set_trace() to import pdb; pdb.set_trace() || breakpoint()
- To attach container
    - sudo docker attach $(docker-compose ps -q service_name)
- in the code: put
        - import pdb; pdb.set_trace()
        - make request(insomnia, postman, chrome, etc), in terminal  of attach, it enable the prompt of pbd
- exit: q
- Autocomplete on pdb: p variable_name (for globals and locals variables)
```

# PRs

- In PRs, always choose
[Squash and merge strategy](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/about-pull-request-merges)
- Choose the templates for PRs, as a better way to structure the PR information.
- Merge only if pipeline passed and you receive the approval of your teach lead.


# Enjoy Coding!!! :rocket:
