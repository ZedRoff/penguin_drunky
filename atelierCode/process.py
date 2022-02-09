### ====================================================================================================
### IMPORTS
### ====================================================================================================
import arcade
from utils import *
import random
import time
class Process:
    ### ====================================================================================================
    ### PARAMETERS
    ### ====================================================================================================
    SCREEN_WIDTH = int(1920 * 0.75)
    SCREEN_HEIGHT = int(1080 * 0.75)

    ### ====================================================================================================
    ### CONSTRUCTOR
    ### ====================================================================================================
    def __inipt__(self):
        pass

    ### ====================================================================================================
    ### INIT
    ### ====================================================================================================
    def setup(self):
        params = {
            "filePath": "images/backgrounds/night.png",
            "filterColor": (255, 255, 255, 160),
            "position": (self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2)
        }
        self.param_particle_penguin = {
            "imagePath": "images/characters/penguin.png",
            "spriteBox": (5,1,250,250),
            "spriteSelect":(4,0),
            "x0": 0,
            "y0": 0,
            "partSize": 50,
            "partScale": 1,
            "partSpeed": 0,
            "color":(255,255,255,160),
            "startAlpha": 25,
            "endAlpha":0,
            "partNB":50,
            "maxLifeTime":0.5,
            "flipH": False
        }
        self.params2 = {
            "filePath": "images/characters/penguin.png",
            "position": (self.SCREEN_WIDTH // 2, 125),
            "spriteBox":(5,1,250,250),
            "startIndex":0,
            "endIndex":4,
            "frameDuration": 4/60,
            "flipH":False
        }
        self.paramLife_1 = {
            "filePath": "images/items/heart.png",
            "position": (100, self.SCREEN_HEIGHT-100),
            "size": (50,50)
        }
        self.paramLife_2 = {
            "filePath": "images/items/heart.png",
            "position": (150, self.SCREEN_HEIGHT - 100),
            "size": (50, 50)
        }
        self.paramLife_3 = {
            "filePath": "images/items/heart.png",
            "position": (200, self.SCREEN_HEIGHT - 100),
            "size": (50, 50)
        }

        self.params3 = {
            "filePath":"images/items/beers.png",
            "filterColor": (255, 255, 255, 160),
            "position":(self.SCREEN_WIDTH//2,self.SCREEN_HEIGHT//2),
            "spriteBox":(3,3,180,180),
            "startIndex":0,
            "endIndex": 8,
        }
        self.paramsScore = {
            "x":self.SCREEN_WIDTH - 100,
            "y":self.SCREEN_HEIGHT - 100,

            "message": "0",
            "size": 25,
            "bold": True,
            "italic": True,
            "color": (255,255,255,255)


        }
        self.gameOver = {
            "x": self.SCREEN_WIDTH // 2,
            "y": self.SCREEN_HEIGHT // 2,
            "message": "",
            "size": 75,
            "bold": True,
            "color": (255,255,255,255),
            "alignH": "center"
        }
        self.deaths = 0
        self.heart_1 = createFixedSprite(self.paramLife_1)
        self.heart_2 = createFixedSprite(self.paramLife_2)
        self.heart_3 = createFixedSprite(self.paramLife_3)
        self.background = createFixedSprite(params)
        self.player = createAnimatedSprite(self.params2)
        self.movingL = False
        self.movingR = False
        self.player.set_texture(0)
        self.items = createAnimatedSprite(self.params3)
        self.items.set_texture(0)
        self.item_destroyed = True
        self.bool_gameOver = False
        self.difficulty = 0
        self.count = 0
        self.particles_penguin = createParticleEmitter(self.param_particle_penguin)

    ### ====================================================================================================
    ### UPDATE
    ### ====================================================================================================
    def update(self, deltaTime):

        self.particles_penguin.update()
        self.particles_penguin.center_x = self.player.center_x
        self.particles_penguin.center_y = self.player.center_y
        self.player.set_texture(0)
        if not self.bool_gameOver:
            if self.movingR == self.movingL:
                self.particles_penguin.center_y = -10000
            if self.movingL:
                self.params2["flipH"] = True
                self.params2["position"] = (self.player.center_x,125)
                self.player = createAnimatedSprite(self.params2)
                self.player.center_x -= 20 + self.difficulty
                self.player.set_texture(4)
                self.param_particle_penguin["flipH"] = True
            if self.movingR:
                self.params2["flipH"] = False
                self.params2["position"] = (self.player.center_x, 125)
                self.player = createAnimatedSprite(self.params2)
                self.player.center_x += 20 + self.difficulty
                self.player.set_texture(4)
                self.param_particle_penguin["flipH"] = False
            if self.player.center_x <= 100:
                self.player.center_x= 101
            if self.player.center_x >= self.SCREEN_WIDTH - 75:
                self.player.center_x= self.SCREEN_WIDTH -76
            if self.item_destroyed:
                self.params3["position"] = (random.randint(100, self.SCREEN_WIDTH - 75), self.SCREEN_HEIGHT)
                self.items = createAnimatedSprite(self.params3)
                self.items.set_texture(random.randint(0,8))
                self.item_destroyed = False
            if self.items.center_y <= 0:
                self.item_destroyed = True
                self.deaths+=1
            if self.deaths == 1:
                self.paramLife_3["filterColor"] = (255,255,255,0)
                self.heart_3 = createFixedSprite(self.paramLife_3)
            elif self.deaths == 2:
                self.paramLife_2["filterColor"] = (255,255,255,0)
                self.heart_2 = createFixedSprite(self.paramLife_2)

            if self.deaths == 3:
                self.paramLife_1["filterColor"] = (255, 255, 255, 0)
                self.heart_1 = createFixedSprite(self.paramLife_1)
                reply = ""
                if int(self.paramsScore["message"]) >= 15:
                    reply = "Pretty Good =)"
                elif int(self.paramsScore["message"]) >= 10 and int(self.paramsScore["message"])  < 15:
                    reply = "You could've done better"
                elif int(self.paramsScore["message"]) < 10:
                    reply = "Review your strategy"

                self.gameOver["message"] = "GAME OVER \nYour Score Was : {}\n{}".format(self.paramsScore["message"], reply)
                self.paramsScore["message"] = 0

                self.deaths = 0
                self.bool_gameOver = True


                self.paramLife_1["filterColor"] = (255, 255, 255, 255)
                self.heart_1 = createFixedSprite(self.paramLife_1)

                self.paramLife_2["filterColor"] = (255, 255, 255, 255)
                self.heart_2 = createFixedSprite(self.paramLife_2)

                self.paramLife_3["filterColor"] = (255, 255, 255, 255)
                self.heart_3 = createFixedSprite(self.paramLife_3)
                self.count = 0
                self.difficulty = 0

        if abs(self.items.center_x // 2 - self.player.center_x // 2) <= 50 and abs(self.items.center_y // 2 - self.player.center_y // 2) <= 50:
            self.item_destroyed = True
            self.paramsScore["message"] = str(int(self.paramsScore["message"])+1)
            self.count += 1
            if self.count == 3:
                self.difficulty += 2
                self.count = 0
        self.items.center_y -= (10 + self.difficulty//2)


    ### ====================================================================================================
    ### RENDERING
    ### ====================================================================================================
    def draw(self):
        self.background.draw()
        self.player.draw()
        self.items.draw()
        self.heart_1.draw()
        self.heart_2.draw()
        self.heart_3.draw()
        drawText(self.paramsScore)
        drawText(self.gameOver)
        self.particles_penguin.draw()
    ### ====================================================================================================
    ### KEYBOARD EVENTS
    ### key is taken from : arcade.key.xxx
    ### ====================================================================================================
    def onKeyEvent(self, key, isPressed):
        if int(key) == 65361:

            self.movingL = isPressed

        elif int(key) == 65363:

            self.movingR = isPressed
        elif arcade.key.SPACE and isPressed and self.bool_gameOver:
            self.gameOver["message"] = ""
            self.bool_gameOver = False



        # print(f"key={key} - isPressed={isPressed}")


    ### ====================================================================================================
    ### GAMEPAD BUTTON EVENTS
    ### buttonName can be "A", "B", "X", "Y", "LB", "RB", "VIEW", "MENU", "LSTICK", "RSTICK"
    ### ====================================================================================================
    def onButtonEvent(self, gamepadNum, buttonName, isPressed):
        print(f"GamePad={gamepadNum} - ButtonNum={buttonName} - isPressed={isPressed}")

    ### ====================================================================================================
    ### GAMEPAD AXIS EVENTS
    ### axisName can be "X", "Y", "RX", "RY", "Z"
    ### ====================================================================================================
    def onAxisEvent(self, gamepadNum, axisName, analogValue):
        print(f"GamePad={gamepadNum} - AxisName={axisName} - Value={analogValue}")

    ### ====================================================================================================
    ### MOUSE MOTION EVENTS
    ### ====================================================================================================
    def onMouseMotionEvent(self, x, y, dx, dy):
        #print(f"MOUSE MOTION : x={x}/y={y} dx={dx}/dy={dy}")
        pass

    def onMouseButtonEvent(self, x, y, buttonNum, isPressed):
        print(x,y,buttonNum,isPressed)