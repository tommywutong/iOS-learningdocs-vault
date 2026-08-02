---
title: 'BracketStripes: Using the Bracketed Capture API'
apple_id: TP40014579
resource_type: Sample Code
platform: iOS
topic: null
technology: AVFoundation
published: '2016-09-28'
source_url: https://developer.apple.com/library/archive/samplecode/BracketStripes/Listings/BracketStripes_Macros_h.html
archived_at: '2026-07-18T03:02:17.258183Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [BracketStripes: Using the Bracketed Capture API](BracketStripes-%20Using%20the%20Bracketed%20Capture%20API.md)


[Next](BracketStripes-BracketStripesImageViewController.h.md)[Previous](BracketStripes-BracketStripesCameraViewController.m.md)

# BracketStripes/Macros.h

```
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Helpful macros.
 */

// Clamp _value to range [_lo, _hi]
#define CLAMP(_value, _lo, _hi) \
    MAX( (_lo), MIN( (_hi), (_value) ) )
```

[Next](BracketStripes-BracketStripesImageViewController.h.md)[Previous](BracketStripes-BracketStripesCameraViewController.m.md)

