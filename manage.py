from flask_script import Server, Manager
from app import start_app
from config.config import Config

manager = Manager(start_app)
manager.add_command("runserver", Server())

if __name__ == "__main__":
    Config.load_env()
    manager.run()
