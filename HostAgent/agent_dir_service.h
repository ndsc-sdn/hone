/* Copyright (c) 2011-2013 Peng Sun. All rights reserved.
 * Use of this source code is governed by a BSD-style license that can be
 * found in the COPYRIGHT file.
 *
 * agent_dir_service.h
 * author: Peng Sun
 * header for the C implementation of directory service
 */

#ifndef _AGENT_DIR_SERVICE_H_
#define _AGENT_DIR_SERVICE_H_
#define IPQUAD(addr) \
    ((unsigned char *)&addr)[0], \
    ((unsigned char *)&addr)[1], \
    ((unsigned char *)&addr)[2], \
    ((unsigned char *)&addr)[3]

#include <asm/types.h>
#include <sys/socket.h>
#include <linux/netlink.h>
#include <netinet/in.h>
#include <stdio.h>
#include <arpa/inet.h>
#include <string.h>
#include <stdlib.h>
#include <errno.h>
#include <unistd.h>
#include "kpsimple/kpsimple.h"
    
#define NETLINK_HONE 30
#define NL_SIZE 256
#define MESSAGE_SIZE 1024

void agent_dir_service_cleanup(void);

void agent_dir_service_run(void);

char* agent_dir_service_recv(void);

#endif
