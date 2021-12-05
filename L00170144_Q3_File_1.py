import paramiko
import time
import re
# Open SSH connection to the device
def ssh_connection(ip):
    try:
        username = "lyitmickd"
        password = "lyitMickD"
        print("Establishing a connection...")
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip.rstrip("\n"), username=username, password=password)
        connection = session.invoke_shell()
        connection.send("ls > dir_contents.txt\n") #unix command to list
        # directory contents and save to file
        time.sleep(1)
        vm_output = connection.recv(65535)
        if re.search(b"% Invalid input", vm_output):
            print("There was an error on vm {}".format(ip))
        else:
            print("Commands successfully executed on {}".format(ip))
            session.close()
    except paramiko.AuthenticationException:
        print("Authentication Error")
        
if __name__ == "__main__":
    ssh_connection("192.168.0.38")