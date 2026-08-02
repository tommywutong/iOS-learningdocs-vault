---
title: Soundboard
apple_id: DTS10000059
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Soundboard/Listings/CGrayBox_h.html
archived_at: '2026-07-18T03:25:12.579787Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Soundboard](Soundboard.md)


[Next](CQuickTimeWindow.cp.md)[Previous](CGrayBox.cp.md)

# CGrayBox.h

```c
// ===========================================================================
//  CGrayBox.h                  ©1995 Apple Computer, Inc. All rights reserved.
// ===========================================================================

#pragma once

#include <LView.h>

const RGBColor              mLtGray = {0xAAAA, 0xAAAA, 0xAAAA};


class   CGrayBox : public LView {
public:
    enum { class_ID = 'gBox' };

    static CGrayBox*        CreateGrayBoxStream(LStream *inStream);
                            CGrayBox(LStream *inStream);

    virtual void            Draw(RgnHandle inSuperDrawRgnH);

protected:
    Boolean                 mDrawGrayBkgrnd;

    virtual void            DrawSelf(); 
    virtual void            ApplyForeAndBackColors();
};
```

[Next](CQuickTimeWindow.cp.md)[Previous](CGrayBox.cp.md)

