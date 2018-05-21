# from flask import Flask
# from flask import request
# import ujson
#
# from python_graphql.schemas.schema_python import lagou_company_schema, lagou_job_schema
#
# app = Flask(__name__)
# app.debug = True
#
#
# @app.route('/graphql/company', methods=['POST'])
# def resolve_company():
#     data = ujson.loads(request.data)
#     return lagou_company_schema.execute(data['query']).data
#
#
# @app.route('/graphql/job', methods=['POST'])
# def resolve_job():
#     data = ujson.loads(request.data)
#     return ''
#
# if __name__ == '__main__':
#     app.run()
