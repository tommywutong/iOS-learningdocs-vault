---
title: PGPuam
apple_id: DTS10000259
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/PGPuam/Listings/sources_PPCGlue_c.html
archived_at: '2026-07-18T03:18:32.959603Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PGPuam](PGPuam.md)


[Next](sources-RemoveServerKey.c.md)[Previous](sources-PGPUAMmsgFormat.h.md)

# sources/PPCGlue.c

```
/*
    File:       PPCGlue.c

    Contains:   Glue necessary to call AppendDialogItemList.

    Version:    Appearance 1.0 SDK

    Copyright:  © 1997 by Apple Computer, Inc., all rights reserved.

    File Ownership:

        DRI:                Edward Voas

        Other Contact:      7 of 9, Borg Collective

        Technology:         OS Technologies Group

    Writers:

        (edv)   Ed Voas

    Change History (most recent first):

         <1>     9/11/97    edv     First checked in.
*/


#define RESULT_OFFSET(type) ((sizeof(type) == 1) ? 3 : ((sizeof(type) == 2) ? 1 : 0))

pascal OSErr
AppendDialogItemList( DialogPtr dialog, SInt16 ditlID, DITLMethod method );

pascal OSErr
AppendDialogItemList( DialogPtr dialog, SInt16 ditlID, DITLMethod method )
{
    long    private_result;

    private_result = CallUniversalProc((UniversalProcPtr)GetToolTrapAddress(0xAA68),
        kD0DispatchedPascalStackBased
         | RESULT_SIZE(SIZE_CODE(sizeof(OSErr)))
         | DISPATCHED_STACK_ROUTINE_SELECTOR_SIZE(kTwoByteCode)
         | DISPATCHED_STACK_ROUTINE_PARAMETER(1, SIZE_CODE(sizeof(dialog)))
         | DISPATCHED_STACK_ROUTINE_PARAMETER(2, SIZE_CODE(sizeof(ditlID)))
         | DISPATCHED_STACK_ROUTINE_PARAMETER(3, SIZE_CODE(sizeof(method))),
        0x0412,
        dialog,
        ditlID,
        method );

    return *(((OSErr*)&private_result) + RESULT_OFFSET(OSErr));
}
```

[Next](sources-RemoveServerKey.c.md)[Previous](sources-PGPUAMmsgFormat.h.md)

