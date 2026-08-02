---
title: PGPuam
apple_id: DTS10000259
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/PGPuam/Listings/sources_PGPUAMdefines_h.html
archived_at: '2026-07-18T03:18:32.699200Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PGPuam](PGPuam.md)


[Next](sources-PGPUAMDialogTest.c.md)[Previous](sources-PGPUAMclientProtocol.h.md)

# sources/PGPUAMdefines.h

```
/*
    File:           PGPUAMdefines.h

    Description:    per context Globals.

    Written by: Vinnie Moscaritolo

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


#define kPGPuamCreatorSig   'rkba'


#define kErrorStringsID 130 

static enum {
    kErrUnableToAuthErr         =1,
    kErrUnableToAuthExplanation,
    kErrUnableToAuthContinueExplanation,

    kErrClientUnableToAuthErr,
    kErrClientUnableToAuthExplanation,
    kErrOther,
    kErrOtherExplanation
    };
```

[Next](sources-PGPUAMDialogTest.c.md)[Previous](sources-PGPUAMclientProtocol.h.md)

