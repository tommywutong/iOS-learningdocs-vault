---
title: 'mapViewDidStopLocatingUser(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapviewdelegate/mapviewdidstoplocatinguser(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapviewdidstoplocatinguser(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapviewdelegate/mapviewdidstoplocatinguser%28_%3A%29.json'
content_hash: 'sha256:10d7fd82d019b1fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapViewDelegate](../mkmapviewdelegate.md)

# mapViewDidStopLocatingUser(_:)

<sub>Instance Method</sub>

Tells the delegate when the map view stops tracking the user’s location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func mapViewDidStopLocatingUser(_ mapView: MKMapView)
```

## Parameters

- `mapView` — The map view that stops tracking the user’s location.

## Discussion

The map view calls this method when the value of the [showsUserLocation](../mkmapview/showsuserlocation.md) property changes to [false](../../swift/false.md).

## See Also

### Tracking the user’s location

- [- mapViewWillStartLocatingUser:](<mapviewwillstartlocatinguser(__).md>) — Tells the delegate that the map view is about to start tracking the user’s location.
- [- mapView:didUpdateUserLocation:](<mapview(__didupdate_).md>) — Tells the delegate when the map view updates the user’s location.
- [- mapView:didFailToLocateUserWithError:](<mapview(__didfailtolocateuserwitherror_).md>) — Tells the delegate when an attempt to locate the user’s location fails.
- [- mapView:didChangeUserTrackingMode:animated:](<mapview(__didchange_animated_).md>) — Tells the delegate when the user-tracking mode changes.
