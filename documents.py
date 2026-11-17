class Documents:
    def __init__(self):self.items={}
    def open(self,item):self.items[item['uri']]={'version':item['version'],'text':item['text']}
    def close(self,uri):self.items.pop(uri,None)
    def text(self,uri):return self.items[uri]['text']
