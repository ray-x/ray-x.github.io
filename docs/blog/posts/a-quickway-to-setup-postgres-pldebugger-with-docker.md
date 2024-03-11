---
layout: post
template: blog_post.html
title: "Setup postgres debugger env with docker"
subtitle: 'debug pl/sql with docker and dbeaver'
author: "Ray"
header-style: text
tags:
  - Docker Postgres
date: 2020-06-14
---
## pldebugger setup
pldebugger require recompile with postgresql source code. A little bit hard to setup.
Lucky enough, debian provides already compiled version.
Strech: version 10
Buster: version 12

```Dockerfile
FROM postgres:12

MAINTAINER ray@ray-x
ENV PG_MAJOR 12
ENV PG_VERSION 12.3-1.pgdg100+1

# Install the postgresql debugger
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
  postgresql-$PG_MAJOR-pldebugger


EXPOSE 5432

```


Start the docker and you should see:

``` log
pgdbg           |
pgdbg           | PostgreSQL Database directory appears to contain a database; Skipping initialization
pgdbg           |
pgdbg           | 2020-06-11 03:00:46.211 UTC [1] LOG:  starting PostgreSQL 12.3 (Debian 12.3-1.pgdg100+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 8.3.0-6) 8.3.0, 64-bit
pgdbg           | 2020-06-11 03:00:46.211 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
pgdbg           | 2020-06-11 03:00:46.211 UTC [1] LOG:  listening on IPv6 address "::", port 5432
pgdbg           | 2020-06-11 03:00:46.214 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
pgdbg           | 2020-06-11 03:00:46.290 UTC [26] LOG:  database system was shut down at 2020-06-21 03:00:32 UTC
pgdbg           | 2020-06-11 03:00:46.314 UTC [1] LOG:  database system is ready to accept connections

```

Notes that the logs began with `pgdbg` instead of `postgres`

To debug with  dbeaver, install extension :

```sql
CREATE EXTENSION pldbgapi;
```

Install debug extension in dbeaver (if not yet)

`Help -> Install new software`
![dbeaver install](https://raw.githubusercontent.com/ray-x/ray-x.github.io/master/img/2020-06-install-plugin.jpg)
Search and install `debugger`  Click "ok", "accept", "confirm"... to install
After restart dbeaver, you should see a debug icon:
![DebugIcon](https://raw.githubusercontent.com/ray-x/ray-x.github.io/master/img/2020-06-debug-beaver.jpg)


Create a demo sql:

``` sql
CREATE SCHEMA test;
DROP function if exists test.somefunc(var integer);
CREATE FUNCTION test.somefunc(var integer) RETURNS integer AS $$
DECLARE
   quantity integer := 30+var;
BEGIN
   RAISE NOTICE 'Quantity here is %', quantity;      --在这里的数量是30
   quantity := 50;
   --
   -- 创建一个子块
   --
   DECLARE
      quantity integer := 80;
   BEGIN
      RAISE NOTICE 'Quantity here is %', quantity;   --在这里的数量是80
   END;
   RAISE NOTICE 'Quantity here is %', quantity;      --在这里的数量是50
   RETURN quantity;
END;
$$ LANGUAGE plpgsql;

SELECT test.somefunc(12);

```

Configure a debug session:
Specify database, function, aurgument:
![Debug config](https://raw.githubusercontent.com/ray-x/ray-x.github.io/master/img/2020-06-debug-config.jpg)

Start debug
![debug window](https://raw.githubusercontent.com/ray-x/ray-x.github.io/master/img/2020-06-debug-window.jpg)
