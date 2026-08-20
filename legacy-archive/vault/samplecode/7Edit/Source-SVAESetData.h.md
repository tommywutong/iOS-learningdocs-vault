---
title: 7Edit
apple_id: DTS10000200
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/7Edit/Listings/Source_SVAESetData_h.html
archived_at: '2026-07-18T02:59:19.467663Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [7Edit](7Edit.md)


[Next](Source-SVAETextUtils.c.md)[Previous](Source-SVAESetData.c.md)

# Source/SVAESetData.h

```c
/*
    File:       SVAESetData.h

    Contains:   

    Written by: Original version by Jon Lansdell and Nigel Humphreys.
                3.1 updates by Greg Sutton.

    Copyright:  Copyright © 1995-1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                7/20/1999   Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1


*/
#ifndef __SVAESETDATA__
#define __SVAESETDATA__

#include <Printing.h>

#include "SVToken.h"

pascal OSErr    DoSetData(const AppleEvent  *theAppleEvent,
                                AppleEvent  *reply,
                                long        handlerRefCon);

OSErr           HandleSetData(const AEDesc *theObj, AEDesc *dataDesc);

OSErr           DoSetWindowProperty(const AEDesc *theWPTokenDesc, const AEDesc *dataDesc);
OSErr           SetWindowSelectionProperty(WindowPtr theWindow, const AEDesc *dataDesc);

OSErr           SetTextProperty(const AEDesc *tokenDesc, const AEDesc *dataDesc);

OSErr           SetFontOfTextToken(TextToken* theToken, Str255 name);
OSErr           SetSizeOfTextToken(TextToken* theToken, short theSize);
OSErr           SetStyleOfTextToken(TextToken* theToken, Style onStyle, Style offStyle);
OSErr           GetTextStyles(const AEDesc *dataDesc, Style *onStyles, Style *offStyles);
void            AddDescStyleItem(DescType theDesc, Style *theStyle);
OSErr           MakeStyleFromAEList(const AEDescList *styleList, Style *theStyle, Boolean *hadPlain);
short           ItemForNamedFont(Str255 theName);

OSErr           GetTHPrintFromDescriptor(const AEDesc *sourceDesc, THPrint *result);

#endif
```

[Next](Source-SVAETextUtils.c.md)[Previous](Source-SVAESetData.c.md)

