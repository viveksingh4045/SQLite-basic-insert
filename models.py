from sqlalchemy import Column, Date, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MetaData(Base):
    '''
    Data model to hold Meta data information
    '''
    __tablename__ = 'MetaData'
    
    id = Column(Integer, primary_key=True)
    connection = Column(String)
    platform = Column(String)
    country = Column(String)
    app = Column(String)
    date = Column(Date)
    ad_cpm = Column(Float)
    install_rate = Column(Float)
    iap_revenue = Column(Float)
    ad_revenue = Column(Float)
    spent = Column(Float)
    fill_rate = Column(Float)
    ctr = Column(Float)
    unfilled_impressions = Column(Float)
    downloads = Column(Float)
    updates = Column(Float)
    returns = Column(Float)
    hits = Column(Float)
    user_sessions = Column(Float)
    new_users = Column(Float)
    dau = Column(Float)
    mau = Column(Float)
    requests = Column(Float)
    paying_users = Column(Float)
    acq_requests = Column(Float)
    acq_impressions = Column(Float)
    acq_clicks = Column(Float)
    acq_completions = Column(Float)
    acq_installs = Column(Float)
    impressions = Column(Float)
    clicks = Column(Float)
    completions = Column(Float)
    conversions = Column(Float)
    measurable_impressions = Column(Float)
    viewable_impressions = Column(Float)
    page_views = Column(Float)
    iap_revenue_gross = Column(Float)

    
class ImpressionMetrics(Base):
    __tablename__ = 'ImpressionMetrics'
    id = Column(Integer, primary_key=True)
    connection = Column(String)
    platform = Column(String)
    country = Column(String)
    app = Column(String)
    date = Column(Date)
    ad_revenue = Column(Float)
    impressions = Column(Float)

