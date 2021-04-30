from paramiko import client

class SSH:

    client = None

    def __init__(self, address, username, password):
        print("Login info sent.")
        print("Connecting to server.")
        self.client = client.SSHClient()    # Create a new SSH client
        self.client.set_missing_host_key_policy(client.AutoAddPolicy())
        self.client.connect(
            address, username=username, password=password, look_for_keys=False) # connect

    def sendCommand(self, command):
        print("Sending your command")
        # Check if connection is made previously
        if (self.client):
            stdin, stdout, stderr = self.client.exec_command(command)
            while not stdout.channel.exit_status_ready():
                # Print stdout data when available
                if stdout.channel.recv_ready():
                    # Retrieve the first 1024 bytes
                    alldata = stdout.channel.recv(1024)
                    while stdout.channel.recv_ready():
                        # Retrieve the next 1024 bytes
                        alldata += stdout.channel.recv(1024)


                    # Print as string with utf8 encoding
                    print(str(alldata, "utf8"))
        else:
            print("Connection not opened.")