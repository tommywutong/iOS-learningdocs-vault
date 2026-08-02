---
title: 'Footprint: Indoor Positioning with Core Location'
apple_id: TP40014457
resource_type: Sample Code
platform: iOS
topic: null
technology: CoreLocation
published: '2016-09-28'
source_url: https://developer.apple.com/library/archive/samplecode/footprint/Listings/ObjC_Footprint_AAPLFloorplanOverlayRenderer_h.html
archived_at: '2026-07-18T03:29:10.133922Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Footprint: Indoor Positioning with Core Location](Footprint-%20Indoor%20Positioning%20with%20Core%20Location.md)


[Next](ObjC-Footprint-AAPLFloorplanOverlayRenderer.m.md)[Previous](ObjC-Footprint-AAPLCoordinateConverter.m.md)

# ObjC/Footprint/AAPLFloorplanOverlayRenderer.h

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This class draws your AAPLFloorplanOverlay into an MKMapView. It is also capable of drawing diagnostic visuals to help with debugging, if needed.
*/

@import MapKit;

/**
    This class draws your AAPLFloorplanOverlay into an MKMapView.
    It is also capable of drawing diagnostic visuals to help with debugging,
    if needed.
*/
@interface AAPLFloorplanOverlayRenderer : MKOverlayRenderer

/**
    @note Overrides the drawMapRect method for \c MKOverlayRenderer.
*/
- (void)drawMapRect:(MKMapRect)mapRect zoomScale:(MKZoomScale)zoomScale inContext:(CGContextRef)context;

@end
```

[Next](ObjC-Footprint-AAPLFloorplanOverlayRenderer.m.md)[Previous](ObjC-Footprint-AAPLCoordinateConverter.m.md)

