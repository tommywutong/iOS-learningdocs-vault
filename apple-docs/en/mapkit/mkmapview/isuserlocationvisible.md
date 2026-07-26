---
title: isUserLocationVisible
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapview/isuserlocationvisible
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/isuserlocationvisible'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/isuserlocationvisible.json'
content_hash: 'sha256:3ed9e33794224f2c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# isUserLocationVisible

<sub>Instance Property</sub>

A Boolean value that indicates whether the user’s location is visible in the map view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isUserLocationVisible: Bool { get }
```

## Discussion

When determining whether the user’s location is visible, this property factors in the horizontal accuracy of the location data. Specifically, if the rectangle that the user’s location represents, plus or minus the horizontal accuracy of that location, intersects the map’s visible rectangle, this property contains the value [true](../../swift/true.md). If that location rectangle doesn’t intersect the map’s visible rectangle, this property contains the value [false](../../swift/false.md).

When the user’s location is unknown, this property contains the value [false](../../swift/false.md).

## See Also

### Displaying the user’s location

- [Converting a user’s location to a descriptive placemark](../converting-a-user-s-location-to-a-descriptive-placemark.md) — Transform the user’s location that displays on a map into an informative textual description by reverse geocoding.
- [showsUserLocation](showsuserlocation.md) — A Boolean value that indicates whether the map tries to display the user’s location.
- [userLocation](userlocation.md) — The annotation object that represents the user’s location.
- [userTrackingMode](usertrackingmode.md) — The mode to use for tracking the user’s location.
- [- setUserTrackingMode:animated:](<setusertrackingmode(__animated_).md>) — Sets the mode to use for tracking the user’s location, with optional animation.
- [MKUserTrackingMode](../mkusertrackingmode.md) — The mode to use for tracking the user’s location on the map.
