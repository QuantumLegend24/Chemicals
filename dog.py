class Dogs:
    def __init__(self,name,breed,rarity,dangerous):
        self.name=name
        self.breed=breed
        self.rarity=rarity
        self.dangerous=dangerous

    def properties(self):
        print("Details of dogs:")
        print("Name:",self.name)
        print("Breed:",self.breed)
        print("Rarity:",self.rarity)
        print("Dangerous:",self.dangerous)


Dog1=Dogs("Astro","German Shephard","Common","Quite safe")
Dog1.properties()

Dog2=Dogs("Hero","Shihpoo","Little rare","Very safe")
Dog2.properties()

Dog3=Dogs("Bella","Pitbull","Common","Very dangerous (Especially if they aren't trained well)")
Dog3.properties()

Dog4=Dogs("Max","Chihuahua","Common","Very safe")
Dog4.properties()

Dog5=Dogs("Teddy","Golden Retriever","Quite common","Very safe")
Dog5.properties()

Dog6=Dogs("Luna","Xoloitzcuintli","Very rare","Quite safe")
Dog6.properties()

Dog7=Dogs("Ice","Siberian Husky","Quite common","A bit dangerous")
Dog7.properties()