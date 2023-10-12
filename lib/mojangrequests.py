class mojangapi():
    def __init__(self):
         self.urls = self.URL()
         self.capes = self.CAPE()
         
    class URL():
        def __init__(self):
            self.uuid = "https://api.mojang.com/users/profiles/minecraft/"
            self.profile = "https://sessionserver.mojang.com/session/minecraft/profile/"
            self.A_check = "https://api.minecraftservices.com/minecraft/profile/name/"
            self.A_check2 = "/available"

    class CAPE():
        def __init__(self):
                self._migrator = ""
                self._2011 =  ""
                self._2012 = "http://textures.minecraft.net/texture/a2e8d97ec79100e90a75d369d1b3ba81273c4f82bc1b737e934eed4a854be1b6"
