---
title: 'mapViewWillStartLoadingMap(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapviewdelegate/mapviewwillstartloadingmap(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapviewwillstartloadingmap(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapviewdelegate/mapviewwillstartloadingmap%28_%3A%29.json'
content_hash: 'sha256:98c706e786fd2091'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapViewDelegate](../mkmapviewdelegate.md)

# mapViewWillStartLoadingMap(_:)

<sub>Instance Method</sub>

Tells the delegate that the specified map view is about to retrieve some map data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func mapViewWillStartLoadingMap(_ mapView: MKMapView)
```

## Parameters

- `mapView` — The map view that begins loading the data.

## Discussion

The map view calls this method whenever it needs to download a new group of map tiles from the server. This typically occurs whenever you expose portions of the map by panning or zooming the content. You can use this method to mark the time that it takes for the map view to load the data.

## See Also

### Loading the map data

- [- mapViewDidFinishLoadingMap:](<mapviewdidfinishloadingmap(__).md>) — Tells the delegate when the specified map view successfully loads the needed map data.
- [- mapViewDidFailLoadingMap:withError:](<mapviewdidfailloadingmap(__witherror_).md>) — Tells the delegate that the specified view is unable to load the map data.
- [- mapViewWillStartRenderingMap:](<mapviewwillstartrenderingmap(__).md>) — Tells the delegate that the map view is about to start rendering some of its tiles.
- [- mapViewDidFinishRenderingMap:fullyRendered:](<mapviewdidfinishrenderingmap(__fullyrendered_).md>) — Tells the delegate when the map view finishes rendering all visible tiles.
