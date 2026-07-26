---
title: MKMultiPolyline
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmultipolyline
source_url: 'https://developer.apple.com/documentation/mapkit/mkmultipolyline'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmultipolyline.json'
content_hash: 'sha256:ccec075e7a1e42dc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKMultiPolyline

<sub>Class</sub>

A collection of multipolyline shapes, each consisting of one or more connected line segments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class MKMultiPolyline
```

## Overview

Use a [MKMultiPolyline](mkmultipolyline.md) object when you have multiple distinct polyline shapes that you intend to render using the same style.

## Relationships

- **Inherits From**: [MKShape](mkshape.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [MKAnnotation](mkannotation.md), [MKGeoJSONObject](mkgeojsonobject.md), [MKOverlay](mkoverlay.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a multipolyline object

- [- initWithPolylines:](<mkmultipolyline/init(__).md>) — Creates a multipolyline object using the provided polylines.

### Accessing polyline objects

- [polylines](mkmultipolyline/polylines.md) — An array containing the polyline objects that make up the multipolyline object.

### Initializers

- [init(polylines:)](<mkmultipolyline/init(polylines_).md>)

## See Also

### Multiple segment lines

- [MKPolyline](mkpolyline.md) — An open polygon overlay consisting of one or more connected line segments.
- [MKGeodesicPolyline](mkgeodesicpolyline.md) — An open polygon overlay consisting of line segments that follow the contours of the Earth to create the shortest path between the specified points.
- [MKPolylineRenderer](mkpolylinerenderer.md) — A visual representation of any polyline overlay object.
- [MKMultiPolylineRenderer](mkmultipolylinerenderer.md) — A visual representation of multiple polyline overlay objects.
- [MKGradientPolylineRenderer](mkgradientpolylinerenderer.md) — A visual representation of any polyline overlay object with a gradient.
