import simpy
import random

def wireless_node(env, name, channel):
    for i in range(2): # Try sending 2 packets
        # Wait before sensing
        yield env.timeout(random.randint(1, 4))
        print(f"Time {env.now:.1f}: Node {name} senses channel...")
        
        # CSMA/CA Backoff / Carrier Sense
        if channel.count == 0:
            with channel.request() as req:
                yield req
                print(f"Time {env.now:.1f}: Node {name} acquired channel. Transmitting frame...")
                yield env.timeout(2.0) # Transmission delay
                print(f"Time {env.now:.1f}: Node {name} finished transmission.")
        else:
            backoff = random.randint(3, 7)
            print(f"Time {env.now:.1f}: Node {name} detected busy channel! Backing off for {backoff}s...")
            yield env.timeout(backoff)

env = simpy.Environment()
channel = simpy.Resource(env, capacity=1) # Shared wireless medium

for i in range(3):
    env.process(wireless_node(env, f"Station-{i+1}", channel))

env.run(until=20)