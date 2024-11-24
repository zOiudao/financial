from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import create_engine, Column, Integer, Text, String, ForeignKey, DateTime, Float
from datetime import datetime
import pytz
tmz = pytz.timezone('America/Sao_Paulo')

engine = create_engine('sqlite:///database/finance_data.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id=Column(Integer, primary_key=True)
    nome=Column(String(60), nullable=False)
    cpf=Column(String(60), nullable=False)
    email=Column(String(60), nullable=False)
    senha=Column(String(60), nullable=False)
    data=Column(DateTime, default=lambda: datetime.now(tmz))
    despesa = relationship('Despesa', back_populates="usuario")
    receita = relationship('Receita', back_populates="usuario")
    
    def __init__(self, nome, cpf, email, senha):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.senha = senha
    
    
class Instituicao(Base):
    __tablename__ = 'instituicoes'
    id=Column(Integer, primary_key=True)
    nome=Column(String(60), nullable=False)
    tipo=Column(String(60), nullable=False)
    descricao=Column(Text(500), nullable=True)
    data=Column(DateTime, default=lambda: datetime.now(tmz))
    despesa = relationship('Despesa', back_populates="instituicao")
    receita = relationship('Receita', back_populates="instituicao")
    
    def __init__(self, nome, tipo, descricao):
        self.nome = nome
        self.tipo = tipo
        self.descricao = descricao
        
        
class Despesa(Base):
    __tablename__ = 'despesas'
    id=Column(Integer, primary_key=True)
    usuario_id=Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    instituicao_id=Column(Integer, ForeignKey('instituicoes.id'), nullable=False)
    valor=Column(Float, nullable=False)
    parcelas=Column(Integer, nullable=False)
    data=Column(DateTime, default=lambda: datetime.now(tmz))
    usuario = relationship('Usuario', back_populates="despesa")
    instituicao = relationship('Instituicao', back_populates="despesa")
    
    def __init__(self, user_id, inst_id, valor, parcelas):
        self.usuario_id = user_id
        self.instituicao_id = inst_id
        self.valor = valor   
        self.parcelas = parcelas     
    
    
class Receita(Base):
    __tablename__ = 'receitas'
    id=Column(Integer, primary_key=True)
    usuario_id=Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    instituicao_id=Column(Integer, ForeignKey('instituicoes.id'), nullable=False)
    valor=Column(Float, nullable=False)
    data=Column(DateTime, default=lambda: datetime.now(tmz))
    instituicao = relationship('Instituicao', back_populates="receita")
    usuario = relationship('Usuario', back_populates="receita")
    
    def __init__(self, user_id, inst_id, valor):
        self.usuario_id = user_id
        self.instituicao_id = inst_id
        self.valor = valor
        

Base.metadata.create_all(engine)