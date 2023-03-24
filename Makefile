## TODO: make this a bash or python script

down:
	docker compose down --volumes --remove-orphans && (rm dags/.airflowignore || true)

run:
	make down && (rm dags/.airflowignores || true) && docker compose up

down-celery:
	docker compose down -f docker-compose.feat23.celery.yml --volumes && (rm dags/.airflowignore || true)

stop:
	docker compose stop