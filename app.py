from flask import Flask, render_template
from flask_restful import Api
from appflask.config import get_url_db, SECRET_KEY
from appflask.backand.database import db
from appflask.models.tasks import TasksSchem
from appflask.routers.taskrout import TaskApi

app = Flask(__name__)
api = Api(app)
api.add_resource(TaskApi, '/tasks', '/tasks/<int:task_id>')


def create_app():
    app.config['SQLALCHEMY_DATABASE_URI'] = get_url_db()
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = SECRET_KEY
    db.init_app(app)
    api.init_app(app)

    @app.route('/')
    def home():
        tasks_schem = TasksSchem.query.all()
        return render_template('tasksmanager.html', tasks=tasks_schem)

    return app


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()

    app.run(debug=True)
