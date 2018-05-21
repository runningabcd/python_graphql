import graphene
import sys
import os

lib_dir = os.path.dirname(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), ""))
parent_dir = os.path.dirname(lib_dir)
sys.path.append(lib_dir)
sys.path.append(parent_dir)

from python_graphql.models.model_lagou import LagouCompanies as LagouComapnyModle, LagouJobs as LagouJobModle, db_session, \
    LagouApplications as LagouAppModel, LagouNews as LagouNewModel, LagouInvests as LagouInvestModel, \
    LagouTeams as LagouTeamModel


class InvestType(graphene.ObjectType):
    company_id = graphene.Int()
    invest_id = graphene.Int()
    round = graphene.String()
    invest_name = graphene.String()
    money = graphene.String()


class NewsType(graphene.ObjectType):
    company_id = graphene.Int()
    news_id = graphene.String()
    title = graphene.String()
    news_url = graphene.String()
    news_date = graphene.String()
    source = graphene.String()


class AppType(graphene.ObjectType):
    company_id = graphene.Int()
    application_id = graphene.Int()
    name = graphene.String()
    product_type = graphene.String()
    logo_url = graphene.String()
    description = graphene.String()
    application_url = graphene.String()


class TeamType(graphene.ObjectType):
    company_id = graphene.Int()
    person_id = graphene.Int()
    logo_url = graphene.String()
    name = graphene.String()
    title = graphene.String()
    description = graphene.String()
    weibo_url = graphene.String()


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
    teams = graphene.List(lambda: TeamType)
    apps = graphene.List(lambda: AppType)
    news = graphene.List(lambda: NewsType)
    invests = graphene.List(lambda: InvestType)

    def resolve_jobs(self, info, **args):
        return db_session.query(LagouJobModle).filter_by(company_id=self.company_id).slice(0, 20).all()

    def resolve_teams(self, info, **kwargs):
        return db_session.query(LagouTeamModel).filter_by(company_id=self.company_id).slice(0, 20).all()

    def resolve_apps(self, info, **kwargs):
        return db_session.query(LagouAppModel).filter_by(company_id=self.company_id).slice(0, 20).all()

    def resolve_news(self, info, **kwargs):
        return db_session.query(LagouNewModel).filter_by(company_id=self.company_id).slice(0, 20).all()

    def resolve_invests(self, info, **kwargs):
        return db_session.query(LagouInvestModel).filter_by(company_id=self.company_id).slice(0, 20).all()


class QueryCompany(graphene.ObjectType):
    company = graphene.Field(CompanyType, company_name=graphene.String())

    def resolve_company(self, info, **args):
        company_name = args.get('company_name')
        company_info = db_session.query(LagouComapnyModle).filter_by(company_name=company_name).first()
        return company_info


company_schema = graphene.Schema(QueryCompany, types=[CompanyType])
