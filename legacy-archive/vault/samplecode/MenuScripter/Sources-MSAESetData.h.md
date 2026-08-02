---
title: MenuScripter
apple_id: DTS10000668
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MenuScripter/Listings/Sources_MSAESetData_h.html
archived_at: '2026-07-18T03:14:39.317211Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MenuScripter](MenuScripter.md)


[Next](Sources-MSAETextUtils.c.md)[Previous](Sources-MSAESetData.c.md)

# Sources/MSAESetData.h

```c
// MSAESetData.h
//
// Original version by Jon Lansdell and Nigel Humphreys.
// 4.0 and 3.1 updates by Greg Sutton.
// ©Apple Computer Inc 1996, all rights reserved.

#ifndef __MSAESETDATA__
#define __MSAESETDATA__

#include <Printing.h>
#include <OSA.h>

#include "MSToken.h"

pascal OSErr    DoSetData(const AppleEvent  *theAppleEvent,
                                AppleEvent  *reply,
                                long        handlerRefCon);

OSErr           HandleSetData(const AEDesc *theObj, AEDesc *dataDesc);

OSErr           SetApplicationProperty( const AEDesc *theTokenDesc, const AEDesc *dataDesc );
OSErr           SetApplicationTokenProperty( AppPropToken* theToken, const AEDesc *dataDesc );
OSErr           SetWindowProperty(const AEDesc *theWPTokenDesc, const AEDesc *dataDesc);
OSErr           SetWindowTokenProperty( WindowPropToken* theToken, const AEDesc* theData );
OSErr           SetWindowSelectionProperty(WindowPtr theWindow, const AEDesc *dataDesc);
OSErr           SetDocumentProperty( const AEDesc *theTokenDesc, const AEDesc *dataDesc );
OSErr           SetDocumentTokenProperty( WindowPropToken* theToken, const AEDesc *dataDesc );
OSErr           SetMenuProperty( const AEDesc *theTokenDesc, const AEDesc *dataDesc );
OSErr           SetMenuTokenProperty( MenuPropToken* theToken, const AEDesc* theData );
OSErr           SetMenuItemProperty( const AEDesc *theTokenDesc, const AEDesc *dataDesc );
OSErr           SetMenuItemTokenProperty( MenuItemPropToken* theToken, const AEDesc* theData );

OSErr           SetTextProperty(const AEDesc *tokenDesc, const AEDesc *dataDesc);
OSErr           CheckForMenuItemName( short theResID, OSAID theOSAID );

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

[Next](Sources-MSAETextUtils.c.md)[Previous](Sources-MSAESetData.c.md)

