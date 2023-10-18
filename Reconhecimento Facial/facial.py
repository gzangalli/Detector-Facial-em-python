import cv2


def detectar_rosto(imagem):

    cascata_rosto = cv2.CascadeClassifier(
        'haarcascade_frontalface_default.xml')
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    cascata_rosto = cv2.CascadeClassifier(
        'haarcascade_frontalface_default.xml')
    faces = cascata_rosto.detectMultiScale(
        imagem_cinza, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(imagem, (x, y), (x+w, y+h), (0, 255, 0), 2)

    return imagem


def main():
    # carregar a imagem
    try:
        imagem = cv2.imread('img/dale.jpg')
        if imagem is None:
            raise Exception("Erro ao carregar a imagem.")
    except Exception as e:
        print(str(e))
        return None

    # aplicar a detecção de rosto na imagem
    imagem_detectada = detectar_rosto(imagem)

    # exibir a imagem resultante
    cv2.imshow('Aplicativo de Reconhecimento Facial', imagem_detectada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
