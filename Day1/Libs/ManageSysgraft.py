import time

from Architectures import X64

class ManageSysgraft(object):
    def __init__(self, addr, port, architecture=X64):
        """
        Connect to a remote host and upload shellcode to start a Graft

        :param string addr: The remote host's address or hostname
        :param int port: The port to connect to
        :param Architecture architecture:
            An object with a shell attribute
            More specifically, a shell attribute containing shellcode for
            the target
        """
        self.architecture = architecture
        self.addr = addr
        self.port = port
        self.num_commands = 0
        
        outputs = ["deet", "doot", "doot", "doot", "deet", "deet", "doot",
                "PSSSSHSHHSHHS", "BRRRRRRARARAR", "WHRRRRRRR", "BA-DUNG",
                "BA-DUNG", "You've got mail. (you're fake-connected now)"]

        for output in outputs:
            time.sleep(1)
            print(output)

    def __str__(self):
        """
        Returns a representation of the object as a string
        Used, for instance, by the logger
        """
        return "Graft {} {} {}".format(self.addr, self.port,
                self.architecture.__name__)

    def send_command(self, command, recv_timeout=4, add_newline=True):
        """
        Send a command to the Graft, return the output received.
        Only one command may run at a time.  This will block until it can run.

        :param string command: The command to send
        :param int recv_timeout:
            The amount of time to wait after last output before considering
            output finished
        :param bool add_newline:
            If true, add a newline if command doesn't end in one

        :returns string: The command output
        """
        response = "root@127.0.0.1> this is a response to command "\
                "#{} - {}.  Normally actual program output "\
                "would be here.".format(self.num_commands, command)
        self.num_commands += 1
        return response

    def close_graft(self, wait_for_command_completion=True):
        """
        Close the Graft nicely
        :param bool wait_for_command_completion:
            Ensure that any running command completes before closing
        """
        print("I'M MEELLLLLLLLTINNNNNGG!")
