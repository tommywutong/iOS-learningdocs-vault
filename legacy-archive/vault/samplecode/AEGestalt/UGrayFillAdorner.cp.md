---
title: AEGestalt
apple_id: DTS10000203
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/AEGestalt/Listings/UGrayFillAdorner_cp.html
archived_at: '2026-07-18T02:59:27.873353Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AEGestalt](AEGestalt.md)


[Next](UGrayFillAdorner.h.md)[Previous](UAEServerCommand.h.md)

# UGrayFillAdorner.cp

```c
//  Copyright © 1991-92 Apple Computer, Inc. All rights reserved.
//  UGrayfillAdorner.cp
//  Kent Sandvik DTS
//  This file is used for specifying the TGrayFill member functions,
//  i.e. drawing gray in the views in forms of an adorner.
//
//  <1>     khs     1.0     First final version


#ifndef __UGRAYFILLADORNER__
#include "UGrayfillAdorner.h"
#endif

//  Globals
// Setup the KS-look&feel gray global
CRGBColor gKSRGBGray(36000,
                     40500,
                     37500);


//  Empty constructor - for avoiding ptabs in global data space

#undef Inherited
#define Inherited TAdorner

#pragma segment ARes
DefineClass(TGrayFill, TAdorner);

TGrayFill::TGrayFill()
{
}


//  Draw TGrayFill Adorner method
#pragma segment ARes
void TGrayFill::Draw(TView* itsView,
                            const VRect&        /*area*/)
{
    CRGBColor saveColor;
    PenState savePenState;
    VRect adornArea;
    CRect QDArea;
    CRect tempRect;

    // save off the current pen state and the foreground color
    GetPenState(&savePenState);
    GetIfColor(saveColor);
    PenNormal();

    // get area
    itsView->GetAdornExtent(adornArea);
    itsView->ViewToQDRect(adornArea, QDArea);
    tempRect = QDArea;

    // colorize it
    SetIfColor(gKSRGBGray);
    PaintRect(tempRect);

    // restore the foreground color and the pen
    SetIfColor(saveColor);
    SetPenState(&savePenState);
}
```

[Next](UGrayFillAdorner.h.md)[Previous](UAEServerCommand.h.md)

