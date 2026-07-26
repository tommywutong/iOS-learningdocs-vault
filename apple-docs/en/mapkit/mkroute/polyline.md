---
title: polyline
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkroute/polyline
source_url: 'https://developer.apple.com/documentation/mapkit/mkroute/polyline'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkroute/polyline.json'
content_hash: 'sha256:2fb7e4e6941e7cc2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKRoute](../mkroute.md)

# polyline

<sub>Instance Property</sub>

The detailed route geometry.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var polyline: MKPolyline { get }
```

## Discussion

The polyline object in this property reflects the complete path of the route, including all of its steps. You can use the polyline object as an overlay in a map view.

## See Also

### Getting the route geometry

- [steps](steps.md) — The array of steps that create the overall route.
- [Step](step.md) — One portion of an overall route.
