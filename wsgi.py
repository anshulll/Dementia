"""App entry point."""

#from application.__init__ import create_app,db
from application import create_app
import os 

#from flask_script import Manager
#from flask_migrate import Migrate, MigrateCommand
#from flask_script import Manager
#from flask_migrate import Migrate, MigrateCommand
basedir=os.getcwd()

app = create_app()
#migrate = Migrate(app, db)
#manager = Manager(app)

#manager.add_command('db', MigrateCommand)


if __name__ == "__main__":
    app.run(Debug=True)
