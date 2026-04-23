import qrcode

# Conteúdo do QR Code
data = "https://www.google.com" # <--- nessa linha coloca a URL do site :) #

qr = qrcode.make(data)

qr.save("qrcode.png")

print("QR Code gerado com sucesso!")