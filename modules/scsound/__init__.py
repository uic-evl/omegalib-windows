from omega import *

# startup command to launch the supercollider server
# by default use scserver.scd for sound generation
# but let users choose a custom script if they want.
def start(scscript = "scsound/scserver.scd"):
    print("Launching the SuperCollider Sound Server...")
    scpath = ofindFile("scsound/scserver.bat")
    scspath = ofindFile(scscript)
    print("executing " + scpath)
    olaunch(scpath + " " + scspath)

# On termination, launch a script that shuts down the sc server
def shutdown():
    scstop = ofindFile("scsound/scstop.bat")
    olaunch(scstop)

import atexit
atexit.register(shutdown)
