---
title: 'mapView(_:didFailToLocateUserWithError:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapviewdelegate/mapview(_:didfailtolocateuserwitherror:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapview(_:didfailtolocateuserwitherror:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapviewdelegate/mapview%28_%3Adidfailtolocateuserwitherror%3A%29.json'
content_hash: 'sha256:a97f1d0f1b3cd8b9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapViewDelegate](../mkmapviewdelegate.md)

# mapView(_:didFailToLocateUserWithError:)

<sub>Instance Method</sub>

Tells the delegate when an attempt to locate the user’s location fails.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func mapView(_ mapView: MKMapView, didFailToLocateUserWithError error: any Error)
```

## Parameters

- `mapView` — The map view that’s tracking the user’s location.

- `error` — An error object containing the reason why location tracking fails.

## See Also

### Tracking the user’s location

- [- mapViewWillStartLocatingUser:](<mapviewwillstartlocatinguser(__).md>) — Tells the delegate that the map view is about to start tracking the user’s location.
- [- mapViewDidStopLocatingUser:](<mapviewdidstoplocatinguser(__).md>) — Tells the delegate when the map view stops tracking the user’s location.
- [- mapView:didUpdateUserLocation:](<mapview(__didupdate_).md>) — Tells the delegate when the map view updates the user’s location.
- [- mapView:didChangeUserTrackingMode:animated:](<mapview(__didchange_animated_).md>) — Tells the delegate when the user-tracking mode changes.
