from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship, backref)
import os

STAG_URI = os.getenv('STAGURI')
engine = create_engine(STAG_URI,
                       convert_unicode=True)
db_session = scoped_session(sessionmaker(bind=engine))
meta = MetaData(schema='data')
Base = declarative_base(metadata=meta)


class LagouCompanies(Base):
    __tablename__ = "lagou_companies"
    company_name = Column(String, primary_key=True, autoincrement=False)
    # 公司id
    company_id = Column(Integer)
    # 公司简称
    name = Column(String)
    # logo
    logo_url = Column(String)
    # 简介（一句话）
    intro = Column(String)
    # 官网
    website = Column(String)
    # 行业
    sector = Column(String)
    # 融资伦次
    round = Column(String)
    # 所在城市
    location = Column(String)
    # 详细地址
    address = Column(String)
    # 公司详细介绍
    description = Column(Text)
    # 来源url
    source_url = Column(String)
    # 认证状态
    auth_type = Column(String)
    # 团队人数
    team_size = Column(String)


class LagouJobs(Base):
    __tablename__ = "lagou_jobs"
    # 公司id
    company_id = Column(Integer)
    # 职位id
    position_id = Column(Integer, primary_key=True, autoincrement=False)
    # 岗位名称
    name = Column(String)
    # 岗位类型
    job_type = Column(String)
    # 工作年限
    work_year = Column(String)
    # 教育
    education = Column(String)
    # 职位类型
    position_type = Column(String)
    # 地点
    location = Column(String)
    # 薪资
    salary = Column(String)
    # 发布时间
    publish_date = Column(String)


class LagouApplications(Base):
    __tablename__ = "lagou_applications"
    # 公司id
    company_id = Column(Integer)
    # 产品id
    application_id = Column(Integer, primary_key=True, autoincrement=False)
    # 产品名称
    name = Column(String)
    # 产品类型
    product_type = Column(String)
    # 产品logo
    logo_url = Column(String)
    # 产品介绍
    description = Column(String)
    # 产品链接
    application_url = Column(String)


class LagouTeams(Base):
    __tablename__ = "lagou_team_members"
    company_id = Column(Integer)
    # 成员id
    person_id = Column(Integer, primary_key=True, autoincrement=False)
    # 团队url
    logo_url = Column(String)
    # 高管姓名
    name = Column(String)
    # 高管职位
    title = Column(String)
    # 高管介绍
    description = Column(Text)
    # 高管微博
    weibo_url = Column(String)


class LagouNews(Base):
    __tablename__ = "lagou_news"
    # 公司id
    company_id = Column(Integer)
    # 新闻id
    news_id = Column(String, primary_key=True, autoincrement=False)
    # 标题
    title = Column(String)
    # 地址
    news_url = Column(String)
    # 时间
    news_date = Column(String)
    # 来源
    source = Column(String)


class LagouInvests(Base):
    __tablename__ = "lagou_invests"
    # 公司id
    company_id = Column(Integer)
    # 投资事件id
    invest_id = Column(Integer, primary_key=True, autoincrement=False)
    # 轮次
    round = Column(String)
    # 投资方
    invest_name = Column(String)
    # 金额 0表示未知
    money = Column(String)
    # financing_date = Column(String)