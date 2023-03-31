import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext

# Obtener la Base de Datos
def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(
            "sqlite_db", detect_types=sqlite3.PARSE_DECLTYPES
            )
        g.db.row_factory = sqlite3.Row
    return g.db

# Cerrar la Base de Datos
def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()

# Iniciar la Base de Datos (reanudar)
def init_db():
    db = get_db()
    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf8"))

@click.command("init-db")
@with_appcontext

# Reiniciar la Base de Datos (desde cero)
def init_db_command():
    """Borrar datos existentes y crear nuevas tablas."""
    init_db()
    click.echo("Base de datos activa.")

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    