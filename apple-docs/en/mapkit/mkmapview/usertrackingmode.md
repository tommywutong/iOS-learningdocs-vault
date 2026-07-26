---
title: userTrackingMode
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 11.0+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapview/usertrackingmode
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/usertrackingmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/usertrackingmode.json'
content_hash: 'sha256:b8bb31b736231bc1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# userTrackingMode

<sub>Instance Property</sub>

The mode to use for tracking the user’s location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var userTrackingMode: MKUserTrackingMode { get set }
```

## Discussion

Setting the tracking mode to [MKUserTrackingModeFollow](../mkusertrackingmode/follow.md) or [MKUserTrackingModeFollowWithHeading](../mkusertrackingmode/followwithheading.md) causes the map view to center the map on that location and begin tracking the user’s location. If it’s zoomed out, the map view automatically zooms in on the user’s location, effectively changing the current visible region.

For possible values, see [MKUserTrackingMode](../mkusertrackingmode.md).

## See Also

### Displaying the user’s location

- [Converting a user’s location to a descriptive placemark](../converting-a-user-s-location-to-a-descriptive-placemark.md) — Transform the user’s location that displays on a map into an informative textual description by reverse geocoding.
- [showsUserLocation](showsuserlocation.md) — A Boolean value that indicates whether the map tries to display the user’s location.
- [userLocationVisible](isuserlocationvisible.md) — A Boolean value that indicates whether the user’s location is visible in the map view.
- [userLocation](userlocation.md) — The annotation object that represents the user’s location.
- [- setUserTrackingMode:animated:](<setusertrackingmode(__animated_).md>) — Sets the mode to use for tracking the user’s location, with optional animation.
- [MKUserTrackingMode](../mkusertrackingmode.md) — The mode to use for tracking the user’s location on the map.
