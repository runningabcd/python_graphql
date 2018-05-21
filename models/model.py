from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship, backref)

engine = create_engine('postgresql+psycopg2://xingqi_stagedata:STxinguXALtfM9gvgbQAGE@192.168.60.5:31907/spider_rawbase_prod',
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
