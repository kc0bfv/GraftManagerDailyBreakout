# Graft Manager Daily Project Breakout

## Description
This GIT repo contains the project for each day of the Python 2 course.  Each day has a folder, each folder has a readme describing that day's project.  It's that simple!

## Project Overview
During this Python course you will construct a "graft" manager.  This manager will provide an interface that allows users to dispatch shellcode to "grafts" executing on remote computers and listening at known IP addresses and ports.  Until the last day you'll be creating a command line interface for this graft manager.  The last day's project will see you create a web interface to the manager.

## Project Use Case
You will deploy a stage 0 to their target.  In your testing, you will simply copy this onto a Kali VM.

You will start the stage 0 on the target.  In testing, you'll execute the file you copied over to Kali.

Outside of Kali, you will execute the manager program.

You will provide the manager program with the IP address and port of the stage 0.

The manager program will automatically connect to the stage 0 and send it shellcode.  The shellcode will execute and start a shell listening over the same connection.

You will tell the manager to execute commands on the target.  The manager will send the commands over TCP, then receive responses from the target.

You will ask the manager to list the responses it has received.

## CLI Block Diagram
https://docs.google.com/presentation/d/1Anu_wvHLz2FqKmgfApmzXvcL3ICeXOBm9WTINRbjBBs/edit?usp=sharing

## Reference Code
https://github.com/kc0bfv/GraftManagerReference
