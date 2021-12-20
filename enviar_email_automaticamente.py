import win32com.client as win32
import datetime

gmail = win32.Dispatch('outlook.application')

email = gmail.CreateItem(0)

email.To = input('o email destinatário : ')
email.Subject = input('assunto do email : ')

#definindo a hora para definir o cumprimento
data = datetime.datetime.now().ctime().split()
horas = data[3].split(':')
hora = int(horas[0])

cumprimento = 'Olá'
if 4 >= hora > 0:
    cumprimento = 'Boa noite!'
elif 12 >= hora > 4:
    cumprimento = 'Bom dia!'
elif 18 >= hora > 12:
    cumprimento = 'Boa tarde!'
elif 23 >= hora > 18:
    cumprimento = 'Boa noite!'

email.HTMLBody = f'''<h3>{cumprimento} Em anexo, meu currículo.</h3>

<h5>Grato, 
<p>Kennedy.</p></h5>'''

anexo = 'C://Users/Usuario/Desktop/cv_KENNEDYMBG.pdf'
email.Attachments.Add(anexo)

email.Send()
