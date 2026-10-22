class Picture:
    def __init__(self, DescriptionP, WidthP, HeightP, FrameColourP):
        self._Description = DescriptionP
        self._Width = WidthP
        self._Height = HeightP
        self._FrameColour = FrameColourP

    def GetDescription(self):
        return self._Description
    def GetWidth(self):
        return self._Width
    def GetHeight(self):
        return self._Height
    def GetFrameColour(self):
        return self._FrameColour
    
    def SetDescription(self, DescriptionP):
        self._Description = DescriptionP
    
PictureArray = []
for i in range(100):
    PictureArray.append(Picture("",0,0,""))
    
def ReadData():
    with open("Pictures.txt") as file:
        
