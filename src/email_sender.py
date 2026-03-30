import smtplib
from email.message import EmailMessage

def enviar_email(arquivo_excel):

    email_remetente = "oirisinacio@gmail.com"
    senha = "joseatnafirlkkfu"
    email_destino = "oirisdc@gmail.com"

    msg = EmailMessage()

    msg["Subject"] = "Relatório automático de cotação de moedas"
    msg["From"] = email_remetente
    msg["To"] = email_destino

    msg.set_content("Segue em anexo o relatório automático das cotações.")

    with open(arquivo_excel, "rb") as f:
        dados = f.read()

    msg.add_attachment(
        dados,
        maintype="application",
        subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename="dados_cotacoes.xlsx"
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

        smtp.login(email_remetente, senha)
        smtp.send_message(msg)

    print("Email enviado com sucesso")