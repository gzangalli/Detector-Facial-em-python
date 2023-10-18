import cv2
import os


def detect_faces(image_path):
    try:
        # caminho do arquivo XML do classificador
        cascade_path = os.path.join(
            os.getcwd(), 'haarcascade_frontalface_default.xml')

        # verificar se o arquivo XML do classificador existe
        if not os.path.isfile(cascade_path):
            raise FileNotFoundError(
                'O arquivo XML do classificador não foi encontrado.')

        # carregar o arquivo de cascata frontal de rostos pré-treinado
        face_cascade = cv2.CascadeClassifier(cascade_path)

        # verificar se o arquivo de imagem existe
        if not os.path.isfile(image_path):
            raise FileNotFoundError('A imagem não foi encontrada.')

        # ler a imagem
        image = cv2.imread(image_path)

        # verificar se a imagem foi carregada corretamente
        if image is None:
            raise ValueError('Falha ao carregar a imagem.')

        # converter para escala de cinza
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # detectar rostos na imagem
        faces = face_cascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # verificar se algum rosto foi detectado
        if len(faces) == 0:
            raise ValueError('Nenhum rosto foi detectado na imagem.')

        # desenhar retângulos ao redor dos rostos detectados
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # mostrar a imagem com os rostos detectados
        cv2.imshow('Detecção de Rostos', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except Exception as e:
        print(f'Erro: {str(e)}')


# caminho da imagem
image_path = 'img/dale2.jfif'

#  função para a detecção de rostos
detect_faces(image_path)
