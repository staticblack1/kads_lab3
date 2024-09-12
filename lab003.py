from lab_chat import get_peer_node, get_channel


def get_username():
    username= input("please enter your desired username: ")
    username=username.strip().upper()
    return username
def get_group():
    groupname= input("enter group name")
    groupname=groupname.strip().upper()
    return groupname
def get_message():
    message=input("enter message")
    message=message.strip()
    return message


def initialize_chat():
    user= get_username()
    group = get_group()
    node= get_peer_node(user)
    return get_channel(node, group)

def start_chat():
    channel = initialize_chat()

    while True:
        try:
            msg = get_message()
            channel.send(msg.encode('utf_8'))
        except (KeyboardInterrupt, SystemExit):
            break
    channel.send("$$STOP".encode('utf_8'))
    print("FINISHED")

start_chat()

