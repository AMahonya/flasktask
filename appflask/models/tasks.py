from appflask.backand.database import db


class TasksSchem(db.Model):
    __tablename__ = 'tasks_schem'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(98), nullable=False)
    description = db.Column(db.String(355), nullable=False)
    status = db.Column(db.Enum('completed', 'incomplete', name='task_status'), nullable=False)
    priority = db.Column(db.Enum('low', 'medium', 'high', name='task_priority'), nullable=False)
    deadline = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'<Task {self.title}>'


