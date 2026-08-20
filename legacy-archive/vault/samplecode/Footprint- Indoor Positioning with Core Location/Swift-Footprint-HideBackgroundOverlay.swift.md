---
title: 'Footprint: Indoor Positioning with Core Location'
apple_id: TP40014457
resource_type: Sample Code
platform: iOS
topic: null
technology: CoreLocation
published: '2016-09-28'
source_url: https://developer.apple.com/library/archive/samplecode/footprint/Listings/Swift_Footprint_HideBackgroundOverlay_swift.html
archived_at: '2026-07-18T03:29:11.419947Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Footprint: Indoor Positioning with Core Location](Footprint-%20Indoor%20Positioning%20with%20Core%20Location.md)


[Next](Document%20Revision%20History.md)[Previous](Swift-Footprint-Utilities.swift.md)

# Swift/Footprint/HideBackgroundOverlay.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This class provides an MKOverlay that can be used to hide MapKit's
                underlaying map tiles.
*/

import Foundation
import MapKit

/**
    This class provides an MKOverlay that can be used to hide MapKit's
    underlaying map tiles.
*/
class HideBackgroundOverlay: MKPolygon {

    /// - returns: a HideBackgroundOverlay object that covers the world.
    class func hideBackgroundOverlay() -> HideBackgroundOverlay {
        var corners =  [MKMapPointMake(MKMapRectGetMaxX(MKMapRectWorld), MKMapRectGetMaxY(MKMapRectWorld)),
                        MKMapPointMake(MKMapRectGetMinX(MKMapRectWorld), MKMapRectGetMaxY(MKMapRectWorld)),
                        MKMapPointMake(MKMapRectGetMinX(MKMapRectWorld), MKMapRectGetMinY(MKMapRectWorld)),
                        MKMapPointMake(MKMapRectGetMaxX(MKMapRectWorld), MKMapRectGetMinY(MKMapRectWorld))]
        return HideBackgroundOverlay(points: &corners, count: corners.count)
    }

    /**
        - returns: true to tell MapKit to hide its underlying map tiles, as long
            as this overlay is visible (which, as you can see above, is
            everywhere in the world), effectively hiding all map tiles and
            replacing them with a solid colored MKPolygon.
    */
    override func canReplaceMapContent() -> Bool {
        return true
    }


}
```

[Next](Document%20Revision%20History.md)[Previous](Swift-Footprint-Utilities.swift.md)

