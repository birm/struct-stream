import json
import xmltodict

class sstream:

    def __init__(self,url,variables, parent_name="/", datatype="json", buffer_size=50, time_key=true, key_name=""):
        self.raw=""
        self.data=[None]*buffer_size
        self.keys=[None]*buffer_size
        self.position=0
        self.update()

    def add_next(record,key):
        #what kind of thing to do
        if time_key:
            #loop around like a ring type
            self.data[self.position%self.buffer_size]=record
            #this is a new record
            self.position=self.position+1
        else:
            #replace the item with the same key, but this is slower ( I think)
            #if it's already in
            if key in self.keys:
                self.data[self.keys.index(key)]=record
                #we don't update the position because it's not a unique thing.
            else:
                self.data[self.position%self.buffer_size]=record
                self.position=self.position+1

    def update():
        self.raw=httpget(url)
        switch self.datatype:
            case "json":
                internal = json.loads(self.raw)
                if (not((self.parent_name=="/") or (self.parent_name=="\\")):
                    internal=internal[self.parent_name]
            case "xml":
                internal = xmltodict.parse(raw)
                if (not((self.parent_name=="/") or (self.parent_name=="\\")):
                    internal=internal[self.parent_name]
        for (i=0; i<self.internal.size; i++){
            for (j=0; j<self.variables.size; j++){
                if not time_key:
                    key=self.internal[i][self.key_name]
                try:
                    record[j]=self.internal[i][self.variables[j]]
                except()
                    record[j]="Not Found in Source"
                self.add_next(record,self.keys)
        return 0

    def summarize(function):
        return reduce(lambda *args: None,reduce(function,list(map(list, map(None,*self.data)))))
    
    #currently this is the only custom method
    average_fun = (lambda a, b: a + b, self.data) / len(self.data)
