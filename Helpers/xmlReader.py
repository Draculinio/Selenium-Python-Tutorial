#from xml.etree import ElementTree
from xml.dom import minidom
class xmlReader:
    def __init__(self):
        #self.my_dom = ElementTree.parse('./Config/configuration.xml')
        self.documento = minidom.parse('./Config/configuration.xml')


    def obtener_datos(self,dato):
        item = self.documento.getElementsByTagName(dato)[0].firstChild.nodeValue
        print(item)
        return item
