import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def enviar_email(remetente, senha, destinatario, assunto, mensagem):
    try:
        servidor = smtplib.SMTP("smtp.gmail.com", 587)
        servidor.starttls()

        servidor.login(remetente, senha)

        msg = MIMEMultipart()
        msg["From"] = remetente
        msg["To"] = destinatario
        msg["Subject"] = assunto

        msg.attach(MIMEText(mensagem, "plain"))

        servidor.send_message(msg)
        servidor.quit()

        print("Email enviado com sucesso!")

    except Exception as e:
        print("Erro ao enviar:", e)


# ================= USO ================= #
if __name__ == "__main__":
    remetente = "email@gmail.com"
    senha = "SUA_SENHA_DE_APP"

    destinatario = input("testes_email.com")
    assunto = input("Assunto: ")
    mensagem = input("Mensagem: ")

    enviar_email(remetente, senha, destinatario, assunto, mensagem)