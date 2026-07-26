---
title: 'mapViewDidFinishLoadingMap(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapviewdelegate/mapviewdidfinishloadingmap(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapviewdidfinishloadingmap(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapviewdelegate/mapviewdidfinishloadingmap%28_%3A%29.json'
content_hash: 'sha256:3802891e8b8c21b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapViewDelegate](../mkmapviewdelegate.md)

# mapViewDidFinishLoadingMap(_:)

<sub>Instance Method</sub>

Tells the delegate when the specified map view successfully loads the needed map data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func mapViewDidFinishLoadingMap(_ mapView: MKMapView)
```

## Parameters

- `mapView` — The map view that starts the load operation.

## Discussion

The map view calls this method when it finishes reloading the map tiles associated with the current request. The map view requests map tiles when a new visible area scrolls into view and tiles aren’t already available. The map may also request map tiles for portions of the map that aren’t currently visible. For example, the map view may load tiles immediately surrounding the currently visible area as needed to handle small pans by the user.

## See Also

### Loading the map data

- [- mapViewWillStartLoadingMap:](<mapviewwillstartloadingmap(__).md>) — Tells the delegate that the specified map view is about to retrieve some map data.
- [- mapViewDidFailLoadingMap:withError:](<mapviewdidfailloadingmap(__witherror_).md>) — Tells the delegate that the specified view is unable to load the map data.
- [- mapViewWillStartRenderingMap:](<mapviewwillstartrenderingmap(__).md>) — Tells the delegate that the map view is about to start rendering some of its tiles.
- [- mapViewDidFinishRenderingMap:fullyRendered:](<mapviewdidfinishrenderingmap(__fullyrendered_).md>) — Tells the delegate when the map view finishes rendering all visible tiles.
