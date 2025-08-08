# Aiogram Telegram Bot Template 

Temegram Bot Template.

## Description

### Startup point

./app.py is the startup point.

### Database

I use postgres in docker with full dsn string in .env file for connection.

	•	I define database models in ./bot/database/models/db_table_{table_name}.py
	•	The Base object is created in ./bot/database/db_base.py
	•	The database is initialized in ./bot/database/init_db.py, including:
	    •	Creating the engine and session
	    •	Creating all tables
	•	In app.py, I load the config and initialize the database by calling the engine, session factory, and table creation logic
	•	I pass the session factory to the bot using await main(config, session_factory)
	•	To use the session inside handlers, I created a middleware (./bot/middlewares/db_session.py) that processes Telegram updates and injects a database session into the handlers using:
dp.update.outer_middleware(DbSessionMiddleware(session_factory))
	•	Finally, I store database-related logic (CRUD operations) in ./bot/database/models/db_requests.py, which I use inside the handlers

### Internationalization and Localization

I use Fluentogram for localization.

	•	In ./bot/locales/{locale_name}/LC_MESSAGES/txt.ftl, I define message variables like command-start = Hello!
	•	I created a middleware at ./bot/middlewares/i18n.py and added it to the dispatcher in bot.py using:
dp.update.middleware(TranslatorRunnerMiddleware())
	•	After an update is received, the middleware detects the user’s locale and provides the appropriate translation dictionary to the handler via translator_hub
	•	In TranslatorRunnerMiddleware, you can define custom logic to determine the user’s language by:
	•	Checking the user’s locale from the Telegram update
	•	Querying the user’s preferred language from the database
	•	Using a cached value or checking via FSM, etc.
	•	If the user’s locale is not found in the locales folder, the default fallback is the English (en) locale

## Getting Started

### Dependencies

- Python 3.10
- Docker Engine
- Check pyproject.toml for dependencies

### Installing

- Install docker;
- Install docker-compose;
- Clone repository with:
```shell
git clone https://github.com/IronRom/aiogram-bot-template.git
```
- Install denepdencies:
```shell
poetry install --no-interaction --no-cache --no-root  
```
- Insert bot token and database dsn string into .env file(use .env.example) for example

### Executing program

To run bot we need to perform a few simple steps:

- cd into apps folder:
```shell
cd aiogram-bot-template
```

Method 1(just database in container):

- Run database container with:
```shell
docker-compose --profile=infrastructure up -d
```
- Run the bot:
```shell
poetry run python app.py
```

Method 2(all in containers):

- Run all modules in containers:

```shell
docker-compose --profile=full up -d
```


## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info

ex. Dominique Pizzie  
ex. [@DomPizzie](https://twitter.com/dompizzie)

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)