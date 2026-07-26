---
title: isPitchEnabled
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapview/ispitchenabled
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/ispitchenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/ispitchenabled.json'
content_hash: 'sha256:90c094dadf6561f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# isPitchEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether the map uses the camera’s pitch information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var isPitchEnabled: Bool { get set }
```

## Discussion

When this property is [true](../../swift/true.md) and the framework associates a valid camera with the map, the map view uses the camera’s pitch angle to tilt the plane of the map. When this property is [false](../../swift/false.md), the map ignores the camera’s pitch angle and the map displays as if the user is looking straight down onto it.

In an app, be sure to check the value of this property to determine whether a map can support 3D.

## See Also

### Accessing map properties

- [MKMapType](../mkmaptype.md) — The type of map to display. _(deprecated)_
- [zoomEnabled](iszoomenabled.md) — A Boolean value that determines whether the user may use pinch gestures to zoom in and out of the map.
- [scrollEnabled](isscrollenabled.md) — A Boolean value that determines whether the user may scroll around the map.
- [rotateEnabled](isrotateenabled.md) — A Boolean value that indicates whether the map uses the camera’s heading information.
- [mapType](maptype.md) — The type of data the map view displays. _(deprecated)_
