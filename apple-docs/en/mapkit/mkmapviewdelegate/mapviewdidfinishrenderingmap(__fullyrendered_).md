---
title: 'mapViewDidFinishRenderingMap(_:fullyRendered:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapviewdelegate/mapviewdidfinishrenderingmap(_:fullyrendered:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapviewdidfinishrenderingmap(_:fullyrendered:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapviewdelegate/mapviewdidfinishrenderingmap%28_%3Afullyrendered%3A%29.json'
content_hash: 'sha256:930bed1fd7355fbd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapViewDelegate](../mkmapviewdelegate.md)

# mapViewDidFinishRenderingMap(_:fullyRendered:)

<sub>Instance Method</sub>

Tells the delegate when the map view finishes rendering all visible tiles.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func mapViewDidFinishRenderingMap(_ mapView: MKMapView, fullyRendered: Bool)
```

## Parameters

- `mapView` — The map view rendering its tiles.

- `fullyRendered` — This parameter is [true](../../swift/true.md) if the map view is able to render all tiles completely, or [false](../../swift/false.md) if errors prevent the map view from rendering all tiles.

## Discussion

This method lets you know when the map view finishes rendering all of the currently visible tiles to the best of its ability. The map view calls this method regardless of whether the view renders all tiles successfully. If there are errors loading one or more tiles that prevent the map view from rendering them, MapKit sets the `fullyRendered` parameter to [false](../../swift/false.md).

## See Also

### Loading the map data

- [- mapViewWillStartLoadingMap:](<mapviewwillstartloadingmap(__).md>) — Tells the delegate that the specified map view is about to retrieve some map data.
- [- mapViewDidFinishLoadingMap:](<mapviewdidfinishloadingmap(__).md>) — Tells the delegate when the specified map view successfully loads the needed map data.
- [- mapViewDidFailLoadingMap:withError:](<mapviewdidfailloadingmap(__witherror_).md>) — Tells the delegate that the specified view is unable to load the map data.
- [- mapViewWillStartRenderingMap:](<mapviewwillstartrenderingmap(__).md>) — Tells the delegate that the map view is about to start rendering some of its tiles.
