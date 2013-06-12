Example of a bug when using spyne and alembic together with Postgresql + XML columns for spyne arrays.

Steps to reproduce:

1. Install requirements
$ pip install -r requirements.txt

2. Setup postgresql test db
$ createdb alembic_spyne_test

3. Run inital migration
$ alembic upgrade head

4. Run the alembic autogeneration to add the new_column column
$ alembic revision --autogenerate -m "added new_column"

Observe something like:

INFO  [alembic.migration] Context impl PostgresqlImpl.
INFO  [alembic.migration] Will assume transactional DDL.
Traceback (most recent call last):
  File "/usr/local/bin/alembic", line 9, in <module>
    load_entry_point('alembic==0.5.0', 'console_scripts', 'alembic')()
  File "/usr/local/lib/python2.7/dist-packages/alembic/config.py", line 265, in main
    CommandLine(prog=prog).main(argv=argv)
  File "/usr/local/lib/python2.7/dist-packages/alembic/config.py", line 260, in main
    self.run_cmd(cfg, options)
  File "/usr/local/lib/python2.7/dist-packages/alembic/config.py", line 247, in run_cmd
    **dict((k, getattr(options, k)) for k in kwarg)
  File "/usr/local/lib/python2.7/dist-packages/alembic/command.py", line 96, in revision
    script.run_env()
  File "/usr/local/lib/python2.7/dist-packages/alembic/script.py", line 193, in run_env
    util.load_python_file(self.dir, 'env.py')
  File "/usr/local/lib/python2.7/dist-packages/alembic/util.py", line 177, in load_python_file
    module = imp.load_source(module_id, path, open(path, 'rb'))
  File "alembic/env.py", line 76, in <module>
    run_migrations_online()
  File "alembic/env.py", line 69, in run_migrations_online
    context.run_migrations()
  File "<string>", line 7, in run_migrations
  File "/usr/local/lib/python2.7/dist-packages/alembic/environment.py", line 536, in run_migrations
    self.get_context().run_migrations(**kw)
  File "/usr/local/lib/python2.7/dist-packages/alembic/migration.py", line 205, in run_migrations
    self):
  File "/usr/local/lib/python2.7/dist-packages/alembic/command.py", line 82, in retrieve_migrations
    autogen._produce_migration_diffs(context, template_args, imports)
  File "/usr/local/lib/python2.7/dist-packages/alembic/autogenerate.py", line 127, in _produce_migration_diffs
    include_schemas)
  File "/usr/local/lib/python2.7/dist-packages/alembic/autogenerate.py", line 188, in _produce_net_changes
    inspector, metadata, diffs, autogen_context)
  File "/usr/local/lib/python2.7/dist-packages/alembic/autogenerate.py", line 217, in _compare_tables
    for s, tname in existing_tables
  File "/usr/local/lib/python2.7/dist-packages/alembic/autogenerate.py", line 217, in <genexpr>
    for s, tname in existing_tables
  File "/usr/local/lib/python2.7/dist-packages/sqlalchemy/engine/reflection.py", line 254, in get_columns
    **kw)
  File "<string>", line 1, in <lambda>
  File "/usr/local/lib/python2.7/dist-packages/sqlalchemy/engine/reflection.py", line 49, in cache
    ret = fn(self, con, *args, **kw)
  File "/usr/local/lib/python2.7/dist-packages/sqlalchemy/dialects/postgresql/base.py", line 1672, in get_columns
    name, format_type, default, notnull, domains, enums, schema)
  File "/usr/local/lib/python2.7/dist-packages/sqlalchemy/dialects/postgresql/base.py", line 1761, in _get_column_info
    coltype = coltype(*args, **kwargs)
TypeError: __init__() takes at least 2 arguments (1 given)
