
import pygame
import os

# steuerung mit pfeiltasten

class Settings:  # Settigns einstellung mit allen variabel für programmieren
    window_width = 1000
    window_height = 700
    path_file = os.path.dirname(os.path.abspath(__file__))
    path_image = os.path.join(path_file, "images")
    fps = 60
    caption = "Ibrahim Aldemir GAME"
    spaceship_width = 70
    spaceship_height = 70
    spaceship_pos_x = window_width / 2
    spaceship_pos_y = window_height / 2
    number_h = 1 
    number_v = -1
    number_h_2 = -1 
    number_v_2 = 1
    





class Background(pygame.sprite.Sprite):  # klasse background/ hintergrund
    def __init__(self, filename="background.png") -> None:
        super().__init__()
        self.image = pygame.image.load(os.path.join(Settings.path_image, filename)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (Settings.window_width, Settings.window_height))

    def draw(self, screen):  # im fenster dastellen
        screen.blit(self.image, (0, 0))


class spaceship(pygame.sprite.Sprite):  # klasse spaceship
    def __init__(self) -> None:
        super().__init__()
        self.original_image_0  = pygame.image.load(os.path.join(Settings.path_image, "0.png")).convert_alpha()
        self.original_image_1  = pygame.image.load(os.path.join(Settings.path_image, "1.png")).convert_alpha()
        self.original_image_2  = pygame.image.load(os.path.join(Settings.path_image, "2.png")).convert_alpha()
        self.original_image_3  = pygame.image.load(os.path.join(Settings.path_image, "3.png")).convert_alpha()
        self.original_image_4  = pygame.image.load(os.path.join(Settings.path_image, "4.png")).convert_alpha()
        self.original_image_5  = pygame.image.load(os.path.join(Settings.path_image, "5.png")).convert_alpha()
        self.original_image_6  = pygame.image.load(os.path.join(Settings.path_image, "6.png")).convert_alpha()
        self.original_image_7  = pygame.image.load(os.path.join(Settings.path_image, "7.png")).convert_alpha()
        self.original_image_8  = pygame.image.load(os.path.join(Settings.path_image, "8.png")).convert_alpha()
        self.original_image_9  = pygame.image.load(os.path.join(Settings.path_image, "9.png")).convert_alpha()
        self.original_image_10 = pygame.image.load(os.path.join(Settings.path_image, "10.png")).convert_alpha()
        self.original_image_11 = pygame.image.load(os.path.join(Settings.path_image, "11.png")).convert_alpha()
        self.original_image_12 = pygame.image.load(os.path.join(Settings.path_image, "12.png")).convert_alpha()
        self.original_image_13 = pygame.image.load(os.path.join(Settings.path_image, "13.png")).convert_alpha()
        self.original_image_14 = pygame.image.load(os.path.join(Settings.path_image, "14.png")).convert_alpha()
        self.original_image_15 = pygame.image.load(os.path.join(Settings.path_image, "15.png")).convert_alpha()
        
        self.original_image = self.original_image_0

        self.image = pygame.transform.scale(self.original_image, (Settings.spaceship_width, Settings.spaceship_height))
        self.rect = self.image.get_rect()
        self.rect.left = Settings.spaceship_pos_x
        self.rect.top = Settings.spaceship_pos_y
        self.speed_h = -3
        self.speed_v = -1


    def update(self):  # wand wird erstellt
        self.rect.move_ip(self.speed_v,self.speed_h)
        
        if self.rect.top >= Settings.window_height:
            self.rect.centery = 2
        if self.rect.centery <= 0:
            self.rect.centery = Settings.window_height 
            
        if self.rect.left >= Settings.window_width:
            self.rect.centerx = 2
        if self.rect.centerx <= 0:
            self.rect.centerx = Settings.window_width 
        
        if self.speed_h == -4 and self.speed_v == 0:
            self.image = self.original_image_0
        elif self.speed_h == -3 and self.speed_v == -1:
            self.image = self.original_image_1
        elif self.speed_h == -2 and self.speed_v == -2:
            self.image = self.original_image_2
        elif self.speed_h == -1 and self.speed_v == -3:
            self.image = self.original_image_3
        elif self.speed_h == 0 and self.speed_v == -4:
            self.image = self.original_image_4
        elif self.speed_h == 1 and self.speed_v == -3:
            self.image = self.original_image_5
        elif self.speed_h == 2 and self.speed_v == -2:
            self.image = self.original_image_6
        elif self.speed_h == 3 and self.speed_v == -1:
            self.image = self.original_image_7
        elif self.speed_h == 4 and self.speed_v == 0:
            self.image = self.original_image_8
        elif self.speed_h == 3 and self.speed_v == 1:
            self.image = self.original_image_9
        elif self.speed_h == 2 and self.speed_v == 2:
            self.image = self.original_image_10
        elif self.speed_h == 1 and self.speed_v == 3:
            self.image = self.original_image_11
        elif self.speed_h == 0 and self.speed_v == 4:
            self.image = self.original_image_12
        elif self.speed_h == -1 and self.speed_v == 3:
            self.image = self.original_image_13
        elif self.speed_h == -2 and self.speed_v == 2:
            self.image = self.original_image_14
        elif self.speed_h == -3 and self.speed_v == 1:
            self.image = self.original_image_15
        
        if self.speed_h >= 5:
            self.speed_h = 4 
        
    def draw(self, screen):  # im fenster dastellen
        screen.blit(self.image, self.rect)
        


class Game(object):  # klasse game
    def __init__(self, ) -> None:
        super().__init__()
        os.environ['SDL_VIDEO_WINDOW_POS'] = "100,100"

        pygame.init()
        pygame.display.set_caption(Settings.caption)
        self.screen = pygame.display.set_mode((Settings.window_width, Settings.window_height))
        self.clock = pygame.time.Clock()
        self.background = Background()
        self.spaceship = spaceship()
        self.number_v = 1
        self.number_v_2 = 1
        self.number_h_2 = 1
        self.number_h = 1

 #       if self.spaceship.speed_h >= 5:
#   self.number_h = Settings.number_h
  #      elif self.spaceship.speed_h <= -5:
  #          self.number_h_2 = Settings.number_h_2
  #self      if self.spaceship.speed_v <=5:
  #          self.number_v = Settings.number_v
   #     elif self.spaceship.speed_v <= -5:
   #         self.number_v_2 = Settings.number_v_2

    def run(self):  # beim spiel start ausführen
        self.running = True
        while self.running:
            self.clock.tick(Settings.fps)
            self.update()
        pygame.quit()

    def update(self):  # alle funktionen werden in eine gesteckt
        self.draw_on_screen()
        self.spaceship.update()
        self.watch_for_events()

        
    def draw_on_screen(self):  # draw alle bitmaps in der funktion
        self.background.draw(self.screen)
        self.spaceship.draw(self.screen)

        pygame.display.flip()

    def watch_for_events(self):  # steuerung
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                
            # Movment
            if event.type == pygame.KEYDOWN:  # hoch
                if event.key == pygame.K_UP:
                    pass
                #self.spaceship.rect.top = self.spaceship.speed_h
            if event.type == pygame.KEYDOWN:  # runter
                if event.key == pygame.K_DOWN:
                    pass
                    #self.spaceship.rect.top += self.spaceship.speed_h
            if event.type == pygame.KEYDOWN:  # links
                if event.key == pygame.K_LEFT:
                    self.spaceship.speed_v -= self.number_v
                    self.spaceship.speed_h += self.number_h
                    print(self.spaceship.speed_h,self.spaceship.speed_v)
            if event.type == pygame.KEYDOWN:  # rechts
                if event.key == pygame.K_RIGHT:
                    self.spaceship.speed_v += self.number_v_2
                    self.spaceship.speed_h -= self.number_h_2
                    print(self.spaceship.speed_h,self.spaceship.speed_v)

            key_input = pygame.key.get_pressed()

if __name__ == '__main__':  # game start
    game = Game()
    game.run()
