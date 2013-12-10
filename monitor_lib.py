#!/usr/bin/python

import os
import sys
import time
import socket
import re
import socket
import fcntl
import struct
import subprocess


def f_cpu():
    arr = {}

    f_stat = open("/proc/stat", "r")
    # proc.stat
    f_stat.seek(0)
    ts = int(time.time())
    for line in f_stat:
        m = re.match("(\w+)\s+(.*)", line)
        if not m:
            continue
        if m.group(1) == "cpu":
            fields = m.group(2).split()
            arr["proc.cpu.user"] =  fields[0];
            arr["proc.cpu.nice"] =  fields[1];
            arr["proc.cpu.system"] =  fields[2];
            arr["proc.cpu.idle"] =  fields[3];
            arr["proc.cpu.iowait"] =  fields[4];
            arr["proc.cpu.irq"] =  fields[5];
            arr["proc.cpu.softirq"] =  fields[6];

    return arr


def f_meminfo():
    # proc.meminfo

    arr = {}
    f_meminfo = open("/proc/meminfo", "r")
    f_meminfo.seek(0)
    ts = int(time.time())
    for line in f_meminfo:
        m = re.match("(\w+):\s+(\d+)", line)
        if m:
            key = "proc.meminfo.%s" % m.group(1).lower()
            arr[key] = m.group(2)
    return arr

def f_diskinfo():
    # 1kblocks
    arr = {}

    df_proc = subprocess.Popen(["df", "-PlTk"], stdout=subprocess.PIPE)
    stdout, _ = df_proc.communicate()
    if df_proc.returncode == 0:
        for line in stdout.split("\n"): # pylint: disable=E1103
            fields = line.split()
            # skip header/blank lines
            if not line or not fields[2].isdigit():
                continue
            # Skip mounts/types we don't care about.
            # Most of this stuff is of type tmpfs, but we don't
            # want to blacklist all tmpfs since sometimes it's
            # used for active filesystems (/var/run, /tmp)
            # that we do want to track.
            if fields[1] in ("debugfs", "devtmpfs"):
                continue
            if fields[6] == "/dev":
                continue
            # /dev/shm, /lib/init_rw, /lib/modules, etc
            #if fields[6].startswith(("/lib/", "/dev/")):  # python2.5+
            if fields[6].startswith("/lib/"):
                continue
            if fields[6].startswith("/dev/"):
                continue

            mount = fields[6]

            arr[mount] = {}
            arr[mount]["df.1kblocks.total"] = fields[2]; 
            arr[mount]["df.1kblocks.used"] = fields[3]; 
            arr[mount]["df.1kblocks.free"] = fields[4]; 

    return arr


def get_ip_address():
    return socket.gethostbyname(socket.gethostname())

def main():
    print f_cpu()
    print f_meminfo()
    print f_diskinfo()

if __name__ == "__main__":
    main()
