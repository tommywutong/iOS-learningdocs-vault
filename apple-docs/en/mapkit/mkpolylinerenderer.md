---
title: MKPolylineRenderer
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkpolylinerenderer
source_url: 'https://developer.apple.com/documentation/mapkit/mkpolylinerenderer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkpolylinerenderer.json'
content_hash: 'sha256:3f54c6dcc82b34b5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKPolylineRenderer

<sub>Class</sub>

A visual representation of any polyline overlay object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MKPolylineRenderer
```

## Overview

This renderer strokes the line only; it doesn’t fill it. You can change the color and other drawing attributes of the polyline by modifying the properties it inherits from the main class. You typically use this class as-is and don’t subclass it.

## Relationships

- **Inherits From**: [MKOverlayPathRenderer](mkoverlaypathrenderer.md)

- **Inherited By**: [MKGradientPolylineRenderer](mkgradientpolylinerenderer.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a polyline renderer

- [- initWithPolyline:](<mkpolylinerenderer/init(polyline_).md>) — Creates a new overlay view using the specified polyline overlay object.

### Accessing the polyline overlay

- [polyline](mkpolylinerenderer/polyline.md) — The polyline overlay object that contains the information for drawing the overlay.

### Accessing the stroke

- [strokeStart](mkpolylinerenderer/strokestart.md) — The unit distance along the line where the stroke starts.
- [strokeEnd](mkpolylinerenderer/strokeend.md) — The unit distance along the line where the stroke ends.

## See Also

### Multiple segment lines

- [MKPolyline](mkpolyline.md) — An open polygon overlay consisting of one or more connected line segments.
- [MKGeodesicPolyline](mkgeodesicpolyline.md) — An open polygon overlay consisting of line segments that follow the contours of the Earth to create the shortest path between the specified points.
- [MKMultiPolyline](mkmultipolyline.md) — A collection of multipolyline shapes, each consisting of one or more connected line segments.
- [MKMultiPolylineRenderer](mkmultipolylinerenderer.md) — A visual representation of multiple polyline overlay objects.
- [MKGradientPolylineRenderer](mkgradientpolylinerenderer.md) — A visual representation of any polyline overlay object with a gradient.
