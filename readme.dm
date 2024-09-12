from pyre import Pyre (from= function, pyre= module, import= function,
from pyre import zhelper= Zhelper=module
import zmq= zmq =module
import uuid= uuid= module
import json= json = module

def get_peer_node(username): ( def =function, get_peer_nobe= variable, username= parameter)
    n = Pyre(username) =( n= variable, pyre(username)=parameter
    #n.set_header("CHAT_Header1","example header1")
    #n.set_header("CHAT_Header2","example header2")
    n.start()
    return n
def join_group(node, group):(function header) def= function used to craete a funtion) join_group(variable- name of the function), (node, group=parameter, description of the function)
    node.join(group)
    print(f"Joined group: {group}") ( print= function, used to call forth a function result