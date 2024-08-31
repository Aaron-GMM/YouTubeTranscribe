from flask import Flask

def create_app():
    app = Flask(__name__)

    # Importa e registra os blueprints dos controllers
    from app.controllers.transcriptionController import transcription_bp
    app.register_blueprint(transcription_bp)

    return app
