import sys
import numpy as np
sys.path.append('zmqRemoteApi')
import math
import time
from zmqRemoteApi import RemoteAPIClient



print ('Program started')
# connect to the coppelia scene
client = RemoteAPIClient()
if client != -1:
    print ('Connected to remote API server')
else:
    print ('Failed connecting to remote API server')
    sys.exit('Could not connect to Coppelia')
sim = client.getObject('sim')
sim.startSimulation()
sim.stopSimulation()

print ('Program ended')

