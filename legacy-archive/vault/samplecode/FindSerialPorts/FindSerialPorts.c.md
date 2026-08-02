---
title: FindSerialPorts
apple_id: DTS10000001
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-15'
source_url: https://developer.apple.com/library/archive/samplecode/FindSerialPorts/Listings/FindSerialPorts_c.html
archived_at: '2026-07-18T03:08:41.380375Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [FindSerialPorts](FindSerialPorts.md)


[Next](Document%20Revision%20History.md)[Previous](FindSerialPorts.md)

# FindSerialPorts.c

```c
/*
    File:       FindSerialPorts.c

    Description:
                This is a little snippet from the "Inside the Macintosh 
                Communications Toolbox" which demonstrates the correct 
                method for detecting which serial ports are present.


    Author:     BB

    Copyright:  Copyright: © 1999 by Apple Computer, Inc.
                all rights reserved.

    Disclaimer: You may incorporate this sample code into your applications without
                restriction, though the sample code has been provided "AS IS" and the
                responsibility for its operation is 100% yours.  However, what you are
                not permitted to do is to redistribute the source as "DSC Sample Code"
                after having made changes. If you're going to re-distribute the source,
                we require that you make it clear in the source that the code was
                descended from Apple Sample Code, but that you've made changes.

    Change History (most recent first):
        6/22/99 - updated for Metrowerks Codewarrior Pro 2.1(KMG)
        2/17/97 - recompiled in Metrowerks Codewarrior 11(BB)  


*/
#include <CommResources.h>
#include <CRMSerialDevices.h>

#include <stdio.h>

void main(void)
{
    CRMRec      c;
    CRMRecPtr   cPtr = &c;
    CRMSerialPtr    serialPtr;

    printf("Listing of available serial ports\n");
    InitCRM();

    c.crmDeviceType = crmSerialDevice;
    c.crmDeviceID   = 0;
    while (cPtr != nil) {
        cPtr = (CRMRecPtr)CRMSearch((CRMRecPtr)cPtr);
        if (cPtr) {
            serialPtr = (CRMSerialPtr)cPtr->crmAttributes;
            printf("We have a port called: %#s\n", *(serialPtr->name));
            printf("   input driver named: %#s\n", *(serialPtr->inputDriverName));
            printf("  output driver named: %#s\n\n", *(serialPtr->outputDriverName));
            c.crmDeviceID = cPtr->crmDeviceID;
        }
    }
}
```

[Next](Document%20Revision%20History.md)[Previous](FindSerialPorts.md)

