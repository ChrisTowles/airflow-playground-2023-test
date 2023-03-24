# run `make` to see the list of available commands
#
## TODO: make this a bash or python script

down:
	docker compose down --volumes --remove-orphans && (rm dags/.airflowignore || true)

run:
	make down && (rm dags/.airflowignores || true) && docker compose up

stop:
	docker compose stop