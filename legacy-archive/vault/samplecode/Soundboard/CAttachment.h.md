---
title: Soundboard
apple_id: DTS10000059
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Soundboard/Listings/CAttachment_h.html
archived_at: '2026-07-18T03:25:12.314601Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Soundboard](Soundboard.md)


[Next](CFilterControl.cp.md)[Previous](CAttachment.cp.md)

# CAttachment.h

```c
// ===========================================================================
//  CAttachment.h               ©1995 Apple Computer, Inc. All rights reserved.
// ===========================================================================

#pragma once

#include <LAttachment.h>


// ===========================================================================
// ¥ C3DBorderAttachment                                 C3DBorderAttachment ¥
// ===========================================================================

class   C3DBorderAttachment : public LAttachment {
public:
            C3DBorderAttachment(void);

protected:
    virtual void    ExecuteSelf(MessageT inMessage, void *ioParam);
};
```

[Next](CFilterControl.cp.md)[Previous](CAttachment.cp.md)

