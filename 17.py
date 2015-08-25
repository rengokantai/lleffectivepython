__author__ = 'Hernan Y.Ke'

def log(message, *args):
    if not args:
        print(message)
    else:
        message=message+",".join(str(i) for i in args)
        print (message)

lis =[1,2,3]
log("hello",*lis)
log("hello",lis)
log("hello",1,2,3)