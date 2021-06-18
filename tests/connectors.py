#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

import pathlib
from meerschaum import get_connector

conns = {
    'timescaledb': get_connector('sql', 'test_timescaledb',
        flavor='timescaledb', username='test', password='test1234', database='testdb',
        port=5439, host='localhost',
    ),
    'mariadb': get_connector('sql', 'test_mariadb',
        flavor='mariadb', username='test', password='test1234', database='testdb',
        port=3309, host='localhost',
    ),
    'mssql': get_connector('sql', 'test_mssql',
        flavor='timescaledb', username='sa', password='supersecureSECRETPASSWORD123!',
        database='master', port=1439, host='localhost',
    ),
    'cockroachdb': get_connector('sql', 'cockroachdb_test',
        flavor='cockroachdb', host='localhost', port=26259,
    ),
    'sqlite':  get_connector('sql', 'test_sqlite',
        database=str(pathlib.Path(__file__).parent.parent / 'data' / 'test_sqlite.db'),
        flavor='sqlite',
    ),
    'duckdb': get_connector('sql', 'test_duckdb',
        database=str(pathlib.Path(__file__).parent.parent / 'data' / 'test_duckdb.db'),
        flavor='duckdb',
    ),
    'api': get_connector('api', 'test_timescaledb_api',
        port=8989, username='test', password='test1234', host='localhost',
    ),
}
