---
title: MKPolyline
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkpolyline
source_url: 'https://developer.apple.com/documentation/mapkit/mkpolyline'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkpolyline.json'
content_hash: 'sha256:63733f14eb3e7699'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKPolyline

<sub>Class</sub>

An open polygon overlay consisting of one or more connected line segments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class MKPolyline
```

## Overview

The points connect end-to-end in the order that you provide them. The first and last points don’t automatically connect to each other.

## Relationships

- **Inherits From**: [MKMultiPoint](mkmultipoint.md)

- **Inherited By**: [MKGeodesicPolyline](mkgeodesicpolyline.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [MKAnnotation](mkannotation.md), [MKGeoJSONObject](mkgeojsonobject.md), [MKOverlay](mkoverlay.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a polyline overlay

- [+ polylineWithPoints:count:](<mkpolyline/init(points_count_).md>) — Creates a polyline object from the specified set of map points.
- [+ polylineWithCoordinates:count:](<mkpolyline/init(coordinates_count_).md>) — Creates a polyline object from the specified set of coordinates.

## See Also

### Multiple segment lines

- [MKGeodesicPolyline](mkgeodesicpolyline.md) — An open polygon overlay consisting of line segments that follow the contours of the Earth to create the shortest path between the specified points.
- [MKMultiPolyline](mkmultipolyline.md) — A collection of multipolyline shapes, each consisting of one or more connected line segments.
- [MKPolylineRenderer](mkpolylinerenderer.md) — A visual representation of any polyline overlay object.
- [MKMultiPolylineRenderer](mkmultipolylinerenderer.md) — A visual representation of multiple polyline overlay objects.
- [MKGradientPolylineRenderer](mkgradientpolylinerenderer.md) — A visual representation of any polyline overlay object with a gradient.
