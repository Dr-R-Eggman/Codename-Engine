import json
from enum import Enum
import pygame

class settingType(Enum):
     SETTING = 1
     CONTROL = 2
     SAVE = 3

class File(object):
    def searchForKey(self, searchFor):
        try:
             return next(key for key, value in self.config.items() if value == searchFor)
        except:
             return "";
     
    def searchForAction(self, searchFor):
        return self.config[searchFor]

    def defaultFile(self):
        self.config = defaultSettings(self.stype)
        self.writeFile()

    def changeSetting(self, action, setting):
        self.config[action] = setting
        self.writeFile()

    def writeFile(self):
        f = open(self.file, 'w+')
        f.write(json.dumps(self.config))
        f.close()
        print(type(self.config))

    def readFile(self):
        f = open(self.file, "r+")
        jsonLine = f.readline()
        
        self.config = json.loads(jsonLine)
        
    def __init__(self,stype,file):
        self.config = ""
        self.stype = stype
        if (file == ""):
            if (self.stype == settingType.CONTROL):     
                self.file = "controls.cfg"
            elif (self.stype == settingType.SETTING):
                self.file = "settings.cfg"
            else:
                print("HALT!")
                exit()
        else:
            self.file = file
        try:
            self.readFile()
        except:
            if (stype != settingType.SAVE):    
                self.defaultFile()

def defaultSettings(stype):
    CONTROLS = {"MoveLeft":pygame.K_LEFT,
                   "MoveRight":pygame.K_RIGHT,
                   "MoveUp":pygame.K_UP,
                   "MoveDown":pygame.K_DOWN,
                   "Interact":pygame.K_e,
                   "Shoot":pygame.K_SPACE,
                   "ChangeWpn1":pygame.K_1,
                   "ChangeWpn2":pygame.K_2,
                   "ChangeWpn3":pygame.K_3,
                   "ChangeWpn4":pygame.K_4}

    SETTINGS = {"Res": "1920x1080",
                   "Vol":"0.5",
                   "Vsync":"0",
                   "Hardw":"0"}

    SAVE = {"SP1":"0",
            "SP2":"0",
            "SP3":"0",
            "SP4":"0"}

    if (stype == settingType.SETTING):
        return SETTINGS
    elif (stype == settingType.CONTROL):
        return CONTROLS
    else:
        return SAVE
