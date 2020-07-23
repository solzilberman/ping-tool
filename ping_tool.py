
import ipaddress
import sys
import subprocess
import platform
from art import *
import multiprocessing.dummy
import multiprocessing
import os


def rangeIp(a, b):
    start_ip = ipaddress.IPv4Address(a)
    end_ip = ipaddress.IPv4Address(b)
    arr = []
    for ip_int in range(int(start_ip), int(end_ip)):
        currIp = ipaddress.IPv4Address(ip_int)
        arr.append(str(currIp))
    return arr


def ping_ip(current_ip_address):
    try:
        output = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower(
        ) == "windows" else 'c', current_ip_address), shell=True, universal_newlines=True)
        if 'unreachable' in output:
            print("TARGET IP [" +
                  str(current_ip_address) + "] is [down]")
            return False

        else:
            print("TARGET IP [" +
                  str(current_ip_address) + "] is [up]")
            return True
    except Exception:
        return False
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)


def ping_range(start, end, rng):
    num_threads = 2 * multiprocessing.cpu_count()
    p = multiprocessing.dummy.Pool(num_threads)
    try:
        p.map(ping_ip, rng)
    except KeyboardInterrupt:
        print('Interrupted')
        p.terminate()
        sys.exit(0)


if __name__ == '__main__':
    f = []
    for i in range(1000):
        f.append("192.168.1.106")
    helpTrue = False
    Art = text2art("PING-TOOL")
    if(sys.argv[1] == '-h' or sys.argv[1] == '--help'):
        print(Art)
        print("             [--] made by s01")
        print(
            "             [1] Welcome to this network tool. It will scan IP Range defined.")
        print("             [Usage] python ping_tool.py <start_ip> <end_ip>")
        print(
            "             [Ex] python ping_tool.py 192.168.1.1 192.168.1.254")
        print("")
        print("")
        print("")
        helpTrue = True
        sys.exit()
    else:
        print(Art)
        print("             [--] made by s01")
        print("")
        print("")
        print("")
        start = sys.argv[1]
        end = sys.argv[2]
        rng = rangeIp(start, end)
        ping_range(0, 255, rng)
