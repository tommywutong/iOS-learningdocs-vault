---
title: 'Footprint: Indoor Positioning with Core Location'
apple_id: TP40014457
resource_type: Sample Code
platform: iOS
topic: null
technology: CoreLocation
published: '2016-09-28'
source_url: https://developer.apple.com/library/archive/samplecode/footprint/Listings/ObjC_Footprint_AAPLHideBackgroundOverlay_m.html
archived_at: '2026-07-18T03:29:10.556107Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Footprint: Indoor Positioning with Core Location](Footprint-%20Indoor%20Positioning%20with%20Core%20Location.md)


[Next](ObjC-Footprint-AAPLFloorplanOverlay.h.md)[Previous](ObjC-Footprint-AAPLFloorplanOverlay.m.md)

# ObjC/Footprint/AAPLHideBackgroundOverlay.m

```objc
/**
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This class provides an MKOverlay that can be used to hide MapKit's underlaying map tiles.
*/

#import "AAPLHideBackgroundOverlay.h"

@implementation AAPLHideBackgroundOverlay

+ (instancetype)hideBackgroundOverlay {
    MKMapPoint corners[4];
    corners[0] = MKMapPointMake(MKMapRectGetMaxX(MKMapRectWorld), MKMapRectGetMaxY(MKMapRectWorld));
    corners[1] = MKMapPointMake(MKMapRectGetMinX(MKMapRectWorld), MKMapRectGetMaxY(MKMapRectWorld));
    corners[2] = MKMapPointMake(MKMapRectGetMinX(MKMapRectWorld), MKMapRectGetMinY(MKMapRectWorld));
    corners[3] = MKMapPointMake(MKMapRectGetMaxX(MKMapRectWorld), MKMapRectGetMinY(MKMapRectWorld));

    return [AAPLHideBackgroundOverlay polygonWithPoints:corners count:4];
}

/**
    @return YES to tell MapKit to hide its underlying map tiles, as long as
        this overlay is visible (which, as you can see above, is everywhere in
        the world), effectively hiding all map tiles and replacing them with a
        solid colored \c MKPolygon.
 */
- (BOOL)canReplaceMapContent {
    return YES;
}

@end
```

[Next](ObjC-Footprint-AAPLFloorplanOverlay.h.md)[Previous](ObjC-Footprint-AAPLFloorplanOverlay.m.md)

