import qrcode

def main():
    img = qrcode.make("hola alex")
    img.save("hola_alex_qr.png")

if __name__ == "__main__":
    main()
