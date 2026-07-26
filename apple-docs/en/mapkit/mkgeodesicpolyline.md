---
title: MKGeodesicPolyline
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkgeodesicpolyline
source_url: 'https://developer.apple.com/documentation/mapkit/mkgeodesicpolyline'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkgeodesicpolyline.json'
content_hash: 'sha256:ad9f20cef78399c6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKGeodesicPolyline

<sub>Class</sub>

An open polygon overlay consisting of line segments that follow the contours of the Earth to create the shortest path between the specified points.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class MKGeodesicPolyline
```

## Overview

A geodesic polyline contains a set of points that connect end-to-end in the order that you provide them. The first and last points don’t automatically connect to each other. When displaying on a two-dimensional map view, the line segment between any two points may appear curved.

## Relationships

- **Inherits From**: [MKPolyline](mkpolyline.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [MKAnnotation](mkannotation.md), [MKGeoJSONObject](mkgeojsonobject.md), [MKOverlay](mkoverlay.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a geodesic polyline overlay

- [+ polylineWithPoints:count:](<mkgeodesicpolyline/init(points_count_).md>) — Creates and returns a geodesic polyline using the specified map points.
- [+ polylineWithCoordinates:count:](<mkgeodesicpolyline/init(coordinates_count_).md>) — Creates and returns a geodesic polyline using the specified coordinates.

## See Also

### Multiple segment lines

- [MKPolyline](mkpolyline.md) — An open polygon overlay consisting of one or more connected line segments.
- [MKMultiPolyline](mkmultipolyline.md) — A collection of multipolyline shapes, each consisting of one or more connected line segments.
- [MKPolylineRenderer](mkpolylinerenderer.md) — A visual representation of any polyline overlay object.
- [MKMultiPolylineRenderer](mkmultipolylinerenderer.md) — A visual representation of multiple polyline overlay objects.
- [MKGradientPolylineRenderer](mkgradientpolylinerenderer.md) — A visual representation of any polyline overlay object with a gradient.
