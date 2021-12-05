import paramiko
import time
import re

# Open SSH connection to the device
# first install ssh-server on the VM
#sudo apt install openssh-server openssh-client
results = []

def ssh_connection(ip):
    """
    """
    try:
        username = "lyitmickd"
        password = "lyitMickD"

        print("Establishing a connection...")
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip.rstrip("\n"), username=username, password=password)
        connection = session.invoke_shell()
        connection.send("ls -al > longList.txt\n") #unix command to list directory contents and save to file
        time.sleep(1)

        #List of command to be executed
        commands = ['mkdir -p Labs/{Lab1,Lab2}', 'sudo apt install curl', 'ls -l --time=atime']
        #loops through the commands
        for command in commands:
            stdin, stdout, stderr = session.exec_command(command)
            time.sleep(.5)
            print(stdout.read().decode())

        vm_output = connection.recv(65535)
        if re.search(b"% Invalid input", vm_output):
            print("There was at least one IOS syntax error on device {}".format(ip))
        else:
            print("Commands successfully executed on {}".format(ip))
        session.close()
    except paramiko.AuthenticationException:
        print("Authentication Error")

if __name__ == "__main__":
    ssh_connection("192.168.0.38")
