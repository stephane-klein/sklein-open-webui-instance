# sklein Open WebUI instance

This repository contains installation scripts for my personal instance of [Open WebUI](https://github.com/open-webui/open-webui).

Connected models:

- https://openrouter.ai
- [Scaleway Generative APIs](https://www.scaleway.com/fr/generative-apis/)

The Open WebUI ["Pipelines"](https://github.com/open-webui/pipelines) service is installed and configured.

More information, see french note: https://notes.sklein.xyz/Projet%2030/

## Preparation

Install [Mise](https://mise.jdx.dev/)

```sh
$ cp .secret.skel .secret
```

Then fill in the `.secret` file with a [Scaleway](https://scaleway.com) API Key that has access permission to the [Scaleway Generative APIs](https://www.scaleway.com/fr/generative-apis/) service.


## Getting started

```sh
$ mise install
$ pip install -r requirements.txt
```

If needed, you can force the environment variables loading with this command:

```sh
$ source .envrc
```

Before starting installation, you can check if the API access tokens work properly:

```
$ ./scripts/check-scaleway-connection.sh
$ ./scripts/check-openrouter-connection.sh
```

```sh
$ ./scripts/create-minio-bucket.sh
$ docker compose up -d --wait
$ ./scripts/create-admin-user.sh
$ ./scripts/create-stephane-klein-user.sh
$ cat openwebui-config.json | ./scripts/openwebui-config-import.sh
```

Open your browser on http://localhost:3000 (admin email: `contact+admin@stephane-klein.info`, password: see `OPEN_WEBUI_ADMIN_PASSWORD`)

## How to import / export json configuration file

Import configuration:

```sh
$ cat openwebui-config.json | ./scripts/openwebui-config-import.sh
```

Export configuration:

```sh
$ ./scripts/openwebui-config-export.sh > openwebui-config.json
```

## Import Open WebUI functions

Le scripts suivant importe et active les functions Open WebUI présents dans le dossiers [`./functions/`](functions/):

```sh
$ ./scripts/openwebui-functions-sync.py
```

## Pipelines Examples and « hot reload »

The *pipelines* contained in the [`./pipelines/`](./pipelines/) folder are automatically loaded when the container starts (`docker compose up -d` or `docker compose restart pipelines`).

This folder contains a *pipeline* named [`hello_world.py`](./pipelines/hello_world.py).

You can reload the pipelines "on the fly" with the following command:

```sh
$ ./scripts/reload-pipelines.sh
```

## Helper scripts

Helper script to directly enter into the PostgreSQL database:

```sh
$ ./sripts/enter-in-pg.sh
postgres=# \dt
              List of relations
 Schema |       Name       | Type  |  Owner
--------+------------------+-------+----------
 public | alembic_version  | table | postgres
 public | auth             | table | postgres
 public | channel          | table | postgres
 public | channel_member   | table | postgres
 public | chat             | table | postgres

...

 public | prompt           | table | postgres
 public | tag              | table | postgres
 public | tool             | table | postgres
 public | user             | table | postgres
(23 rows)

postgres=#
```

Helper script to explore Minio Object Storage:

```sh
$ ./scripts/aws-s3-local-minio.sh s3 ls openwebui --recursive
2025-04-26 12:36:39        682 openwebui/2b12371e-44b0-402e-985f-4cb736c12396_README.md
2025-04-26 12:38:04       2386 openwebui/6a86139c-83f9-4521-a99a-264ac260e11f_README.md
```

Helper script to explore Redis data:

```sh
$ ./scripts/enter-in-redis.sh
127.0.0.1:6379[1]> keys *
1) "open-webui:session_pool"
2) "open-webui:user_pool"
3) "usage_cleanup_lock"
```

## Teardown

```sh
$ docker compose down -v
```
