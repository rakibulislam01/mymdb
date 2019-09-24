#!/usr/bin/env bash
# shellcheck disable=SC1009
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE DATABASE mymdb;
    CREATE USER mymdb;
    GRANT ALL ON DATABASE mymdb TO "mymdb";
    ALTER USER mymdb PASSWORD 'mymdb';
    ALTER USER mymdb CREATEDB;
EOSQL

