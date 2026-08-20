---
title: CopyBits vs. CopyMask
apple_id: DTS10000076
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/CopyBits_vs._CopyMask/Listings/Test_h.html
archived_at: '2026-07-18T03:04:20.043499Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CopyBits vs. CopyMask](CopyBits%20vs.%20CopyMask.md)


[Next](Document%20Revision%20History.md)[Previous](Test.c.md)

# Test.h

```c
/*
    File:       Test.h

    Contains:   

    Written by: Tony Myles  

    Copyright:  Copyright © 1992-1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                7/9/1999    Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1


*/

#include <Dialogs.h>
#include <Fonts.h>
#ifndef __QDOFFSCREEN__
#include <QDOffscreen.h>
#endif


enum
{
    kFrameCount = 500,
    kCopyBitsPictItem = 1,
    kCopyBitsFramesItem = 11,
    kCopyBitsTicksItem = 12,
    kCopyBitsFPSItem = 13,
    kCopyMaskPictItem = 2,
    kCopyMaskFramesItem = 14,
    kCopyMaskTicksItem = 15,
    kCopyMaskFPSItem = 16,
    kApplePictResID = 128,
    kPixPatResID = 128
};


void LetTheGameBegin(DialogPtr srcDialogP);
OSErr CreateOptimumGWorld(GWorldPtr *optGWorld, Rect *devRect);
OSErr CreateGWorldFromPict(GWorldPtr *pictGWorld, PicHandle pictH);
OSErr CreateGWorldFromPictResource(GWorldPtr *pictGWorldP, short pictResID);
OSErr CreateGrafPort(Rect *newPortRect, GrafPtr *newPort);
OSErr CreateGrafPortFromPictResource(short pictID, GrafPtr *offScrnPort);
void DisposeGrafPort(GrafPtr doomedPort);
void GetDItemText(DialogPtr dlgP, short itemNum, Str255 itemStr);
void SetDItemText(DialogPtr dlgP, short itemNum, Str255 itemStr);
void GetDItemRect(DialogPtr dlgP, short itemNum, Rect *itemRect);
```

[Next](Document%20Revision%20History.md)[Previous](Test.c.md)

