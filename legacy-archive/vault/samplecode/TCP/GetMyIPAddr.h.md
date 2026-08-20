---
title: TCP
apple_id: DTS10000263
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/TCP/Listings/GetMyIPAddr_h.html
archived_at: '2026-07-18T03:25:58.884557Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TCP](TCP.md)


[Next](MacTCPCommonTypes.h.md)[Previous](dnr.c.md)

# GetMyIPAddr.h

```
/* 
    GetMyIPAddr.h   
    C definitions of parameter block entries needed for IP calls

    Copyright Apple Computer, Inc. 1989 
    All rights reserved

*/

#define ipctlGetAddr        15          /* csCode to get our IP address */

#define ParamBlockHeader    \
    struct QElem *qLink;    \
    short qType;            \
    short ioTrap;           \
    Ptr ioCmdAddr;          \
    ProcPtr ioCompletion;   \
    OSErr ioResult;         \
    StringPtr ioNamePtr;    \
    short ioVRefNum;        \
    short ioCRefNum;        \
    short csCode

struct IPParamBlock {
    ParamBlockHeader;           /* standard I/O header */
    ip_addr ourAddress;         /* our IP address */
    long    ourNetMask;         /* our IP net mask */
    };
```

[Next](MacTCPCommonTypes.h.md)[Previous](dnr.c.md)

