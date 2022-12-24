import pygame
import button

pygame.init()

#create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

#game variables
game_paused = False
menu_state = "main"

#define fonts
font = pygame.font.SysFont("arialblack", 40)

#define colours
TEXT_COL = (255, 255, 255)

#load button images
mapa_img = pygame.image.load("images/mostarmapa.png").convert_alpha()
jogadores_img = pygame.image.load("images/jogadores.png").convert_alpha()
problema_img = pygame.image.load("images/problema.png").convert_alpha()
dfs_img = pygame.image.load('images/procuradfs.png').convert_alpha()
bfs_img = pygame.image.load('images/procurabfs.png').convert_alpha()
astar_img = pygame.image.load('images/brocuraastar.png').convert_alpha()
greedy_img = pygame.image.load('images/procuragreedy.png').convert_alpha()
sair_img = pygame.image.load('images/sair.png').convert_alpha()


#create button instances
mapa_button = button.Button(304, 125, mapa_img, 1)
jogadores_button = button.Button(297, 250, jogadores_img, 1)
problema_button = button.Button(336, 375, problema_img, 1)
dfs_button = button.Button(226, 75, dfs_img, 1)
bfs_button = button.Button(225, 200, bfs_img, 1)
astar_button = button.Button(246, 325, astar_img, 1)
greedy_button = button.Button(332, 450, greedy_img, 1)
sair_button = button.Button(225, 200, sair_img, 1)

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#game loop
run = True
while run:

  screen.fill((52, 78, 91))

  #check if game is paused
  if game_paused == True:
    #check menu state
    if menu_state == "main":
      #draw pause screen buttons
      if resume_button.draw(screen):
        game_paused = False
      if options_button.draw(screen):
        menu_state = "Jogadores"
      if quit_button.draw(screen):
        run = False
    #check if the options menu is open
    if menu_state == "options":
      #draw the different options buttons
      if video_button.draw(screen):
        print("Video Settings")
      if audio_button.draw(screen):
        print("Audio Settings")
      if keys_button.draw(screen):
        print("Change Key Bindings")
      if back_button.draw(screen):
        menu_state = "main"
  else:
    draw_text("Press SPACE to pause", font, TEXT_COL, 160, 250)

  #event handler
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        game_paused = True
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()