from flask import Flask
from flask_graphql import GraphQLView
import sys
import os

lib_dir = os.path.dirname(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), ""))
parent_dir = os.path.dirname(lib_dir)
sys.path.append(lib_dir)
sys.path.append(parent_dir)

from python_graphql.models.model import db_session
from python_graphql.schemas.schema import company_schema, job_schema

app = Flask(__name__)
app.debug = True

app.add_url_rule('/graphql/company', view_func=GraphQLView.as_view('company', schema=company_schema,
                                                                   graphiql=True, context={'session': db_session}))
app.add_url_rule('/graphql/job', view_func=GraphQLView.as_view('job', schema=job_schema,
                                                               graphiql=True, context={'session': db_session}))


@app.teardown_appcontext
def shoutdown_session(execpet=None):
    db_session.remove()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
