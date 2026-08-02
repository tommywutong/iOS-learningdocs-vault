---
title: 'Footprint: Indoor Positioning with Core Location'
apple_id: TP40014457
resource_type: Sample Code
platform: iOS
topic: null
technology: CoreLocation
published: '2016-09-28'
source_url: https://developer.apple.com/library/archive/samplecode/footprint/Listings/ObjC_Footprint_AAPLViewController_h.html
archived_at: '2026-07-18T03:29:10.694252Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Footprint: Indoor Positioning with Core Location](Footprint-%20Indoor%20Positioning%20with%20Core%20Location.md)


[Next](ObjC-Footprint-AAPLViewController.m.md)[Previous](ObjC-Footprint-AAPLCoordinateConverter.h.md)

# ObjC/Footprint/AAPLViewController.h

```objc
/**
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Primary view controller for what is displayed by the application. In this class we configure an MKMapView to display a floorplan, recieve location updates to determine floor number, as well as provide a few helpful debugging annotations.

                We will also show how to highlight a region that you have defined in PDF coordinates but not Latitude  Longitude.
*/

@import UIKit;

/**
    Primary view controller for what is displayed by the application.

    In this class we configure an \c MKMapView to display a floorplan, recieve
    location updates to determine floor number, as well as provide a few helpful
    debugging annotations.

    We will also show how to highlight a region that you have defined in PDF
    coordinates but not Latitude & Longitude.
*/
@interface AAPLViewController : UIViewController
@end
```

[Next](ObjC-Footprint-AAPLViewController.m.md)[Previous](ObjC-Footprint-AAPLCoordinateConverter.h.md)

