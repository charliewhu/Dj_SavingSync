# Django Project Template

Readymade Django project, complete with:
* Poetry ✅
* Gitignore ✅
* Github Actions ✅
* Custom User model ✅
* Folder restructure ✅
* Static setup ✅
* Environs[django] ✅
* Behave-django for BDD ✅
* Playwright ✅
* pytest-playwright ✅
* Model-Bakery ✅
* Psycopg2 ✅
* Gunicorn ✅
* Dockerfile ✅
* docker-compose ✅
* Nginx ✅

## Creating a project

```bash
// clone repo
mkdir your_folder_name
cd your_folder_name
git clone https://github.com/charliewhu/Dj_Project_Template.git .

// OPTIONAL: install dependencies locally
// this is only required for module intellisense to work
poetry install

// run type check
docker-compose run type_check

// run unit tests
docker-compose run unit_test

// run e2e tests
docker-compose run e2e_test

// run development server
docker-compose up

// run nginx server
docker-compose -f docker-compose.prod.yaml up
```
