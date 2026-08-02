---
title: SCSI Async Sample
apple_id: DTS10000022
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/SCSI_Async_Sample/Listings/Src_DisplayTestParameters_c.html
archived_at: '2026-07-18T03:22:30.376355Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SCSI Async Sample](SCSI%20Async%20Sample.md)


[Next](Src-DisplayTestResults.c.md)[Previous](Src-DialogUtilities.h.md)

# Src/DisplayTestParameters.c

```c
/*                              DisplayTestParameters.c                         */
/*
 * DisplayTestParameters.c
 * Copyright © 93 Apple Computer Inc. All Rights Reserved.
 *
 * Run the dialog until the user has had enough.
 */
#include "SCSIAsyncSample.h"
#include "SCSIDefinitions.h"
#include <math.h>
#define ALWAYS      1
#define NEVER       1
#define INFO        (*infoPtr)

void
DisplayOneParameter(
        register InfoPtr                infoPtr
    );


void
DisplayTestParameters(void)
{
        InfoPtr                         currentInfoPtr;

        if (infoPtrQueue.qHead == NULL)
            DisplayLogString(gLogListHandle, "\pNo devices to test");
        for (currentInfoPtr = (InfoPtr) infoPtrQueue.qHead;
                currentInfoPtr != NULL;
                currentInfoPtr = (InfoPtr) currentInfoPtr->link) {
            DisplayOneParameter(currentInfoPtr);
        }
}

void
DisplayOneParameter(
        register InfoPtr                infoPtr
    )
{
        Str255                          work;

        DisplayDeviceInfo(infoPtr);
        if (INFO.validDevice) {
            work[0] = 0;
            AppendPascalString(work, "\p Buffer Length: ");
            AppendUnsigned(work, INFO.bufferLength);
            DisplayLogString(gLogListHandle, work);
            /* */
            work[0] = 0;
            AppendPascalString(work, "\p Transfer Quantum: ");
            AppendUnsigned(work, INFO.transferQuantum);
            switch (INFO.transferQuantum) {
            case 0:     AppendPascalString(work, "\p (normal)");        break;
            case 1:     AppendPascalString(work, "\p (polled)");        break;
            default:    AppendPascalString(work, "\p (blocked)");       break;
            }
            DisplayLogString(gLogListHandle, work);
            /* */
            work[0] = 0;
            AppendPascalString(work, "\p Transfer Size: ");
            AppendUnsigned(work, INFO.transferSizeBlocks);
            AppendPascalString(work, "\p (blocks)");
            DisplayLogString(gLogListHandle, work);
            /* */
            work[0] = 0;
            if (INFO.totalTransfers == 0)
                AppendPascalString(work, "\p Unlimited transfers");
            else if (INFO.totalTransfers == 1)
                AppendPascalString(work, "\p One transfer only");
            else {
                AppendPascalString(work, "\p Stop after ");
                AppendUnsigned(work, INFO.totalTransfers);
                AppendPascalString(work, "\p transfers");
            }
            DisplayLogString(gLogListHandle, work);
            /* */
            work[0] = 0;
            AppendPascalString(work, "\p Asychronous transfers ");
            AppendPascalString(work, (INFO.enableAsync) ? "\penabled" : "\pdisabled");
            DisplayLogString(gLogListHandle, work);
            /* */
            work[0] = 0;
            AppendPascalString(work, "\p Disconnect ");
            AppendPascalString(work, (INFO.enableDisconnect) ? "\penabled" : "\pdisabled");
            DisplayLogString(gLogListHandle, work);
            /* */
            work[0] = 0;
            DisplayLogString(gLogListHandle, (INFO.enableRandomSeek)
                    ? "\p Random Seek"
                    : "\p Sequential Read"
                );
        }
}

void
DisplayDeviceInfo(
        register InfoPtr                infoPtr
    )
{
        Str255                          work;

        pstrcpy(work, "\p¥ÊThread: ");
        AppendUnsigned(work, INFO.threadIndex);
        if (INFO.validDevice == FALSE) {
            AppendPascalString(work, "\p - Invalid Device");
            DisplayLogString(gLogListHandle, work);
        }
        else {
            AppendPascalString(work, "\p: ");
            AppendSCSIBusID(work, INFO.deviceIdent);
            AppendPascalString(work, "\p Ò");
            AppendPascalString(work, (StringPtr) INFO.vendor);
            AppendPascalString(work, "\p, ");
            AppendPascalString(work, (StringPtr) INFO.product);
            AppendPascalString(work, "\pÓ");
            DisplayLogString(gLogListHandle, work);
        }
}

void
AppendSCSIBusID(
        StringPtr           result,
        DeviceIdent         deviceIdent
    )
{

        AppendPascalString(result, "\pBus ID: ");
        AppendUnsigned(result, deviceIdent.bus);
        AppendChar(result, '.');
        AppendUnsigned(result, deviceIdent.targetID);
}
```

[Next](Src-DisplayTestResults.c.md)[Previous](Src-DialogUtilities.h.md)

