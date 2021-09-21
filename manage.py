from app.models import Comment, Pitch, User
from flask_script import Manager,Server
from app import create_app, db
from flask_migrate import Migrate, MigrateCommand


#create app instance
app=create_app('production')

manager=Manager(app)
#the add_command method to create a new command 'server'
manager.add_command('server',Server)

migrate =Migrate(app,db)
manager.add_command('db',MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User=User,Pitch=Pitch,Comment=Comment )

if __name__=='__main__':
    manager.run()


