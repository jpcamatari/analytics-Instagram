from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USUARIO = "root"
SENHA = "pedromarins"
HOST = "35.247.197.93"
BANCO = "UrnaEletronica"
PORT = "3306"

CON = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

engine = create_engine(CON, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Partido:
    def __init__(self, sigla):
        self.sigla = sigla


class Prefeito:
    def __init__(self, nome, partido, numero, foto):
        self.nome = nome
        self.partido = partido
        self.numero = numero
        self.foto = foto

class Vereador:
    def __init__(self, nome, partido, numero, foto):
        self.nome = nome
        self.partido = partido
        self.numero = numero
        self.foto = foto


