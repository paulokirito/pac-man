import pygame
import random

# Inicializar Pygame
pygame.init()

# Configurações da tela
WIDTH = 800
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pac Man')

# Carregar imagens
PACMAN_IMAGE = pygame.image.load('pacman.png')
GHOST_IMAGE = pygame.image.load('ghost.png')

# Posições iniciais
pacman_position = [WIDTH // 2, HEIGHT // 2]
ghost_position = [WIDTH // 2 + 50, HEIGHT // 2]

# Funções de movimento
def move_pacman(keys):
    if keys[pygame.K_UP]:
        pacman_position[1] -= 5
    if keys[pygame.K_DOWN]:
        pacman_position[1] += 5
    if keys[pygame.K_LEFT]:
        pacman_position[0] -= 5
    if keys[pygame.K_RIGHT]:
        pacman_position[0] += 5

def move_ghost():
    ghost_position[0] += random.randint(-5, 5)
    ghost_position[1] += random.randint(-5, 5)

# Loop principal do jogo
running = True
while running:
    # Verificar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Verificar teclas pressionadas
    keys = pygame.key
