import pygame

class EntityShape():
   def __init__(self,pid,pos,size):
        self.rect = pygame.Rect[pos[0], pos[1], size[0], size[1]]
        self.id = ""
        self.colour = ((255,255,255))
        self.text = ""

class EntityImage(pygame.sprite.Sprite):
    def __init__(self,pid,pos,image,alpha):
        super().__init__()
        self.id = ""
        self.text = ""

        if (convert):
            self.image = pygame.image.load(image).convert()
        else:
            self.image = pygame.image.load(image)
        
        self.rect = pygame.Rect(pos[0], pos[1], self.image.get_width(), self.image.get_height())

    def addText(self, text, font, pos, colour):
        if (text != ""):
            myfont = pygame.font.SysFont(font[0], font[1])
            label = myfont.render(text, 1, (colour))
            self.image.blit(label, (pos[0], pos[1]))

    def resizeImage(self, res):
        picture = pygame.transform.scale(picture, (res[0], res[1]))
