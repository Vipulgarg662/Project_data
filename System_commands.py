import os


def shutdown(self):
    os.system("shutdown -s")
def restart(self):
    os.system("shutdown -r")
def logout(self):
    os.system("shutdown -l")

user=input("Tell me ")

if user=='shutdown':
    shutdown(1)
elif user=='restart':
    restart(1)
elif user=='log out':
    logout(1)

