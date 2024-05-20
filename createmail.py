import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Informations de connexion au serveur SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_user = 'You@gmail.com'  # Remplacez par votre adresse e-mail
smtp_password = 'gwrq eojh kimu azeo'  # Remplacez par votre mot de passe (ou mot de passe d'application)

# Informations de l'e-mail
to_email = 'Their@gmail.com'  # Remplacez par l'adresse e-mail du destinataire
subject = 'Salut'
body = 'Bonjour'

# Création du message
msg = MIMEMultipart()
msg['From'] = smtp_user
msg['To'] = to_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# Envoi de l'e-mail
try:
    # Connexion au serveur SMTP
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Démarrer TLS pour sécuriser la connexion
        server.login(smtp_user, smtp_password)  # Connexion au serveur SMTP
        server.sendmail(smtp_user, to_email, msg.as_string())  # Envoi de l'e-mail
        print(f'E-mail envoyé à {to_email}')
except Exception as e:
    print(f'Échec de l\'envoi de l\'e-mail: {e}')
