import os

class Nodes:
    """Stores nodes and performs queries"""
    
    def __init__(self):
        print('Initialized nodes subsystem.')

    def add(self, id, data):
        try:
            fhandle = open(str(id), 'wb')
            fhandle.write(data)
            fhandle.close
        except IOError:
            print('Error: Could not add node.')
            pass
    
    def delete(self, id):
        if(self.exists(id)):
            try:
                os.remove(str(id))
            except OSError:
                print('Error: Could not remove node.')
                pass
            
    def exists(self, id):
        try:
            fhandle = open(str(id), 'rb')
            fhandle.close()
            return True
        except IOError:
            return False

    def getNodeData(self, id):
        try:
            fhandle = open(str(id), 'rb')
            data = fhandle.read()
            fhandle.close()
            return data
        except IOError:
            print('Error: Node', str(id), 'does not exist.')
            return False

    def setNodeData(self, id, data):
        try:
            fhandle = open(str(id), 'wb')
            fhandle.write(data)
            fhandle.close()
            return True
        except IOError:
            print('Error: Could not set node data. ')
            return False


