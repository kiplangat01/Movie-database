# Creating app instance
from multiprocessing import Manager
from multiprocessing.managers import Server
from app import create_app,db
# .....
from app.models import User
# ...
from app.main import create_app


app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)

# ...
manager.add_command('server',Server)
@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User )


if __name__ == '__main__':
    manager.run()