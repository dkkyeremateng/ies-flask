from app import app, db
from flask.ext.script import Manager, Server
from flask.ext.migrate import MigrateCommand


# manager config
manager = Manager(app)

manager.add_command("run", Server(use_debugger=True, use_reloader=True, host="localhost", port="5000"))
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    db.create_all()
    manager.run()
