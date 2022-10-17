
import requests



def fetch (url,option):
    htmlmethod ={"get":requests.get,"post":requests.post,"delete":requests.delete,"patch":requests.patch,"put":requests.put}
    method = option["method"] or "get"
    if  not (hasattr(requests,method) and  method in htmlmethod):
        raise "invalid method"


    ## the header specified should be in the request format
    return htmlmethod[method]((url), option["body"], option["header"])
   
   
    
    

print(requests)
        