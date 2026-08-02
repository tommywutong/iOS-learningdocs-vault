---
title: AEGestalt
apple_id: DTS10000203
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/AEGestalt/Listings/ULabelView_cp.html
archived_at: '2026-07-18T02:59:28.086415Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AEGestalt](AEGestalt.md)


[Next](ULabelView.h.md)[Previous](UInformationView.h.md)

# ULabelView.cp

```c
//  ULabelView.cp 
//  Copyright © 1991-92 by Apple Computer, Inc. All rights reserved.
//  Kent Sandvik DTS
//  This file contains all the member functions for TLabelView, i.e.
//  it handles the drawing of the TLabelView view.
//
//  <1>     khs     1.0     First final version


#ifndef __ULABELVIEW__  
#include "ULabelView.h" 
#endif


#undef Inherited
#define Inherited TView

#pragma segment AInit
DefineClass(TLabelView, TView);

TLabelView::TLabelView()
{

    //  create all the label strings, yes, this would be far better if we
    //  loaded them in from STR# resources, and maybe we will do this in the
    //  next improved version (and charge $99 for the 1.1 release)
    fLabel1 = "¥ Machine type:";
    fLabel2 = "¥ System Version:";
    fLabel3 = "¥ Processor Type:";
    fLabel4 = "¥ Has FPU?";
    fLabel5 = "¥ Has Color Quickdraw?";
    fLabel6 = "¥ Has 32-bit Quickdraw?";
    fLabel7 = "¥ Has SCSI?";
    fLabel8 = "¥ Has Apple Event Mgr?";
    fLabel9 = "¥ Has EditionMgr?";
    fLabel10 = "¥ Is A/UX system?";
    fLabel11 = "¥ Has TrueType?";
    fLabel12 = "¥ AppleTalk driver no:";
}


//  Draw the information contained in the drawing object field to screen
#pragma segment ARes
void TLabelView::Draw(const VRect& area)
{
    Inherited::Draw(area);
    // draw the real thing!
    this->DrawLabels();
}


#pragma segment ARes
void TLabelView::DrawLabels()
{
    // Set font and font size
    PenNormal();
    TextFont(geneva);
    TextSize(9);

    // Draw Labels
    MoveTo(kHorizontStart, kVerticalStart);
    DrawString(fLabel1);
    MoveTo(kHorizontStart, kVerticalStart + kVerticalOffset);
    DrawString(fLabel2);
    MoveTo(kHorizontStart, kVerticalStart + 2 * kVerticalOffset);
    DrawString(fLabel3);
    MoveTo(kHorizontStart, kVerticalStart + 3 * kVerticalOffset);
    DrawString(fLabel4);
    MoveTo(kHorizontStart, kVerticalStart + 4 * kVerticalOffset);
    DrawString(fLabel5);
    MoveTo(kHorizontStart, kVerticalStart + 5 * kVerticalOffset);
    DrawString(fLabel6);
    MoveTo(kHorizontStart, kVerticalStart + 6 * kVerticalOffset);
    DrawString(fLabel7);
    MoveTo(kHorizontStart, kVerticalStart + 7 * kVerticalOffset);
    DrawString(fLabel8);
    MoveTo(kHorizontStart, kVerticalStart + 8 * kVerticalOffset);
    DrawString(fLabel9);
    MoveTo(kHorizontStart, kVerticalStart + 9 * kVerticalOffset);
    DrawString(fLabel10);
    MoveTo(kHorizontStart, kVerticalStart + 10 * kVerticalOffset);
    DrawString(fLabel11);
    MoveTo(kHorizontStart, kVerticalStart + 11 * kVerticalOffset);
    DrawString(fLabel12);

    // restore pen
    PenNormal();
}
```

[Next](ULabelView.h.md)[Previous](UInformationView.h.md)

