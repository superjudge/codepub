import random
import radio
from microbit import accelerometer, Image, display, sleep, button_a

tools = (Image.SKULL, Image.PITCHFORK, Image.PACMAN)

random.seed(463473567345343)
my_id = 'foo'
tool = 0
peers = set()
receives = 0

radio.on()

while True:
    #if accelerometer.was_gesture('shake'):
    if button_a.was_pressed():
        tool = random.randrange(3)
        #display.clear()
        #sleep(1000)
        #display.show(tool)
    
    display.clear()
    display.scroll('%s' % len(peers))
    display.show(tools[tool])

    sleep_time = random.randint(200, 500)
    print('sleep time: %s' % sleep_time)
    
    if receives >= 10:
        print('sending: %s %s' % (my_id, tool))
        radio.send('%s %s' % (my_id, tool))
        receives = 0

    incoming = radio.receive()
    receives += 1
    
    print(incoming)
    
    if incoming:
        (their_id, their_tool) = incoming.split()
        
        if int(their_tool) == tool:
            peers.add(their_id)
        else:
            peers.discard(their_id)

    print(peers)
    
    #print('sleeping...')
    #sleep(sleep_time)
    
    print('sleeping...')
    sleep(sleep_time)
