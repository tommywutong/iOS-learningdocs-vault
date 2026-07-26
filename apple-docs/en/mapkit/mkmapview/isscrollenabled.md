---
title: isScrollEnabled
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapview/isscrollenabled
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/isscrollenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/isscrollenabled.json'
content_hash: 'sha256:e7be87f4426a9393'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# isScrollEnabled

<sub>Instance Property</sub>

A Boolean value that determines whether the user may scroll around the map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isScrollEnabled: Bool { get set }
```

## Discussion

This property controls only user interactions with the map. If you set the value of this property to [false](../../swift/false.md), you may still change the map location programmatically by changing the value in the [region](region.md) property.

The default value of this property is [true](../../swift/true.md).

## See Also

### Accessing map properties

- [MKMapType](../mkmaptype.md) — The type of map to display. _(deprecated)_
- [zoomEnabled](iszoomenabled.md) — A Boolean value that determines whether the user may use pinch gestures to zoom in and out of the map.
- [pitchEnabled](ispitchenabled.md) — A Boolean value that indicates whether the map uses the camera’s pitch information.
- [rotateEnabled](isrotateenabled.md) — A Boolean value that indicates whether the map uses the camera’s heading information.
- [mapType](maptype.md) — The type of data the map view displays. _(deprecated)_
