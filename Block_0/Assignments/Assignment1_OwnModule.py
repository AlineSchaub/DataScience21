<<<<<<< HEAD
listDic = {}
class ListKeeper:    
    def __init__(self,name,liste):
        self.name = name
        self.liste = liste
        listDic[self.name] = self.liste
    def add(self, name, liste):
        listDic[name] = liste
        print(listDic)
    def show(self):
        print('Alle Namen der Listen: ', listDic.keys())
    def delete(self, name):
        listDic.pop(name)
        print('Listen mit gelöschtem Element: ', listDic)
    def sort(self):
        listDic.keys()
        print('Sortierte Listen: ', listDic)   
    def append(self, name, liste):
        listDic[name].append(liste)
        print('Liste mit dem Namen ', name, 'erweitert: ',listDic)
        
=======
listDic = {}
class ListKeeper:    
    def __init__(self,name,liste):
        self.name = name
        self.liste = liste
        listDic[self.name] = self.liste
    def add(self, name, liste):
        listDic[name] = liste        
    def show(self):
        print('Alle Namen der Listen: ', listDic.keys())
    def delete(self, name):
        listDic.pop(name)
        print('Listen mit gelöschtem Element: ', listDic)
    def sort(self):
        listDic.keys()
        print('Sortierte Listen: ', listDic)   
    def append(self, name, liste):
        listDic[name].append(liste)
        print('Liste mit dem Namen ', name, 'erweitert: ',listDic)
        
>>>>>>> fff4ce7a466ff96ce442a9c3a0a3a5281ec16268
