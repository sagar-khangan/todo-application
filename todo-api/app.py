from flask import Flask
from todo.views import todo
from todo.helpers import init_schema

app = Flask(__name__)
app.register_blueprint(todo,url_prefix='/api/todo')


if __name__ == '__main__':
    init_schema()
    app.run(debug=True)

