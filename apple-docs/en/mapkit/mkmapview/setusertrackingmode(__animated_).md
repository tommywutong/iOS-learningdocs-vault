---
title: 'setUserTrackingMode(_:animated:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 11.0+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapview/setusertrackingmode(_:animated:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/setusertrackingmode(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/setusertrackingmode%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:bdd381247150c49d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# setUserTrackingMode(_:animated:)

<sub>Instance Method</sub>

Sets the mode to use for tracking the user’s location, with optional animation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setUserTrackingMode(_ mode: MKUserTrackingMode, animated: Bool)
```

## Parameters

- `mode` — The mode for tracking the user’s location. [MKUserTrackingMode](../mkusertrackingmode.md) describes the possible values.

- `animated` — If [true](../../swift/true.md), the map animates the change from the current mode to the new mode; otherwise, it doesn’t. This parameter affects only tracking-mode changes. Changes to the user’s location or heading use animation.

## Discussion

Setting the tracking mode to [MKUserTrackingModeFollow](../mkusertrackingmode/follow.md) or [MKUserTrackingModeFollowWithHeading](../mkusertrackingmode/followwithheading.md) causes the map view to center the map on that location and begin tracking the user’s location. If it’s zoomed out, the map view automatically zooms in on the user’s location, effectively changing the current visible region.

## See Also

### Related Documentation

- [- mapView:didChangeUserTrackingMode:animated:](<../mkmapviewdelegate/mapview(__didchange_animated_).md>) — Tells the delegate when the user-tracking mode changes.
- [- mapView:didUpdateUserLocation:](<../mkmapviewdelegate/mapview(__didupdate_).md>) — Tells the delegate when the map view updates the user’s location.
- [heading](../mkuserlocation/heading.md) — The heading of the user’s location.

### Displaying the user’s location

- [Converting a user’s location to a descriptive placemark](../converting-a-user-s-location-to-a-descriptive-placemark.md) — Transform the user’s location that displays on a map into an informative textual description by reverse geocoding.
- [showsUserLocation](showsuserlocation.md) — A Boolean value that indicates whether the map tries to display the user’s location.
- [userLocationVisible](isuserlocationvisible.md) — A Boolean value that indicates whether the user’s location is visible in the map view.
- [userLocation](userlocation.md) — The annotation object that represents the user’s location.
- [userTrackingMode](usertrackingmode.md) — The mode to use for tracking the user’s location.
- [MKUserTrackingMode](../mkusertrackingmode.md) — The mode to use for tracking the user’s location on the map.
