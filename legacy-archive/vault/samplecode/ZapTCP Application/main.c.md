---
title: ZapTCP Application
apple_id: DTS10000272
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ZapTCP_Application/Listings/main_c.html
archived_at: '2026-07-18T03:28:35.073437Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ZapTCP Application](ZapTCP%20Application.md)


[Next](zaptcp.c.md)[Previous](ZapTCP%20Application.md)

# main.c

```c
/*-----------------------------------------------------------------

    ZapTCP application patch sample

    Steve Falkeburg MacDTS 6/29/93
    written in Think C 6.0

  -----------------------------------------------------------------*/

#ifndef __TYPES__
#include <Types.h>
#endif

#ifndef __DEVICES__
#include <Devices.h>
#endif

#ifndef __MEMORY__
#include <Memory.h>
#endif

#include <MacTCPCommonTypes.h>
#include <TCPPB.h>
#include "zaptcp.h"

void OpenTCPStuff(void);

void main(void)
{
    InstallZapTCP();    // patch _ExitToShell
    OpenTCPStuff();     // open a stream
    ExitToShell();      // exit, causing the patch to be called and the stream closed
}


// opens up a stream and doesn't close it, so our patch to _ExitToShell
// will notice that there's a connection open and will close it when the app
// exits.

void OpenTCPStuff(void)
{
    short drvrRefNum;
    OSErr err;
    TCPiopb pBlock;
    Ptr rcvBuff;

    err = OpenDriver("\p.ipp",&drvrRefNum);
    if (err!=noErr)
        return;

    rcvBuff = NewPtr(8192);
    if (MemError()!=noErr)
        return;

    pBlock.csCode = TCPCreate;
    pBlock.ioCRefNum = drvrRefNum;
    pBlock.csParam.create.rcvBuff = rcvBuff;
    pBlock.csParam.create.rcvBuffLen = 8192;
    pBlock.csParam.create.notifyProc = nil;
    err = PBControl((ParmBlkPtr)&pBlock,false);
    if (err!=noErr)
        return;
}
```

[Next](zaptcp.c.md)[Previous](ZapTCP%20Application.md)

