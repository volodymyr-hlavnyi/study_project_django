UID := $(shell id -u)
export UID

.PHONY: d-work-i-run
# Make all actions needed for run homework from zero.
d-work-i-run:
	@make init-configs &&\
	make d-run

.PHONY: d-work-i-run-dev
# Make all actions needed for run homework from zero.
d-work-i-run-dev:
	@make init-configs-dev &&\
	make d-run-dev

.PHONY: d-work-i-run-dev-local
# Make all actions needed for run homework from zero.
d-work-i-run-dev-local:
	@make init-configs-dev &&\
	make d-run-dev-local

.PHONY: d-work-i-run-d
d-work-i-run-d:
	@make init-configs &&\
	make d-run-d

.PHONY: d-work-i-purge
# Make all actions needed for purge homework related data.
d-work-i-purge:
	@make d-purge

.PHONY: init-configs
# Configuration files initialization
init-configs:
	@@cp .env.prod .env && \
	cp docker-compose.override.prod.yml docker-compose.override.yml


.PHONY: init-configs-dev
# Configuration files initialization
init-configs-dev:
	@cp .env.dev .env && \
	cp alembic.dev.ini alembic.ini && \
	cp docker-compose.override.dev.yml docker-compose.override.yml


.PHONY: d-run-d
# Just run
d-run-d:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker compose up --build -d

.PHONY: d-run
# Just run
d-run:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker compose up --build

.PHONY: d-run-dev
# Just run
d-run-dev:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		COMPOSE_PROFILES=local_dev \
		docker compose up --build


.PHONY: d-run-dev-local
# Just run
d-run-dev-local:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
	    COMPOSE_PROFILES=pg_only \
		docker compose up --build

.PHONY: d-stop
# Stop services
d-stop:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker compose down

.PHONY: d-purge
# Purge all data related with services
d-purge:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker compose down --volumes --remove-orphans --rmi local --timeout 0


.PHONY: init-dev
# Init environment for development
init-dev:
	@pip install --upgrade pip && \
	pip install --requirement requirements/local.txt && \
	pre-commit install

.PHONY: work-i-run
# Run work.
work-i-run:
	@python app.py

.PHONY: work-i-purge
work-i-purge:
	@echo Goodbye


.PHONY: pre-commit-run
# Run tools for files from commit.
pre-commit-run:
	@pre-commit run

.PHONY: pre-commit-run-all
# Run tools for all files.
pre-commit-run-all:
	@pre-commit run --all-files

.PHONY: update-db
# update db local
# 1.
# alembic revision --autogenerate -m "202407041704 Change id autoincrement"
update-db:
	@alembic revision --autogenerate -m "20240721_1320 Change name table Congregation" && \
	alembic upgrade head && \
	python3 update-db.py

.PHONY: d-update-db
# update db in docker
d-update-db:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
        docker exec -it attendants-app-1 alembic upgrade head && \
        docker exec -it attendants-app-1 python update-db.py

.PHONY: d-update-db-29108
# update db in docker
d-update-db-29108:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
        docker exec -it attendants_29108-app-1 alembic upgrade head && \
        docker exec -it attendants_29108-app-1 python update-db.py

.PHONY: d-create-admin
# update db in docker
d-create-admin:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
        docker exec -it attendants-app-1 python application/services/create_admin.py

.PHONY: create-admin-db
# Update db in docker
create-admin-db:
	export USER1=admin PASSWORD1=admin_password && \
	python application/services/create_admin_db.py --user $$USER1 --password $$PASSWORD1

.PHONY: restore-db
# Restore db in docker
restore-db:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
	docker cp db/2024_07_19_29108_pg.dump attendants-postgres-1:/var/lib/postgresql/data/ && \
	docker exec -it attendants-postgres-1 pg_restore -U admin -d postgres_db /var/lib/postgresql/data/2024_07_19_29108_pg.dump
