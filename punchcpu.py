import dis
import os
import sys
import re
from time import sleep
from multiprocessing import Process
from subprocess import check_output as run

EMPFY_MAP = { 
    '50':1, 
    '60':1.5, 
    '65':1.8, 
    '70':2.2, 
    '75':3, 
    '80':4, 
    '85':6, 
    '90':9, 
    '95':18 
}

def getcpuinfo():
    """
    this function will analysis /proc/cpuinfo to ge expected fileds
    :return (hertz, cores): a tuple continas Hertz and number of cores
    """
    cv = None
    hv = None
    if os.name == 'posix':
        with open('/proc/cpuinfo', 'r') as fo:
            cpuinfo = fo.read()
            cv = re.search('cpu cores\t+: (\S+)', cpuinfo)
            hv = re.search('cpu MHz\t+: (\S+)\.\d+', cpuinfo)
    elif os.name == 'nt':
        cpuinfo = run(['WMIC', 'CPU', 'Get', '/Format:List'])
        cv = re.search('NumberOfCores=(\S+)', cpuinfo)
        hv = re.search('CurrentClockSpeed=(\S+)', cpuinfo)
    else:
       sys.exit("Unsupported OS!")

    print("CPU MHz: %s" %  hv.group(1))
    print("CPU cores: %s" %  cv.group(1))
    return (hv.group(1), cv.group(1))

def doticks(percent='70', hz=2500):
    """ doticks
    For example:
    2.5GHz CPU will excute 2.5 * 10^9 CPU clocks per second
    modern CPU executes 2 instructions per clocks, hence
    there will be 5000,000,000 instructinos be executed
    per second roughly, so 1,000,000 instructions consume
    one 10ms.
    """
    clockspersec = int(hz) * 1000 * 1000
    instructspersec = (clockspersec * 2) / 50 # fifty-two instructions per iteration of 'xrange()'
    instructsper10ms = instructspersec / 100
    instructsper10msempfy =instructsper10ms * int(EMPFY_MAP[percent])
    print("CPU clocks per second: %d" % clockspersec)
    print("number of instructions per 10ms: %d" % instructsper10msempfy)
    while True:
        for i in xrange(int(instructsper10msempfy)):
            pass
        sleep(0.01)  # sleep 10ms


# issue mulitple processes for multi-core scheduling
def takeplaceonmulticores(percentage=70, hertz=2.5, cores=12):
    for x in range(int(cores)):
        p = Process(target=doticks, kwargs={ 'percent' : percentage, 'hz' : hertz })
        p.start()
        print("started process on core %d ... \n" % x)

if __name__ == '__main__':
    arglen = len(sys.argv)
    cpuhertz, numcore = getcpuinfo()
    cpucores = numcore
    cpuusage = '50'
    if arglen == 3:
        cpuusage = sys.argv[1]
        cpucores = sys.argv[2]
    elif arglen == 2:
        cpuusage = sys.argv[1]

    if cpuusage not in EMPFY_MAP.keys():
        print("invalid CPU percentage")
        sys.exit(299)

    print ("CPU USAGE: %s" % cpuusage)
    print ("CPU CORES: %s" % cpucores)

    takeplaceonmulticores(cpuusage, cpuhertz, cpucores)


