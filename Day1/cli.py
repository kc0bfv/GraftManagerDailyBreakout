#!/usr/bin/env python

"""
This is terrible, but it should get you started
"""

from Libs.ManageAllGrafts import ManageAllGrafts

def mainloop():
    manager = ManageAllGrafts()

    while True:
        addr = raw_input("Where do you want to connect? ")
        port = int(raw_input("What port? "))
        ind = manager.add_graft(addr, port)
        cmd = raw_input("What command? ")
        manager.command_graft(ind, cmd)
        print manager.list_graft_responses(ind)
        cmd = raw_input("Ok, gimme another: ")
        manager.command_graft(ind, cmd)
        print manager.list_graft_responses(ind)
        cmd = raw_input("Ok, one more: ")
        manager.command_graft(ind, cmd)
        print manager.list_graft_responses(ind)
        print manager.list_grafts()

if __name__ == "__main__":
    mainloop()
