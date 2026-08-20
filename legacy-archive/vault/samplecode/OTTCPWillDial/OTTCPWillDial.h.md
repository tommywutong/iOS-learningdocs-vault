---
title: OTTCPWillDial
apple_id: DTS10000256
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/OTTCPWillDial/Listings/OTTCPWillDial_h.html
archived_at: '2026-07-18T03:17:26.170192Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OTTCPWillDial](OTTCPWillDial.md)


[Next](TestOTTCPWillDial.c.md)[Previous](OTTCPWillDial.c.md)

# OTTCPWillDial.h

```objc
/*
    File:       OTTCPWillDial.h

    Contains:   Library to determine whether open a TCP endpoint will
                dial the modem.

    Written by: Quinn "The Eskimo!"

    Copyright:  © 1998 by Apple Computer, Inc., all rights reserved.

    Change History (most recent first):

    You may incorporate this sample code into your applications without
    restriction, though the sample code has been provided "AS IS" and the
    responsibility for its operation is 100% yours.  However, what you are
    not permitted to do is to redistribute the source as "DSC Sample Code"
    after having made changes. If you're going to re-distribute the source,
    we require that you make it clear in the source that the code was
    descended from Apple Sample Code, but that you've made changes.
*/

/////////////////////////////////////////////////////////////////

#import "Types.h"

/////////////////////////////////////////////////////////////////

enum {
    kOTTCPDialUnknown = 0,
    kOTTCPDialTCPDisabled,
    kOTTCPDialYes,
    kOTTCPDialNo
};

extern OSStatus OTTCPWillDial(UInt32 *willDial);
    // This routine returns, in willDial, a flag indicating
    // whether opening a TCP/IP provider will cause the modem 
    // to dial.  You must call InitOpenTransport before calling
    // this routine.
```

[Next](TestOTTCPWillDial.c.md)[Previous](OTTCPWillDial.c.md)

