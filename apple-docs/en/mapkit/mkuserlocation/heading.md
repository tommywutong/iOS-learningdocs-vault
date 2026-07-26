---
title: heading
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.9+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkuserlocation/heading
source_url: 'https://developer.apple.com/documentation/mapkit/mkuserlocation/heading'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkuserlocation/heading.json'
content_hash: 'sha256:63097f99ffa7d0b9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKUserLocation](../mkuserlocation.md)

# heading

<sub>Instance Property</sub>

The heading of the user’s location.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var heading: CLHeading? { get }
```

## Discussion

This property is `nil` if the user’s location tracking mode isn’t [MKUserTrackingModeFollowWithHeading](../mkusertrackingmode/followwithheading.md).

## See Also

### Determining the user’s location

- [location](location.md) — The location of the device.
- [updating](isupdating.md) — A Boolean value that indicates whether the map view is updating the user’s location.
