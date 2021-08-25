from flask_script import Manager,Server
from app import create_app
from flask_migrate import Migrate, migrate


app = create_app()

manager = Manager(app)


if __name__ == '__main__':
    manager.run()