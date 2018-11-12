import subprocess


def shutdown(self):
    subprocess.call(["shutdown", "-f", "-s", "-t", "60"])
def restart(self):
    subprocess.call(["Restarting system", "-f", "-r", "-t", "60"])
def logout(self):
    subprocess.call(["Logging Out User", "-f","-l","-t","60"])
def abort(self):
    subprocess.call(["Aborting Shutdown", "-f","-a","-t","60"])


user=input("Tell me ")

if user=='shutdown':
    shutdown(1)
elif user=='restart':
    restart(1)
elif user=='log out':
    logout(1)
elif user=='abort':
    abort(1)
