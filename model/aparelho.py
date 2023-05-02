from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base

class Aparelho(Base):
    __tablename__ = 'aparelho'

    codigo = Column("Código", Integer, primary_key=True)
    nome = Column(String(140))
    potencia = Column(Float)
    voltagem = Column(Integer)
    comodo = Column(String(140))
    amperagem = Column(Float)
    diametro_fio = Column(Float)

    def __init__(self, codigo: int, nome:str, potencia:float, voltagem:int, comodo:str, 
                 amperagem:float, diametro_fio:float, 
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Aparelho eletrônico

        Arguments:
            codigo: numero do patrimonio do aparelho
            nome: nome do aparelho
            potencia: potência do aparelho (W)
            voltagem: voltagem do aparelho (V)
            comodo: cômodo em que o aparelho é mais utilizado
            amperagem: amperagem do aparelho (A)
            diametro_fio: diâmetro mínimo do fio que deve ser utilizado (mm)
            data_insercao: data de quando o aparelho foi inserido na base
        """
        self.codigo = codigo
        self.nome = nome
        self.potencia = potencia
        self.voltagem = voltagem
        self.comodo=comodo
        self.amperagem = amperagem
        self.diametro_fio = diametro_fio

        if data_insercao:
            self.data_insercao = data_insercao
        else:
            self.data_insercao = datetime.today()