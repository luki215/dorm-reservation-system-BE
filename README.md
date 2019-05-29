# Installation
This project requires [VSCode insiders](https://code.visualstudio.com/insiders/)
## Installing new pypi packages
- add the package name in `requirements.txt`
- `docker-compose build` in non-remote session
- in remote session vscode run `rebuild container` action
# Development
## Services
`adminer.dorms.localhost` - [Adminer](https://www.adminer.org/cs/) instance for managing and displaying DB
`api.dorms.localhost` - running BE app
## Database
In python console run:
- `import app.database`
- `app.database.init_db()` to init the database and create tables
- `app.database.seed_data()` to insert into db seed data