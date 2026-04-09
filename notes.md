# Week 01 — Port Scanner

## What I worked on
Found a tutorial I can look at to learn how port scanners work.

## What I understood
I understood how socket objects are made and how the port scanner works.

## What confused me
One of the functions that is meant to allow multiple ports. Not too sure how that function can be fixed but I am working on it.

## What I changed or added
Nothing yet — reading and understanding first

## What I want to figure out next
How to get the program to run
the current error message: 
usage: portScanner.py [-h] target start_port end_port
portScanner.py: error: the following arguments are required: target, start_port, end_port

Update - I know why it shows this error message. It is because the idle does not take arguments.

## Time spent
20min

### What does the code do in plain English
The port scanner checks for weak points in the network.

### What library is it using to connect to ports
socket

### What happens when a port is open — what does the code do
It prints a message saying which port number is open

### What happens when a port is closed — what does the code do
It prints a message saying which port number is closed

### Is there any part you genuinely don't understand — write the exact line
Lines 23 to 27

## Interesting finding
Port 80 and port 21 came back open on my scan.
Port 80 = web server running
Port 21 = FTP enabled — insecure protocol, sends data in plain text
