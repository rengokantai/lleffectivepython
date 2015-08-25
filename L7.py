__author__ = 'Hernan Y.Ke'


UNDEFINED = object()
import json
def parsejson(path):
    handle = open(path, 'r+')
    try:
        data = handle.read()
        op = json.loads(data)
        value = op['num']/op['enum']
    except ZeroDivisionError:
        return UNDEFINED
    else:
        op['result'] = value
        result = json.dumps(op)
        handle.seek(0)
        handle.write(result)
        return  value
    finally:
        handle.close()

path = './file.json'

print (parsejson(path) is UNDEFINED)
