---
title: 'tvOSMaps: Using MapKit in a tvOS application'
apple_id: TP40017314
resource_type: Sample Code
platform: tvOS
topic: User Experience
technology: MapKit
published: '2016-10-04'
source_url: https://developer.apple.com/library/archive/samplecode/tvOSMaps/Listings/tvOSMaps_SearchResultMapAnnotation_swift.html
archived_at: '2026-07-26T19:54:16.661329Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [tvOSMaps: Using MapKit in a tvOS application](tvOSMaps-%20Using%20MapKit%20in%20a%20tvOS%20application.md)


[Next](tvOSMaps-SearchableItem%2BSampleData.swift.md)[Previous](tvOSMaps-MapViewController.swift.md)

# tvOSMaps/SearchResultMapAnnotation.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    An `NSObject` subclass that implements the `MKAnnotation` protocol to allow `SearchableItem`s to be displayed on an `MKMapView`.
*/

import MapKit

class SearchResultMapAnnotation: NSObject, MKAnnotation {

    let item: SearchableItem

    var coordinate: CLLocationCoordinate2D {
        return item.location
    }

    var title: String? {
        return item.title
    }

    init(item: SearchableItem) {
        self.item = item
    }
}
```

[Next](tvOSMaps-SearchableItem%2BSampleData.swift.md)[Previous](tvOSMaps-MapViewController.swift.md)

