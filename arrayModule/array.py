
# inhering the list Module and adding more functions




class Array_(list):
    def __init__(self,arr:list):
        super().__init__(arr)
        super().__setattr__("splice",self.splice)
        super().__setattr__("split",self.split)
        
        
        
    def splice(self ,a=0,b=0,str:list=[]) ->list:
     
        self[a:b] =str
    def split(self ,a=0,b=None) ->list:
      c = b != None and b  or len(self) 
      return  self[a:c] 


# a = Array_([1,2,3,4,5])
# print(a)
# a.splice(1,2,["aa"])
# print(a.split(1,2))

