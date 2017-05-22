from Architectures import X64

class ManageSysgraft(object):
    def __init__(self, addr, port, architecture=X64):
        """
        Connect to a remote host and upload shellcode to start a Graft

        :param string addr: The remote host's address or hostname
        :param int port: The port to connect to
        :param Architecture architecture:
            An object with an attribute named "shell"
            More specifically, a shell attribute containing shellcode for
            the target
        """
        # Do anything necessary for the class
        # TODO

        # Connect to the remote host
        # TODO

        # Send it the shellcode necessary to run a shell over the connection
        # TODO
        pass

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

        :param string command: The command to send
        :param int recv_timeout:
            The amount of time to wait after last output before considering
            output finished
        :param bool add_newline:
            If true, add a newline if command doesn't end in one

        :returns string: The command output
        """
        # TODO
        pass

    def close_graft(self, wait_for_command_completion=True):
        """
        Close the Graft nicely
        :param bool wait_for_command_completion:
            Ensure that any running command completes before closing
        """
        # TODO
        pass
