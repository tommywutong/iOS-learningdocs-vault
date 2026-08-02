---
title: 'Footprint: Indoor Positioning with Core Location'
apple_id: TP40014457
resource_type: Sample Code
platform: iOS
topic: null
technology: CoreLocation
published: '2016-09-28'
source_url: https://developer.apple.com/library/archive/samplecode/footprint/Listings/ObjC_Footprint_AAPLHideBackgroundOverlay_h.html
archived_at: '2026-07-18T03:29:10.511329Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Footprint: Indoor Positioning with Core Location](Footprint-%20Indoor%20Positioning%20with%20Core%20Location.md)


[Next](ObjC-Footprint-AAPLFloorplanOverlay.m.md)[Previous](ObjC-Footprint-AAPLAppDelegate.m.md)

# ObjC/Footprint/AAPLHideBackgroundOverlay.h

```objc
/**
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This class provides an MKOverlay that can be used to hide MapKit's underlaying map tiles.
*/

@import MapKit;

/**
    This class provides an \c MKOverlay that can be used to hide MapKit's
    underlaying map tiles.
*/
@interface AAPLHideBackgroundOverlay : MKPolygon

/// @return an \c AAPLHideBackgroundOverlay object that covers the world
+ (instancetype)hideBackgroundOverlay;

@end
```

[Next](ObjC-Footprint-AAPLFloorplanOverlay.m.md)[Previous](ObjC-Footprint-AAPLAppDelegate.m.md)

