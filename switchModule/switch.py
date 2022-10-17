



from email.policy import default


def switch(txt:str,case={}):
    default = "default" in case
    txt_ = txt in case
    # print(txt_,default)
    
    # print(1 and case[txt]() or 2 and 4)
    # print(case[txt]())

    if txt_:
        case[txt]()
    elif default:
        case["default"]()

    # (lambda: txt_ and case[txt]() or default and case["default"]())()


def p():
    print("lol")

def d():
    print("sddl")

def sd():
    print("sdddddl")
switch("v",case={
    "Vv":d,
    "lol":p,
    # "default":sd

                

})