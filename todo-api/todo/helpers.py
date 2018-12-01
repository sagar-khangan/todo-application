from todo.models import Base, Tasks,TaskList
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json
engine = create_engine('sqlite:///db.sqlite', echo=True)
Session = sessionmaker(bind=engine)


def init_schema():
    Base.metadata.create_all(engine)


def create(list_id,data):

    try:
        session = Session()
        task = Tasks(name=data['name'])
        session.add(task)
        session.commit()
        task_id = task.id
        tasklist = session.query(TaskList).filter_by(id=list_id).one()
        if tasklist.tasks is None:
            _data = list()
        else:
            _data = json.loads(tasklist.tasks)
        _data.append(task_id)
        tasklist.tasks = json.dumps(_data)
        session.merge(tasklist)
        session.commit()
        session.close()

        return "Task inserted", True
    except Exception as e:
        return "Error in inserting task", False


def retrieve(list_id):

    try:
        session = Session()
        tasklist = session.query(TaskList).filter_by(id=list_id).one()
        if tasklist.tasks is None:
            return "List does not exists", False
        tasks = json.loads(tasklist.tasks)
        result = list()
        for _task in tasks:
            _result = session.query(Tasks).filter_by(id=_task).one()
            result.append(_result)
        session.close()
        resp = [i.__dict__ for i in result]
        [i.pop('_sa_instance_state') for i in resp]
        return resp, True
    except Exception as e:
        return "Error in Fetching task", False


def update(list_id,task_id,data):
    session = Session()
    try:
        task = session.query(Tasks).filter_by(id=task_id).one()
        if data.get('name'):
            task.name = data.get('name')
        if data.get('task_finished'):
            task.task_finished = data.get('task_finished')
        session.merge(task)
        session.commit()
        session.close()
        return "Task updated", True
    except Exception as e:
        return "Error in updating task", False


def delete(list_id,task_id):
    try:
        session = Session()
        task = session.query(Tasks).filter_by(id=task_id)
        task_id = task.one().id
        session.delete(task.one())
        session.commit()
        tasklist = session.query(TaskList).filter_by(id=list_id).one()
        _tasks = json.loads(tasklist.tasks)
        _tasks.remove(task_id)
        tasklist.tasks = json.dumps(_tasks)
        session.merge(tasklist)
        session.commit()
        session.close()
        return "Task deleted", True
    except Exception as e:
        return "Error in deleting task", False

