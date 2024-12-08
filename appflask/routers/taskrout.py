from flask_restful import Resource, reqparse
from appflask.models.tasks import TasksSchem
from appflask.backand.database import db

task_create_parser = reqparse.RequestParser()
task_create_parser.add_argument('title', type=str, required=True,
                                help='Title is required.', location='json')
task_create_parser.add_argument('description', type=str, required=True,
                                help='Description is required.', location='json')
task_create_parser.add_argument('status', type=str, choices=('completed', 'incomplete'),
                                required=True, help='Status is required.', location='json')
task_create_parser.add_argument('priority', type=str, choices=('low', 'medium', 'high'),
                                required=True, help='Priority is required.', location='json')
task_create_parser.add_argument('deadline', type=str, required=True,
                                help='Deadline is required in YYYY-MM-DD format.',
                                location='json')

task_update_parser = reqparse.RequestParser()
task_update_parser.add_argument('title', type=str, location='json')
task_update_parser.add_argument('description', type=str, location='json')
task_update_parser.add_argument('status', type=str, choices=('completed', 'incomplete'), location='json')
task_update_parser.add_argument('priority', type=str, choices=('low', 'medium', 'high'), location='json')
task_update_parser.add_argument('deadline', type=str,
                                help='Deadline should be in YYYY-MM-DD format.', location='json')


class TaskApi(Resource):
    def get(self, task_id=None):
        if task_id:
            task = TasksSchem.query.get_or_404(task_id)
            return {'id': task.id, 'title': task.title, 'description': task.description, 'status': task.status,
                    'priority': task.priority, 'deadline': task.deadline.strftime('%Y-%m-%d')}
        else:
            tasks = TasksSchem.query.all()
            return [{'id': task.id, 'title': task.title, 'description': task.description, 'status': task.status,
                     'priority': task.priority, 'deadline': task.deadline.strftime('%Y-%m-%d')} for task in tasks]

    def post(self):
        args = task_create_parser.parse_args()
        new_task = TasksSchem(title=args['title'], description=args['description'], status=args['status'],
                              priority=args['priority'], deadline=args['deadline'])
        db.session.add(new_task)
        db.session.commit()
        created_task = {'id': new_task.id, 'title': new_task.title, 'description': new_task.description,
                        'status': new_task.status, 'priority': new_task.priority,
                        'deadline': new_task.deadline.strftime('%Y-%m-%d')}
        return [created_task, "Задача успешно создана"]

    def put(self, task_id):
        task = TasksSchem.query.get_or_404(task_id)
        args = task_update_parser.parse_args()
        if 'title' in args:
            task.title = args['title']
        if 'description' in args:
            task.description = args['description']
        if 'status' in args:
            task.status = args['status']
        if 'priority' in args:
            task.priority = args['priority']
        if 'deadline' in args:
            task.deadline = args['deadline']
        db.session.commit()
        updated_task = {'id': task.id, 'title': task.title, 'description': task.description, 'status': task.status,
                        'priority': task.priority, 'deadline': task.deadline.strftime('%Y-%m-%d')}
        return [updated_task, "Задача успешно обновлена"]

    def delete(self, task_id):
        task = TasksSchem.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
        return 'Задача удалена'
