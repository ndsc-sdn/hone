"""
Author: Peng Sun
hone_run.py
Run hone system
usage: python hone_run.py mgmtprog
"""

import logging
import sys

import hone_rts
from hone_util import LogUtil

def main():
    if len(sys.argv) < 2:
        print "Please provide management program"
        sys.exit()
    # initialize logging
    LogUtil.InitLogging()
    # organize the management programs
    mgmtProg = [hone_rts.HoneHostInfoJob] + sys.argv[1:]
    logging.info('Controller starts with the following programs: %s', mgmtProg)
    LogUtil.DebugLog('global', 'mgmt programs {0}'.format(mgmtProg))
    try:
        print 'HONE controller starts.'
        LogUtil.EvalLog(1, 'controller starts')
        hone_rts.RtsRun(mgmtProg)
    except KeyboardInterrupt:
        LogUtil.DebugLog('global', 'catch keyboard interrupt')
    finally:
        LogUtil.EvalLog(2, 'controller stops')
        logging.info('Controller stops')
        print 'HONE controller stops.'

if __name__ == '__main__':
    main()
