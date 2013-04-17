'''
HONE application
Author: Peng Sun
Purpose:
debug
'''

from hone_lib import *
from math import *
import time, sys

def cpuMemQuery():
    q = (Select(['app','cpu','memory'])*
         From('AppStatus')*
         Where([('app','==','python2.7')])*
         Every(1))
    return q

def myPrint(x):
    cpuOutput = open('eval_ctrl_cpu.txt','a')
    memOutput = open('eval_ctrl_mem.txt','a')
    (hostID, seq, [app, cpu, mem]) = x
    ct = time.time()
    print >>cpuOutput, str(seq)+' '+str(cpu)+' '+str(ct)
    print >>memOutput, str(seq)+' '+str(mem)+' '+str(ct)
    cpuOutput.close()
    memOutput.close()
    print 'seq:'+str(seq)+',cpu:'+str(cpu)+',mem:'+str(mem)+',time:'+str(ct)

def main():
    return (cpuMemQuery()>>
            MergeHosts()>>
            Print(myPrint))




