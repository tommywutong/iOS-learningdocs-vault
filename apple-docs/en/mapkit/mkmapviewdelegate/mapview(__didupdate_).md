---
title: 'mapView(_:didUpdate:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapviewdelegate/mapview(_:didupdate:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapview(_:didupdate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapviewdelegate/mapview%28_%3Adidupdate%3A%29.json'
content_hash: 'sha256:c4f6460a4dabe029'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapViewDelegate](../mkmapviewdelegate.md)

# mapView(_:didUpdate:)

<sub>Instance Method</sub>

Tells the delegate when the map view updates the user’s location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func mapView(_ mapView: MKMapView, didUpdate userLocation: MKUserLocation)
```

## Parameters

- `mapView` — The map view that’s tracking the user’s location.

- `userLocation` — The location object representing the user’s latest location. This property may be `nil`.

## Discussion

While the [showsUserLocation](../mkmapview/showsuserlocation.md) property is [true](../../swift/true.md), the map view calls this method whenever it receives a new location update. It also calls this method if the map view’s user-tracking mode is [MKUserTrackingModeFollowWithHeading](../mkusertrackingmode/followwithheading.md) and the heading changes.

The.map view doesn’t call this method if the app is running in the background. If you want to receive location updates while running in the background, use the Core Location framework.

## See Also

### Tracking the user’s location

- [- mapViewWillStartLocatingUser:](<mapviewwillstartlocatinguser(__).md>) — Tells the delegate that the map view is about to start tracking the user’s location.
- [- mapViewDidStopLocatingUser:](<mapviewdidstoplocatinguser(__).md>) — Tells the delegate when the map view stops tracking the user’s location.
- [- mapView:didFailToLocateUserWithError:](<mapview(__didfailtolocateuserwitherror_).md>) — Tells the delegate when an attempt to locate the user’s location fails.
- [- mapView:didChangeUserTrackingMode:animated:](<mapview(__didchange_animated_).md>) — Tells the delegate when the user-tracking mode changes.
