---
title: AEGestalt
apple_id: DTS10000203
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/AEGestalt/Listings/UInformationView_h.html
archived_at: '2026-07-18T02:59:28.047148Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AEGestalt](AEGestalt.md)


[Next](ULabelView.cp.md)[Previous](UInformationView.cp.md)

# UInformationView.h

```c
//  UInformationView.h
//  Copyright © 1991-92 by Apple Computer, Inc. All rights reserved.
//  Kent Sandvik DTS
//  This file contains the class TInformationView, used to present
//  the information obtained over the network in the rightmost view
//
//  <1>     khs     1.0     First final version


#ifndef __UINFORMATIONVIEW__
#define __UINFORMATIONVIEW__

#ifndef __UAEGESTALT__
#include "UAEGestalt.h"
#endif


DeclareClassDesc(TInformationView);

class TInformationView : public TView
{

    DeclareClass(TInformationView);

public:
    TInformationView();
    virtual void Draw(const VRect& area);
    virtual void DrawInformation();

    //  FIELDS
    Boolean fHasGestaltInfo;
    CStr255 fLabel1, fLabel2, fLabel3, fLabel4, fLabel5, fLabel6, 
            fLabel7, fLabel8, fLabel9, fLabel10, fLabel11, fLabel12;
};

#endif
```

[Next](ULabelView.cp.md)[Previous](UInformationView.cp.md)

