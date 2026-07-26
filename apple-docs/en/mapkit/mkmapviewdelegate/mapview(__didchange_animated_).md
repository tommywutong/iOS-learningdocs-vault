---
title: 'mapView(_:didChange:animated:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 11.0+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapviewdelegate/mapview(_:didchange:animated:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapview(_:didchange:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapviewdelegate/mapview%28_%3Adidchange%3Aanimated%3A%29.json'
content_hash: 'sha256:d8dfc0caee1bda83'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapViewDelegate](../mkmapviewdelegate.md)

# mapView(_:didChange:animated:)

<sub>Instance Method</sub>

Tells the delegate when the user-tracking mode changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func mapView(_ mapView: MKMapView, didChange mode: MKUserTrackingMode, animated: Bool)
```

## Parameters

- `mapView` — The map view where the user-tracking mode changes.

- `mode` — The mode to use for tracking the user’s location.

- `animated` — If [true](../../swift/true.md), the map animates the change from the current mode to the new mode; otherwise, the map doesn’t animate the change. This parameter affects only tracking-mode changes. The map animates all changes to the user’s location and heading.

## See Also

### Related Documentation

- [- setUserTrackingMode:animated:](<../mkmapview/setusertrackingmode(__animated_).md>) — Sets the mode to use for tracking the user’s location, with optional animation.

### Tracking the user’s location

- [- mapViewWillStartLocatingUser:](<mapviewwillstartlocatinguser(__).md>) — Tells the delegate that the map view is about to start tracking the user’s location.
- [- mapViewDidStopLocatingUser:](<mapviewdidstoplocatinguser(__).md>) — Tells the delegate when the map view stops tracking the user’s location.
- [- mapView:didUpdateUserLocation:](<mapview(__didupdate_).md>) — Tells the delegate when the map view updates the user’s location.
- [- mapView:didFailToLocateUserWithError:](<mapview(__didfailtolocateuserwitherror_).md>) — Tells the delegate when an attempt to locate the user’s location fails.
