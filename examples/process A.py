from src import heraut

# Initialize the sender, once per process per sender
sender = heraut.Sender(name='process A')
# Send the message
sender.send(message='hello world', label='', target='process B')
# Tell the listner no more messages will be coming.
sender.stop_listener(target='process B')
