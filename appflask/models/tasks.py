from appflask.backand.database import db


class TasksSchem(db.Model):
    """
    Модель для представления задач в базе данных.
    Эта модель определяет структуру таблицы 'tasks_schem', которая используется для хранения информации
    о задачах, включая их заголовок, описание, статус, приоритет и крайний срок выполнения.
    """
    __tablename__ = 'tasks_schem'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(98), nullable=False)
    description = db.Column(db.String(355), nullable=False)
    status = db.Column(db.Enum('completed', 'incomplete', name='task_status'), nullable=False)
    priority = db.Column(db.Enum('low', 'medium', 'high', name='task_priority'), nullable=False)
    deadline = db.Column(db.Date, nullable=False)

    def __repr__(self):
        """
        Возвращает строковое представление объекта Task.
        Этот метод используется для представления объекта Task в виде строки,
        что полезно для отладки и логгирования.
        """
        return f'<Task {self.title}>'
