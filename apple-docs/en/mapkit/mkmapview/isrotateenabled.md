---
title: isRotateEnabled
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapview/isrotateenabled
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/isrotateenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/isrotateenabled.json'
content_hash: 'sha256:b612391f03b07f54'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# isRotateEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether the map uses the camera’s heading information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var isRotateEnabled: Bool { get set }
```

## Discussion

When this property is [true](../../swift/true.md) and the framework associates a valid camera with the map, the map uses the camera’s heading angle to rotate the plane of the map around its center point. When this property is [false](../../swift/false.md), the map view ignores the camera’s heading angle and the map orients so that the map view situates true north at the top.

## See Also

### Accessing map properties

- [MKMapType](../mkmaptype.md) — The type of map to display. _(deprecated)_
- [zoomEnabled](iszoomenabled.md) — A Boolean value that determines whether the user may use pinch gestures to zoom in and out of the map.
- [scrollEnabled](isscrollenabled.md) — A Boolean value that determines whether the user may scroll around the map.
- [pitchEnabled](ispitchenabled.md) — A Boolean value that indicates whether the map uses the camera’s pitch information.
- [mapType](maptype.md) — The type of data the map view displays. _(deprecated)_
