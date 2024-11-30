#!/usr/bin/bash

psql santa_workshop -c "\pset format unaligned" -c "\pset fieldsep ','" -f query.sql
