# Aplicativo de Reconhecimento Facial

Este repositório contém dois scripts Python para a detecção de rostos em imagens usando a biblioteca OpenCV (Open Source Computer Vision Library).

## facial1.py

Este script `facial1.py` é um aplicativo simples que detecta rostos em uma imagem e desenha retângulos ao redor deles. Ele carrega uma imagem da pasta `img/`, converte-a em tons de cinza e aplica a detecção de rosto. O resultado é exibido em uma janela.

## facial2.py

O script `facial2.py` é uma aplicação mais robusta para a detecção de rostos. Ele carrega uma imagem especificada pelo usuário e verifica a existência de arquivos XML do classificador de rostos. Em seguida, ele carrega o arquivo XML do classificador e aplica a detecção de rosto na imagem. Se nenhum rosto for detectado, uma mensagem de erro será exibida. Caso contrário, retângulos são desenhados ao redor dos rostos detectados e a imagem resultante é exibida em uma janela.
