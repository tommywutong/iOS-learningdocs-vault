---
title: 'mapViewWillStartRenderingMap(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapviewdelegate/mapviewwillstartrenderingmap(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapviewwillstartrenderingmap(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapviewdelegate/mapviewwillstartrenderingmap%28_%3A%29.json'
content_hash: 'sha256:a41a4697aaccc5d3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapViewDelegate](../mkmapviewdelegate.md)

# mapViewWillStartRenderingMap(_:)

<sub>Instance Method</sub>

Tells the delegate that the map view is about to start rendering some of its tiles.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func mapViewWillStartRenderingMap(_ mapView: MKMapView)
```

## Parameters

- `mapView` — The map view that’s about to start rendering.

## Discussion

The map view calls this method when the map reveals one or more tiles that require rendering.

## See Also

### Loading the map data

- [- mapViewWillStartLoadingMap:](<mapviewwillstartloadingmap(__).md>) — Tells the delegate that the specified map view is about to retrieve some map data.
- [- mapViewDidFinishLoadingMap:](<mapviewdidfinishloadingmap(__).md>) — Tells the delegate when the specified map view successfully loads the needed map data.
- [- mapViewDidFailLoadingMap:withError:](<mapviewdidfailloadingmap(__witherror_).md>) — Tells the delegate that the specified view is unable to load the map data.
- [- mapViewDidFinishRenderingMap:fullyRendered:](<mapviewdidfinishrenderingmap(__fullyrendered_).md>) — Tells the delegate when the map view finishes rendering all visible tiles.
