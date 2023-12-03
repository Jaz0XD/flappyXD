import pygame.sprite
import configs
import assets
from layer import Layer

class Music(pygame.sprite.Sprite):
    def __init__ (self, index,*groups):
        self._layer = Layer.UI
        self.image = assets.get_sprite("musiccredits")
        self.rect = self.image.get_rect(bottomleft= (configs.SCREEN_WIDTH * index , configs.SCREEN_HEIGHT))
        self.mask = pygame.mask.from_surface(self.image)
        super().__init__(*groups)
