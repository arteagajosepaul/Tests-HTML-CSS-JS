import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuraciones de la ventana
ancho_pantalla, alto_pantalla = 800, 600
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
pygame.display.set_caption('Movimiento de Personaje con Fondo')

# Cargar la imagen de fondo
fondo_imagen = pygame.image.load('bosque.png').convert()  # Asegúrate de tener el archivo
# Escalar la imagen de fondo al tamaño de la ventana, si es necesario
fondo_imagen = pygame.transform.scale(fondo_imagen, (ancho_pantalla, alto_pantalla))

# Cargar las imágenes del personaje
personaje_imagen1 = pygame.image.load('figura 1.png').convert_alpha()
personaje_imagen2 = pygame.image.load('figura 2.png').convert_alpha()

# Lista de imágenes para la animación
imagenes_personaje = [personaje_imagen1, personaje_imagen2]
indice_imagen = 0  # Índice de la imagen actual en la animación

# Coordenadas iniciales del personaje
pos_x = ancho_pantalla // 2
pos_y = alto_pantalla // 2

# Velocidad de movimiento del personaje
velocidad = 5

# Control de tiempo para la animación
tiempo_ultimo_cambio = pygame.time.get_ticks()

# Bucle principal del juego
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Obtener todas las teclas presionadas
    teclas_presionadas = pygame.key.get_pressed()

    # Mover el personaje con las teclas de flecha
    moviendose = False
    if teclas_presionadas[pygame.K_LEFT]:
        pos_x -= velocidad
        moviendose = True
    if teclas_presionadas[pygame.K_RIGHT]:
        pos_x += velocidad
        moviendose = True

    # Actualizar el índice de imagen para la animación si el personaje se está moviendo
    if moviendose and pygame.time.get_ticks() - tiempo_ultimo_cambio > 100:
        tiempo_ultimo_cambio = pygame.time.get_ticks()
        indice_imagen = (indice_imagen + 1) % len(imagenes_personaje)

    # Mantener al personaje dentro de los límites de la pantalla
    pos_x = max(0, min(ancho_pantalla - personaje_imagen1.get_width(), pos_x))

    # Actualizar la pantalla
    pantalla.blit(fondo_imagen, (0, 0))  # Dibuja el fondo
    pantalla.blit(imagenes_personaje[indice_imagen], (pos_x, pos_y))  # Dibuja el personaje encima del fondo

    # Refrescar la pantalla
    pygame.display.flip()

    # Controlar la tasa de refresco de la pantalla
    pygame.time.Clock().tick(60)

# Salir de Pygame
pygame.quit()
sys.exit()
