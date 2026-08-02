---
title: Inline Input for TextEdit
apple_id: DTS10001094
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Inline_Input_for_TextEdit/Listings/TSMTE_Interfaces_CIncludes_TSMTE_h.html
archived_at: '2026-07-18T03:12:56.361322Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Inline Input for TextEdit](Inline%20Input%20for%20TextEdit.md)


[Next](TSMTE%20Interfaces-PPCCIncludes-TSMTE.h.md)[Previous](InlineInputSample-InlineInputSample.r.md)

# TSMTE Interfaces/CIncludes/TSMTE.h

```c
/*
    File:       TSMTE.h

    Contains:   Definitions for TSMTE

    Copyright:  ©1991-1993 Apple Technology, Inc.
                All rights reserved.

*/

#ifndef __TSMTE__
#define __TSMTE__

#ifndef __TEXTEDIT__
#include <TextEdit.h>
#endif

#ifndef __DIALOGS__
#include <Dialogs.h>
#endif

#ifndef __TEXTSERVICES__
#include <TextServices.h>
#endif


// signature, interface types

enum {
    kTSMTESignature = 'tmTE',
    kTSMTEInterfaceType = kTSMTESignature,
    kTSMTEDialog = 'tmDI'
};


// Gestalt

enum {
    gestaltTSMTEAttr = kTSMTESignature,
    gestaltTSMTEPresent = 0,
    gestaltTSMTE = gestaltTSMTEPresent, // old name, for compatibility only
    gestaltTSMTEVersion = 'tmTV',
    gestaltTSMTE1 = 0x100
};


// update flag for TSMTERec

enum {
    kTSMTEAutoScroll = 1
};


// callback procedure definitions

typedef pascal void (*TSMTEPreUpdateProcPtr)(TEHandle textH, long refCon);

typedef pascal void (*TSMTEPostUpdateProcPtr)(TEHandle textH, long fixLen,
        long inputAreaStart, long inputAreaEnd,
        long pinStart, long pinEnd, long refCon);


// data types

struct TSMTERec
{
    TEHandle                textH;
    TSMTEPreUpdateProcPtr   preUpdateProc;
    TSMTEPostUpdateProcPtr  postUpdateProc;
    long                    updateFlag;
    long                    refCon;
};
typedef struct TSMTERec TSMTERec, *TSMTERecPtr, **TSMTERecHandle;


struct TSMDialogRecord
{
    DialogRecord    fDialog;
    TSMDocumentID   fDocID;
    TSMTERecHandle  fTSMTERecH;
    long            fTSMTERsvd[3];          // reserved
};
typedef struct TSMDialogRecord TSMDialogRecord, *TSMDialogPeek;

#endif
```

[Next](TSMTE%20Interfaces-PPCCIncludes-TSMTE.h.md)[Previous](InlineInputSample-InlineInputSample.r.md)

