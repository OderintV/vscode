class Tree:
    def __init__(self, name, hGrowth, maxHeight, maxWidth, evergreen):
        self._TreeName = name
        self._HeightGrowth = hGrowth
        self._MaxHeight = maxHeight
        self._MaxWidth = maxWidth
        self._Evergreen = evergreen
        
    def GetTreeName(self):
        return self._TreeName
    def GetGrowth(self):
        return self._HeightGrowth
    def GetMaxHeight(self):
        return self._MaxHeight
    def GetMaxWidth(self):
        return self._MaxWidth
    def GetEvergreen(self):
        return self._Evergreen

def ReadData():
    TreeObjects = []
    try:
        
    