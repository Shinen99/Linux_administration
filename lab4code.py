import threading
from os import fork, waitpid
from argparse import ArgumentParser

mutex = threading.Lock()

def fprocess(message, process_number, itter_number):
    pid = None
    for i in range(process_number):
        pid = fork()
        if pid == 0:
            for j in range((i+1)*itter_number):
                with mutex:
                    with open("log.txt", 'a') as logf:
                        logf.write(f"Itteration {j+1}: {message}\n")
    if pid != 0:
        p, _ = waitpid(-1, 0)
        while p:
            try:
                p, _ = waitpid(-1, 0)
            except ChildProcessError:
                return

argp = ArgumentParser()

argp.add_argument('-m', '--message', type=str, required=True)

argp.add_argument('-pn', '--process_number', type=int, required=True)

argp.add_argument('-in', '--itter_number', type=int, required=True)

args = argp.parse_args()

f = open("log.txt", 'w')
f.close()

fprocess(args.message, args.process_number, args.itter_number)