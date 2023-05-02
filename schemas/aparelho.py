from pydantic import BaseModel
from typing import Optional, List
from model.aparelho import Aparelho
from datetime import datetime


class AparelhoSchema(BaseModel):
    """ Define como um novo aparelho a ser inserido deve ser representado
    """
    
    codigo: int
    nome: str
    potencia: float
    voltagem: int
    comodo: Optional[str]
    amperagem: Optional[float]
    diametro_fio: Optional[float]
        
class AparelhoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do aparelho.
    """
    codigo: int = 1

class ListagemAparelhosSchema(BaseModel):
    """ Define como uma listagem de aparelhos será retornada.
    """
    aparelhos:List[AparelhoSchema]

def apresenta_aparelhos(aparelhos: List[Aparelho]):
    """ Retorna uma representação do aparelho.
    """
    lista_aparelhos = []
    for aparelho in aparelhos:
        lista_aparelhos.append({
            "codigo": aparelho.codigo, 
            "nome": aparelho.nome,
            "potencia": aparelho.potencia,
            "voltagem": aparelho.voltagem,
            "comodo": aparelho.comodo,
            "amperagem": aparelho.amperagem,
            "diametro_fio": aparelho.diametro_fio
        })

    return {"aparelhos": lista_aparelhos}

def apresenta_aparelho(aparelho: Aparelho):
    """ Retorna uma representação do aparelho.
    """
    return {
        "codigo": aparelho.codigo, 
        "nome": aparelho.nome,
        "potencia": aparelho.potencia,
        "voltagem": aparelho.voltagem,
        "comodo": aparelho.comodo,
        "amperagem": aparelho.amperagem,
        "diametro_fio": aparelho.diametro_fio
    }



class AparelhoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    codigo: int

class AparelhoViewSchema(BaseModel):
    """ Define como um aparelho será retornado.
    """
    codigo: int = 1
    nome: str = "Play Station 5"
    potencia: float = 350.00
    voltagem: int = 110
    comodo: Optional[str] = "Salão de Jogos"
    amperagem: Optional[float] = 5
    diametro_fio: Optional[float] = 10
    data_insercao: Optional[datetime] = datetime.today()