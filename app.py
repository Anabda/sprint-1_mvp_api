from flask_openapi3 import OpenAPI, Info, Tag
from sqlalchemy.exc import IntegrityError
from flask_cors import CORS
from flask import redirect

from model import Session, Aparelho
from schemas import *

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)


# tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
aparelho_tag = Tag(name="Aparelho", description="Cria, lista e remove aparelhos da base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/aparelho', tags=[aparelho_tag],
          responses={"200": AparelhoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_aparelho(form: AparelhoSchema):
    """Adiciona um novo Aparelho à base de dados
    """
    aparelho = Aparelho(
        codigo=form.codigo, 
        nome=form.nome,
        potencia=form.potencia,
        voltagem=form.voltagem,
        comodo=form.comodo,
        amperagem=form.amperagem,
        diametro_fio=form.diametro_fio)
    
    try:
        session = Session()
        session.add(aparelho)
        session.commit()
        print("Inseri!")
        return apresenta_aparelho(aparelho), 200

    except IntegrityError as e:
        error_msg = "Não foi possível cadastrar o aparelho, pois já existe um aparelho com esse código"
        print("erro: aparelho já cadastrado")
        return {"mesage": error_msg}, 409

    except Exception as e:
        error_msg = "Erro inesperado, o aparelho inserido não foi cadastrado"
        print("erro!")
        return {"mesage": error_msg}, 400


@app.get('/aparelhos', tags=[aparelho_tag],
         responses={"200": ListagemAparelhosSchema, "404": ErrorSchema})
def get_aparelhos():
    """Retorna uma listagem de produtos cadastrados na base.
    """
    
    session = Session()
    aparelhos = session.query(Aparelho).all()

    if not aparelhos:
        return {"aparelhos": []}, 200
    print(aparelhos)
    return apresenta_aparelhos(aparelhos), 200

@app.delete('/aparelho', tags=[aparelho_tag],
            responses={"200": AparelhoDelSchema, "404": ErrorSchema})
def del_produto(query: AparelhoBuscaSchema):
    """Deleta um Aparelho a partir do nome informado

    Retorna uma mensagem de confirmação da remoção.
    """
    codigo = query.codigo
    session = Session()
    count = session.query(Aparelho).filter(Aparelho.codigo == codigo).delete()
    session.commit()

    if count:
        return {"mesage": "Aparelho removido", "aparelho": codigo}
    error_msg = "Aparelho não encontrado"
    return {"mesage": error_msg}, 404
    