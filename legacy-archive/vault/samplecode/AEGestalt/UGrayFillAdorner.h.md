---
title: AEGestalt
apple_id: DTS10000203
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/AEGestalt/Listings/UGrayFillAdorner_h.html
archived_at: '2026-07-18T02:59:27.944455Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AEGestalt](AEGestalt.md)


[Next](UInformationView.cp.md)[Previous](UGrayFillAdorner.cp.md)

# UGrayFillAdorner.h

```c
//  Copyright © 1991-92 Apple Computer, Inc. All rights reserved.
//  UGrayfillAdorner.h
//  Kent Sandvik DTS
//  This file contains the TGrayFill class, the gray background 
//  adornment in the window
//
//  <1>     khs     1.0     First final version


#ifndef __UGRAYFILLADORNER__
#define __UGRAYFILLADORNER__

#ifndef __UAEGESTALT__
#include "UAEGestalt.h"
#endif

DeclareClassDesc(TGrayFill);

class TGrayFill : public TAdorner
{

    DeclareClass(TGrayFill);

public:
    TGrayFill();
    virtual void Draw(TView* itsView,
                             const VRect&       /*area*/);
};

#endif
```

[Next](UInformationView.cp.md)[Previous](UGrayFillAdorner.cp.md)

