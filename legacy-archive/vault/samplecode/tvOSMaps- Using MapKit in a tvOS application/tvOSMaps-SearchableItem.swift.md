---
title: 'tvOSMaps: Using MapKit in a tvOS application'
apple_id: TP40017314
resource_type: Sample Code
platform: tvOS
topic: User Experience
technology: MapKit
published: '2016-10-04'
source_url: https://developer.apple.com/library/archive/samplecode/tvOSMaps/Listings/tvOSMaps_SearchableItem_swift.html
archived_at: '2026-07-26T19:54:16.671507Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [tvOSMaps: Using MapKit in a tvOS application](tvOSMaps-%20Using%20MapKit%20in%20a%20tvOS%20application.md)


[Next](README.md.md)[Previous](tvOSMaps-SearchableItem%2BSampleData.swift.md)

# tvOSMaps/SearchableItem.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A simple struct representing an item that can be searched for.
*/

import CoreLocation

struct SearchableItem: Equatable {

    // MARK: Properties

    let identifier: String

    let title: String

    let location: CLLocationCoordinate2D
}

// MARK: Equatable

func ==(lhs: SearchableItem, rhs: SearchableItem)-> Bool {
    // Two `SearchableItem`s are considered equal if their identifiers.
    return lhs.identifier == rhs.identifier
}
```

[Next](README.md.md)[Previous](tvOSMaps-SearchableItem%2BSampleData.swift.md)

