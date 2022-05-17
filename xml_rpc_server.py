from xmlrpc.server import SimpleXMLRPCServer

def calculatrice(n1,n2,op):
  if (op==+):
    return x + y

  if (op==-):
    return x - y
  
  if (op==*):
    return x * y

  if (op==/):
    return x / y
  

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(calculatrice, "calculatrice")
server.serve_forever()
