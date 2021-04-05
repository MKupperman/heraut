# Heraut

Heraut, the herald of pythonic message passing.

A python 3.6+ package for message passing between threads.

## Minimal example:

#### Sending Information
```python
import heraut

# Initialize the sender, once per process per sender
sender = heraut.Sender(name='process A')
# Send the message
sender.send(message='hello world', label='', target='process B')
# Tell the listner no more messages will be coming. 
sender.stop_listener(target='process B')
```

#### Recieving Information

```python
import  heraut

listener = heraut.Listener()
while listener.listening():
    # get the message
    message, label, metadata = listener.get_message()
    # do something with the message
    print(message)
# Shut down the listner. 
listener.end()
```
