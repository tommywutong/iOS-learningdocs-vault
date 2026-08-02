---
title: STD File Saver
apple_id: DTS10000307
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-26'
source_url: https://developer.apple.com/library/archive/samplecode/STD_File_Saver/Listings/Source_StdFileSaver_c.html
archived_at: '2026-07-18T03:22:49.039410Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [STD File Saver](STD%20File%20Saver.md)


[Next](Source-StdFileSaver.r.md)[Previous](Source-StdFileSaver.a.md)

# Source/StdFileSaver.c

```c
/*
** Copyright 1991-1996 Apple Computer. All rights reserved.
**
**  You may incorporate this sample code into your applications without
**  restriction, though the sample code has been provided "AS IS" and the
**  responsibility for its operation is 100% yours.  However, what you are
**  not permitted to do is to redistribute the source as "DSC Sample Code"
**  after having made changes. If you're going to re-distribute the source,
**  we require that you make it clear in the source that the code was
**  descended from Apple Sample Code, but that you've made changes.
*/

#error

// This file is unused, I think

#error

#include <types.h>
#include <Devices.h>

// all functions just say that everything is fine and nothing else 
// see also StdFileSaver.a for an alternate version of the driver 

// a printer driver related to a physical device would of course 
// be more complete than that 

pascal OSErr DRVROpen(ParmBlkPtr ctlPB, DCtlPtr dCtl)
{
#pragma unused(ctlPB)
#pragma unused(dCtl)
    return noErr;
}

pascal OSErr DRVRClose(ParmBlkPtr ctlPB, DCtlPtr dCtl)
{
#pragma unused(ctlPB)
#pragma unused(dCtl)
    return noErr;
}

pascal OSErr DRVRControl(ParmBlkPtr ctlPB, DCtlPtr dCtl)
{
#pragma unused(ctlPB)
#pragma unused(dCtl)
    return noErr;
}

pascal OSErr DRVRPrime(ParmBlkPtr ctlPB, DCtlPtr dCtl)
{
#pragma unused(ctlPB)
#pragma unused(dCtl)
    return noErr;
}

pascal OSErr DRVRStatus(ParmBlkPtr ctlPB, DCtlPtr dCtl)
{
#pragma unused(ctlPB)
#pragma unused(dCtl)
    return noErr;
}
```

[Next](Source-StdFileSaver.r.md)[Previous](Source-StdFileSaver.a.md)

