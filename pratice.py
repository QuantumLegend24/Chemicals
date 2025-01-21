class Elements:
    def __init__(self,name,form,rarity,dangerous,number):
        self.name=name
        self.form=form
        self.rarity=rarity
        self.dangerous=dangerous
        self.number=number

    def properties(self):
        print("Details of the chemicals:")
        print("Name:",self.name)
        print("Form:",self.form)
        print("Rarity:",self.rarity)
        print("Dangerous:",self.dangerous)
        print("Number:",self.number)


c1=Elements("Rhodium","Metal|Solid","Extremely rare","Quite safe",45)
c1.properties()

c2=Elements("Einsteinium","Metal|Solid","Extremely rare","Highly hazardous",99)
c2.properties()

c3=Elements("Oxygen","Gas","Extremely abundant","Almost always safe",8)
c3.properties()

c4=Elements("Astatine","Metalloid|Solid","Extremely rare","Highly hazardous",85)
c4.properties()

c5=Elements("Francium","Metal|Solid","Almost impossible to find","Highly hazardous",87)
c5.properties()

c6=Elements("Gallium","Metal|Solid 30 degrees C+ liquid under 30","Quite rare","Not really toxic",31)
c6.properties()