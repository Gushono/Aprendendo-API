
from flask import render_template
from app import app
import requests
import json



from app.models.forms import CadastroForm


#from app.models.tables import User

#CONFIGURAÇÃO DA ROTA DE INDEX
@app.route("/index/")
@app.route("/")
def index():
	#RENDERIZAÇÃO DO TEMPLATE DA TELA PRINCIPAL
	return render_template('index.html')


#CONFIGURAÇÃO DA ROTA DE CADASTRO
@app.route("/cadastro/")
@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
	#Recebendo o valor dos dados vindos da classe CadastroForm
	form = CadastroForm()
	#Se o submit for validado, então:
	if form.validate_on_submit():
		print("A cidade é: " + form.idAlgo.data)
		
		#Pega o valor do nome da cidade no FORM
		NomeCidade = form.idAlgo.data
		
		#Token de segurança da API
		token = '27dc2dde8778e2f6963013dfa87b0e5d'
		#recebe os dados da cidade digitado pelo link da api
		recebeDadosCidade= requests.get('http://apiadvisor.climatempo.com.br/api/v1/locale/city?name='+NomeCidade+'&state=SP&token='+token)
		#transforma os jados da cidade em um dicionário
		recebeDadosTempoCidade = json.loads(recebeDadosCidade.text)
		#Atribui o ID da cidade pegando dos valores contidos no dicionario
		idCidade = recebeDadosTempoCidade[0]['id']
		
		#MELHORIAS FUTURAS
		#POPULAR LISTA DO INPUT COM CIDADES
		
		#recebe os valores do tempo da api passando como parametros o ID da cidade recuperado anteriormente
		r = requests.get('http://apiadvisor.climatempo.com.br/api/v1/weather/locale/'+str(idCidade)+'/current?token='+token)
		#transforma os dados em dicionário novamente
		recebeDadosTempo = json.loads(r.text)
		print (recebeDadosTempo)
		
		
		
		
	

		#Retorna para a view confirmacao o form + os dados em formato de dicionario do tempo
		return render_template('confirmacao.html', form=form, dadostempo=recebeDadosTempo)
		#return render_template('projeto.html', form=form)
		

	else:
		print(form.errors)
	#RENDERIZAÇÃO DO TEMPLATE PROJETO.HTML
	return render_template('projeto.html', form = form)
		


