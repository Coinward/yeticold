import subprocess
import os
import sys

home = sys.argv[1]

file = '[Desktop Entry]\nVersion=1.0\nName=Level Three\nExec=gnome-terminal --  bash -c "python3 '+home+'/yeticold/initialize.py YetiLevelThreePrimary; $SHELL" %F\nTerminal=true\nX-MultipleArgs=false\nType=Application\nIcon='+home+'/yeticold/static/yeti.png\nStartupNotify=true'
subprocess.call('sudo rm /usr/share/applications/YetiLevelThreePrimary.desktop',shell=True)
subprocess.call("sudo echo '"+file+"' >> /usr/share/applications/YetiLevelThreePrimary.desktop", shell=True)
subprocess.call('sudo chmod +x /usr/share/applications/YetiLevelThreePrimary.desktop', shell=True)

file = '[Desktop Entry]\nVersion=1.0\nName=Level Two\nExec=gnome-terminal --  bash -c "python3 '+home+'/yeticold/initialize.py YetiLevelTwo; $SHELL" %F\nTerminal=true\nX-MultipleArgs=false\nType=Application\nIcon='+home+'/yeticold/static/yeti.png\nStartupNotify=true'
subprocess.call('sudo rm /usr/share/applications/YetiLevelTwo.desktop',shell=True)
subprocess.call("sudo echo '"+file+"' >> /usr/share/applications/YetiLevelTwo.desktop", shell=True)
subprocess.call('sudo chmod +x /usr/share/applications/YetiLevelTwo.desktop', shell=True)

file = '[Desktop Entry]\nVersion=1.0\nName=Level One\nExec=gnome-terminal --  bash -c "python3 '+home+'/yeticold/initialize.py YetiLevelOne; $SHELL" %F\nTerminal=true\nX-MultipleArgs=false\nType=Application\nIcon='+home+'/yeticold/static/yeti.png\nStartupNotify=true'
subprocess.call('sudo rm /usr/share/applications/YetiLevelOne.desktop',shell=True)
subprocess.call("sudo echo '"+file+"' >> /usr/share/applications/YetiLevelOne.desktop", shell=True)
subprocess.call('sudo chmod +x /usr/share/applications/YetiLevelOne.desktop', shell=True)