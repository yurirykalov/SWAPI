CREATE SCHEMA IF NOT EXISTS stg;

CREATE TABLE IF NOT EXISTS stg.metadata(
    id uuid NOT NULL, -- synthetic PK: schema & table_name
    "schema" varchar NOT NULL DEFAULT 'stg', 
    table_name varchar NOT NULL , 
    last_loaded_id int NOT NULL, -- last loaded id in corresponding table
    updated_ts timestamp NOT NULL, 
    CONSTRAINT stg_metadata_pk PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS stg.people(
    id int NOT NULL, 
    payload jsonb, 
    updated_ts timestamp NOT NULL,
    CONSTRAINT stg_people_pk PRIMARY KEY (id)
);