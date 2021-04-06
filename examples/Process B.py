from src import heraut

listener = heraut.Listener(name='process B')
flag = True
while flag and listener.listening():
    # get the message
    flag, message, label, metadata = listener.get_message()
    # do something with the message
    print(message)
# Shut down the listner.
listener.end()
