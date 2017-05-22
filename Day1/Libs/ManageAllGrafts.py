import Architectures
from ManageSysgraft import ManageSysgraft

class ManageAllGrafts(object):
    """
    A class that manages a set of grafts
    """
    def __init__(self):
        """
        Setup anything that you need for the class in here
        """
        # TODO
        pass

    def add_graft(self, addr, port, architecture=Architectures.X64):
        """
        Add and instantiate a new graft, return an int the caller can use
        to reference their new graft (I'm calling it an index)

        :param str addr: The network address of the new graft
        :param int port: The port of the new graft
        :param Architecture architecture: The architecture of the target
        :returns int: The new graft's index
        """
        # TODO
        pass

    def del_graft(self, index):
        """
        Remove and close a graft by index
        :returns None:
        """
        # TODO
        pass

    def list_grafts(self):
        """
        :returns list: A list of (index, addr, port) tuples
        """
        # TODO
        pass

    def command_graft(self, index, command):
        """
        Send a command to a graft, store it for the caller to retrieve later
        :param int index:
        :param str command: The command to send to the graft
        :returns None:
        """
        # TODO
        pass

    def list_graft_responses(self, index):
        """
        Return the responses for a graft (by index)
        :return list: A list of objects pairing commands and responses
        """
        # TODO
        pass

    def close(self):
        """
        Delete all grafts, closing all of them
        :returns None:
        """
        # TODO
        pass
