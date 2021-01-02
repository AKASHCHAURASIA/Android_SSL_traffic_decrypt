import frida
import time
import sys
import os
def on_message(message, data):

    if message['type'] == 'send':
        message_payload = []
        message_payload = message['payload']
        

        print('---------',message_payload)


device = frida.get_usb_device()


#pid = device.spawn(["com.test.myapplication"])

#device.resume(pid)

time.sleep(1)  # Without it Java.perform silently fails

session = device.attach(sys.argv[1])

script = session.create_script(open(sys.argv[2]).read())

script.on('message', on_message)

script.load()


t=sys.stdin.read()
