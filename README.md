# Bot for parse news and notify users
Bot parses news about Boston Celtics and sends it to users that subscribed to mailing
Users can subscribe/unsubscribe to mailing.

## Project Libs
* Python
* aiogram
* Gino
* BeautifulSoup
* PostgreSQL
* Docker(docker-compose)

## Install and Run
1. `git clone https://github.com/SaD-Pr0gEr/TG-bot-for-newsletter.git`
2. `pip install -r requirements.txt`
3. Apply migrations`
   alembic upgrade head
   `
6. `python3 run.py`

## Alembic
* Create migrations `alembic revision --autogenerate -m 'migration name'`
* Apply migration `alembic upgrade head`

## Docker 
1. Build `docker compose build`
2. Up `Docker compose up`
3. Enter into container `docker exec -it container_name bash`
4. run `alembic upgrade head` or write it on docker-compose.yml as command
