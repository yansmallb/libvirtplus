# -*- coding: UTF-8 -*-
import sys
from route import start_server


if __name__ == "__main__":
    if len(sys.argv) < 3 and len(sys.argv) != 1:
        print "libvirtplus: host port"
        exit()

    if len(sys.argv) == 1:
        start_server()
    else:
        start_server(sys.argv[1], sys.argv[2])

