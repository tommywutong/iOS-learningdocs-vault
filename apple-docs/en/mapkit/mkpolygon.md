---
title: MKPolygon
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkpolygon
source_url: 'https://developer.apple.com/documentation/mapkit/mkpolygon'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkpolygon.json'
content_hash: 'sha256:72f06db0ef823539'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKPolygon

<sub>Class</sub>

A closed polygon overlay.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class MKPolygon
```

## Overview

The points you add to this overlay connect end-to-end in the order you provide them. The first and last points connect to each other to create a closed shape.

When creating a polygon, you can mask out portions of the polygon by specifying one or more interior polygons. For the polygons you specify, this class uses the even-odd fill rule to determine the final occupied area. When applied to overlapping polygons, this rule can cause the framework to mask specific regions out and thereby remove them from the total occupied area. For more information about how fill rules apply to paths, see [Paths](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/dq_paths/dq_paths.html#//apple_ref/doc/uid/TP30001066-CH211) in [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066).

## Relationships

- **Inherits From**: [MKMultiPoint](mkmultipoint.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [MKAnnotation](mkannotation.md), [MKGeoJSONObject](mkgeojsonobject.md), [MKOverlay](mkoverlay.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a polygon overlay

- [+ polygonWithPoints:count:](<mkpolygon/init(points_count_).md>) — Creates and returns a polygon object from the specified set of map points.
- [+ polygonWithPoints:count:interiorPolygons:](<mkpolygon/init(points_count_interiorpolygons_).md>) — Creates and returns a polygon object from the specified set of map points and interior polygons.
- [+ polygonWithCoordinates:count:](<mkpolygon/init(coordinates_count_).md>) — Creates and returns a polygon object from the specified set of coordinates.
- [+ polygonWithCoordinates:count:interiorPolygons:](<mkpolygon/init(coordinates_count_interiorpolygons_).md>) — Creates and returns a polygon object from the specified set of coordinates and interior polygons.

### Accessing the interior polygons

- [interiorPolygons](mkpolygon/interiorpolygons.md) — The array of polygons that nest inside the enclosing polygon.

## See Also

### Custom shape overlays

- [MKPolygonRenderer](mkpolygonrenderer.md) — The visual representation of a single polygon overlay.
- [MKMultiPolygon](mkmultipolygon.md) — A collection of multiple closed polygon overlays.
- [MKMultiPolygonRenderer](mkmultipolygonrenderer.md) — The visual representation of multiple polygon overlays.
- [MKOverlayPathRenderer](mkoverlaypathrenderer.md) — The visual representation of a path-based overlay.
