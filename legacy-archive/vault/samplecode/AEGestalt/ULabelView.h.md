---
title: AEGestalt
apple_id: DTS10000203
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/AEGestalt/Listings/ULabelView_h.html
archived_at: '2026-07-18T02:59:28.153516Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AEGestalt](AEGestalt.md)


[Next](ULookupCommand.cp.md)[Previous](ULabelView.cp.md)

# ULabelView.h

```c
//  ULabelView.h
//  Copyright © 1991-92 by Apple Computer, Inc. All rights reserved.
//  Kent Sandvik DTS
//  This file contains the TLabelView class, used for displaying
//  the labels in the leftmost view
//
//  <1>     khs     1.0     First final version


#ifndef __ULABELVIEW__
#define __ULABELVIEW__

#ifndef __UAEGESTALT__
#include "UAEGestalt.h"
#endif


DeclareClassDesc(TLabelView);

class TLabelView : public TView
{

    DeclareClass(TLabelView);

public:
    TLabelView();
    virtual void Draw(const VRect& area);
    virtual void DrawLabels();

    //  FIELDS
    CStr255 fLabel1, fLabel2, fLabel3, fLabel4, fLabel5, fLabel6, fLabel7, 
            fLabel8, fLabel9, fLabel10, fLabel11, fLabel12;
};

#endif
```

[Next](ULookupCommand.cp.md)[Previous](ULabelView.cp.md)

