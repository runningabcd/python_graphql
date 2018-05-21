from flask import Flask
from flask_graphql import GraphQLView
import sys
import os

lib_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(lib_dir)
sys.path.append(lib_dir)
sys.path.append(parent_dir)

from python_graphql.models.model_lagou import db_session
from python_graphql.schemas.schema_lagou import company_schema

app = Flask(__name__)
app.debug = True

app.add_url_rule('/lagou_company', view_func=GraphQLView.as_view('lagou', schema=company_schema,
                                                                 graphiql=True))


@app.teardown_appcontext
def shoutdown_session(execpet=None):
    db_session.remove()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=31211)