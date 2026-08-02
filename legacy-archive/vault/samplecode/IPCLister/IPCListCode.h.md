---
title: IPCLister
apple_id: DTS10000208
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-14'
source_url: https://developer.apple.com/library/archive/samplecode/IPCLister/Listings/IPCListCode_h.html
archived_at: '2026-07-18T03:12:05.873211Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [IPCLister](IPCLister.md)


[Next](IPCLister.main.c.md)[Previous](IPCListCode.c.md)

# IPCListCode.h

```c
/*
    File:       IPCListCode.h

    Contains:   

    Written by: Jim Luther      

    Copyright:  Copyright © 1992-1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                7/21/1999   Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1


*/
#pragma once
#include <AppleTalk.h>
#include <PPCToolBox.h>

#define MaxTuples  100
#define  MaxPorts  100
typedef unsigned char Tuple[104];

/*
TYPE
Tuple = PACKED ARRAY[1..104] OF Char;
{ an AddrBlock (4 bytes), a one byte enumerator, and an EntityName (99 bytes) }
*/

Tuple myRetBuff[100];                                       /*  myRetBuff: ARRAY[1..MaxTuples] OF Tuple;{for NBP Lookup} */
MPPParamBlock paramblk;                                     /*  paramblk: MPPParamBlock; */
EntityName myEntityName;                                    /* myEntityName: EntityName; */
AddrBlock myAddrBlock;                                      /* myAddrBlock: AddrBlock; */
short i, j;                                                 /* i, j: integer; */
short gCount;                                               /*  gCount: integer; */
PortInfoRec gPortInfoBuffer[100];                           /*  gPortInfoBuffer: ARRAY[1..MaxPorts] OF PortInfoRec; */
XPPParamBlock xppParamblk;                                  /*  xppParamblk: XPPParamBlock; */
Str255 zoneName;                                            /*  zoneName: Str255; */

OSErr gErr;                                                 /*  gErr: OSErr; */

OSErr myIPCListPorts(short theStartIndex, short theRequestCount, short *theActualCount, Str32 theObjStr, Str32 theZoneStr,
                     PortInfoArrayPtr thePortInfoBufferPtr);

OSErr GetAllPPCAbleMachines(MPPParamBlock *paramblk);
OSErr GetPortsOnMachine(MPPParamBlock *paramblk);
```

[Next](IPCLister.main.c.md)[Previous](IPCListCode.c.md)

