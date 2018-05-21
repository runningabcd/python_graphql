import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
import sys
import os

lib_dir = os.path.dirname(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), ""))
parent_dir = os.path.dirname(lib_dir)
sys.path.append(lib_dir)
sys.path.append(parent_dir)

from python_graphql.models.model import LagouCompanies as LagouComapnyModle, LagouJobs as LagouJobModle, db_session


# class LagouCompany(SQLAlchemyObjectType):
#     class Meta:
#         model = LagouComapnyModle
#         interfaces = (relay.Node,)
#
#
# class LagouJob(SQLAlchemyObjectType):
#     class Meta:
#         model = LagouJobModle
#         interfaces = (relay.Node,)
class JobType(graphene.ObjectType):
    company_id = graphene.Int()
    position_id = graphene.Int()
    name = graphene.String()
    job_type = graphene.String()
    work_year = graphene.String()
    education = graphene.String()
    position_type = graphene.String()
    location = graphene.String()
    salary = graphene.String()
    publish_date = graphene.String()

class CompanyType(graphene.ObjectType):
    company_name = graphene.String()
    company_id = graphene.Int()
    name = graphene.String()
    logo_url = graphene.String()
    intro = graphene.String()
    website = graphene.String()
    sector = graphene.String()
    round = graphene.String()
    location = graphene.String()
    address = graphene.String()
    description = graphene.String()
    source_url = graphene.String()
    auth_type = graphene.String()
    team_size = graphene.String()
    jobs = graphene.List(lambda: JobType)

    def resolve_jobs(self, info, **args):
        return db_session.query(LagouJobModle).filter_by(company_id=self.company_id).all()


class QueryCompany(graphene.ObjectType):
    company = graphene.Field(CompanyType, company_name=graphene.String())

    def resolve_company(self, info, **args):
        company_name = args.get('company_name')
        company_info = db_session.query(LagouComapnyModle).filter_by(company_name=company_name).first()
        return company_info


class QueryJob(graphene.ObjectType):
    jobs = graphene.List(lambda: JobType, company_id=graphene.Int())
    companys = graphene.Field(CompanyType, company_id=graphene.Int())

    def resolve_jobs(self, info, **args):
        return db_session.query(LagouJobModle).filter_by(company_id=args.get('company_id')).all()

    def resolve_companys(self, info, **args):
        return db_session.query(LagouComapnyModle).filter_by(company_id=args.get('company_id')).first()


company_schema = graphene.Schema(QueryCompany, types=[CompanyType])
job_schema = graphene.Schema(QueryJob, types=[JobType])