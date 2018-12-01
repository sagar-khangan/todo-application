from sqlalchemy import Column, Integer, String,Boolean,ARRAY
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TaskList(Base):
    __tablename__ = 'tasklist'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    tasks = Column(String)

    def __repr__(self):
        return "TasksList(id='%s', name='%s')" % (
            self.id, self.name)


class Tasks(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String)
    task_finished = Column(Boolean,default=False)

    def __repr__(self):
        return "Tasks(id='%s', name='%s', task_finished='%s')" % (
                                         self.id, self.name, self.task_finished)

