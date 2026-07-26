---
title: interiorPolygons
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkpolygon/interiorpolygons
source_url: 'https://developer.apple.com/documentation/mapkit/mkpolygon/interiorpolygons'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkpolygon/interiorpolygons.json'
content_hash: 'sha256:160577e1e13bc2a0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKPolygon](../mkpolygon.md)

# interiorPolygons

<sub>Instance Property</sub>

The array of polygons that nest inside the enclosing polygon.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var interiorPolygons: [MKPolygon]? { get }
```

## Discussion

When the screen renders a polygon, the renderer masks the area that any interior polygons occupy so they aren’t part of the polygon.
