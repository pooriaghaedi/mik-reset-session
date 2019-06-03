import paramiko
import socket
import re
import time as ti
import os

# SSH connection to MikroTik using paramiko

class Mikssh():
    mikroitkip =  os.getenv('MikIP')
    username = os.getenv('MikUsername')
    passwd = os.getenv('MikPassword')

    def connect(self):
        try:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(hostname=self.mikroitkip, username=self.username, password=self.passwd, timeout=10)
            remote = self.ssh.invoke_shell()
            print("connected")
            return (remote)
        except paramiko.AuthenticationException:
            print("Authentication failed when connecting to Router")
        except Exception as e:
            print(e)

    def send_command(self, command):
        try:
            stdin, stdout, stderr = self.ssh.exec_command(command + "\n")
            output = stdout.read()
            output = (str(output))
            return output
        except Exception as e:
            print(e)
