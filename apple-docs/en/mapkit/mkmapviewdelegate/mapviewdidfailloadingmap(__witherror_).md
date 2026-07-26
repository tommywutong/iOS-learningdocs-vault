---
title: 'mapViewDidFailLoadingMap(_:withError:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapviewdelegate/mapviewdidfailloadingmap(_:witherror:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapviewdidfailloadingmap(_:witherror:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapviewdelegate/mapviewdidfailloadingmap%28_%3Awitherror%3A%29.json'
content_hash: 'sha256:87bd33852708e3c1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapViewDelegate](../mkmapviewdelegate.md)

# mapViewDidFailLoadingMap(_:withError:)

<sub>Instance Method</sub>

Tells the delegate that the specified view is unable to load the map data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func mapViewDidFailLoadingMap(_ mapView: MKMapView, withError error: any Error)
```

## Parameters

- `mapView` — The map view that starts the load operation.

- `error` — The reason that the map view can’t load the map data.

## Discussion

The map view might call this method in situations where the device doesn’t have access to the network or is unable to load the map data for some reason. The map view may also call this method if a request for additional map tiles comes in while a previous request for tiles is pending. You can use this message to notify the user that the map data is unavailable.

## See Also

### Loading the map data

- [- mapViewWillStartLoadingMap:](<mapviewwillstartloadingmap(__).md>) — Tells the delegate that the specified map view is about to retrieve some map data.
- [- mapViewDidFinishLoadingMap:](<mapviewdidfinishloadingmap(__).md>) — Tells the delegate when the specified map view successfully loads the needed map data.
- [- mapViewWillStartRenderingMap:](<mapviewwillstartrenderingmap(__).md>) — Tells the delegate that the map view is about to start rendering some of its tiles.
- [- mapViewDidFinishRenderingMap:fullyRendered:](<mapviewdidfinishrenderingmap(__fullyrendered_).md>) — Tells the delegate when the map view finishes rendering all visible tiles.
