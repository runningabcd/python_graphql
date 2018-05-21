# from graphene import ObjectType, String, Int, Schema, AbstractType, Argument, List
#
# from python_graphql.models.model import db_session, LagouCompanies, LagouJobs
#
# class LagouCompany(ObjectType):
#     print("/"*66)
#     companyname = String()
#     companyid = Int()
#
#     def resolve_companyid(root, args, info):
#         print("?"*66)
#         # if not company_id:
#         company_name = args.get('companyname')
#         data = db_session.query(LagouCompanies.company_id).filter(LagouCompanies.company_name == company_name).first()
#         return data
#         # return db_session.query(LagouCompanies).filter(LagouCompanies.company_id == company_id).filter(
#         #     LagouCompanies.company_name == company_name).first()
#
# # class LagouJob(ObjectType):
# #     job = List(company_id=Int(required=True))
# #
# #     def resolve_job(self, info):
# #         company_id = info.context.get('company_id')
# #         if not company_id:
# #             return
# #         return db_session.query(LagouJobs).filter(LagouJobs.company_id == company_id).first()
#
# # lagou_job_schema = Schema(LagouJob)
# lagou_company_schema = Schema(LagouCompany)
# print(lagou_company_schema.execute('''{lagoucompany(companyname: "上海倬倬文化艺术交流有限公司"){companyid}}''').data)
#
# # class Query(ObjectType):
# #     hello = String(name=String(default_value="stranger"))
# #
# #     def resolve_hello(self, info, name):
# #         return 'Hello ' + name
# #
# # schema = Schema(query=Query)
# # result = schema.execute('{ hello(name:hahahahahah) }')
# # print(result.data['hello'])