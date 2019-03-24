from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, RadioField
from wtforms.validators import DataRequired

#Classe CadastroFrom
class CadastroForm(FlaskForm):
	idAlgo = StringField("idAlgo", validators=[DataRequired()])
	

		
	
		