---
title: showsUserLocation
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapview/showsuserlocation
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/showsuserlocation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/showsuserlocation.json'
content_hash: 'sha256:f26f6213eb8a0b60'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# showsUserLocation

<sub>Instance Property</sub>

A Boolean value that indicates whether the map tries to display the user’s location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var showsUserLocation: Bool { get set }
```

## Discussion

This property doesn’t indicate whether the user’s location is actually visible on the map, only whether the map view tries to display it. Setting this property to [true](../../swift/true.md) causes the map view to use the Core Location framework to find the user’s location and try to display it on the map. While this property is [true](../../swift/true.md), the map view continues to track the user’s location and update it periodically. The default value of this property is [false](../../swift/false.md).

Showing the user’s location doesn’t ensure that it’s visible on the map. The user might scroll the map to a different point, causing the location to be offscreen. To determine whether the user’s location displays on the map, use the [userLocationVisible](isuserlocationvisible.md) property.

## See Also

### Displaying the user’s location

- [Converting a user’s location to a descriptive placemark](../converting-a-user-s-location-to-a-descriptive-placemark.md) — Transform the user’s location that displays on a map into an informative textual description by reverse geocoding.
- [userLocationVisible](isuserlocationvisible.md) — A Boolean value that indicates whether the user’s location is visible in the map view.
- [userLocation](userlocation.md) — The annotation object that represents the user’s location.
- [userTrackingMode](usertrackingmode.md) — The mode to use for tracking the user’s location.
- [- setUserTrackingMode:animated:](<setusertrackingmode(__animated_).md>) — Sets the mode to use for tracking the user’s location, with optional animation.
- [MKUserTrackingMode](../mkusertrackingmode.md) — The mode to use for tracking the user’s location on the map.
