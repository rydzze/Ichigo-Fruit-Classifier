import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

def init_app():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    
    app = Flask(__name__,
                static_folder=os.path.join(base_dir, 'static'),
                template_folder=os.path.join(base_dir, 'templates'))

    app.config['UPLOAD_FOLDER'] = os.path.join(base_dir, 'uploads')
    app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'defaultsecretkey')

    with app.app_context():
        from app import routes
        app.register_blueprint(routes.bp)

    return app