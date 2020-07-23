
import ipaddress
import sys
import subprocess
import platform
from art import *


def rangeIp(a, b):
    start_ip = ipaddress.IPv4Address(a)
    end_ip = ipaddress.IPv4Address(b)
    arr = []
    for ip_int in range(int(start_ip), int(end_ip)):
        currIp = ipaddress.IPv4Address(ip_int)
        arr.append(currIp)
    return arr


def ping_ip(current_ip_address):
    try:
        output = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower(
        ) == "windows" else 'c', current_ip_address), shell=True, universal_newlines=True)
        if 'unreachable' in output:
            return False
        else:
            return True
    except Exception:
        return False


if __name__ == '__main__':
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
        start = sys.argv[1]
        end = sys.argv[2]

    current_ip_address = rangeIp(start, end)
    for each in current_ip_address:
        if ping_ip(each):
            print(f"{each} is [up]")
        else:
            print(f"{each} is [down]")
