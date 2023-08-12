from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Experiments_Base = declarative_base()


class Prompts(Experiments_Base):
    __tablename__ = 'prompts'

    id = Column(Integer, primary_key=True)
    short_name = Column(String)
    prompt_text = Column(String)


class Models(Experiments_Base):
    __tablename__ = 'models'

    id = Column(Integer, primary_key=True)
    model_name = Column(String)


class Experiments(Experiments_Base):
    __tablename__ = 'experiments'

    id = Column(Integer, primary_key=True)
    prompt_id = Column(Integer, ForeignKey('prompts.id'))
    model_id = Column(Integer, ForeignKey('models.id'))
    message_set = Column(String)
    results = Column(JSON)
