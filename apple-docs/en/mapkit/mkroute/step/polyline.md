---
title: polyline
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkroute/step/polyline
source_url: 'https://developer.apple.com/documentation/mapkit/mkroute/step/polyline'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkroute/step/polyline.json'
content_hash: 'sha256:38829a6d52ecb485'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKRoute](../../mkroute.md) · [Step](../step.md)

# polyline

<sub>Instance Property</sub>

The detailed step geometry.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var polyline: MKPolyline { get }
```

## Discussion

The polyline object in this property contains the geometry for this step. You can use the polyline object as an overlay in a map view.
