


from jsmodule import setInterval ,clearInterval ,setTimeout,clearTimeout




def pri():
    print("ll")


v = setInterval(pri, 1000)
def pri2():
   clearInterval(v)
c = setTimeout(pri2, 5000)
