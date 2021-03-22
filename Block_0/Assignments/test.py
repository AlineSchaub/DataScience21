listDic = {}
class ListKeeper:
    def __init__(self, name,liste):
        listDic[name] = liste
    def add(name, liste):
        listDic[name] = liste        
    def show():
        print('Alle Namen der Listen: ', listDic.keys())
    def delete(name):
        listDic.pop(name)
        print('Listen mit gelöschtem Element: ', listDic)
    def sort(name):
        listDic.keys()
        print('Sortierte Listen: ', listDic)   
    def append(name, liste):
        listDic[name].append(liste)
        print('Liste mit dem Namen ', name, 'erweitert: ',listDic)
        
