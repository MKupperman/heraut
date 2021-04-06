# Heraut

Heraut, the herald of pythonic message passing.

A python 3.6+ package for message passing between threads and processes.

## Minimal example:

#### Sending Information

```python

from src import heraut

# Initialize the sender, once per process per sender
sender = heraut.Sender(name='process A')
# Send the message
sender.send(message='hello world', label='', target='process B')
# Tell the listner no more messages will be coming. 
sender.stop_listener(target='process B')
```

#### Recieving Information

```python

from src import heraut

listener = heraut.Listener()
flag = True
while flag and listener.listening():
    # get the message
    flag, message, label, metadata = listener.get_message()
    # do something with the message
    print(message)
# Shut down the listner. 
listener.end()
```
