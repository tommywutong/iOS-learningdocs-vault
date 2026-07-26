---
title: MKMultiPolylineRenderer
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmultipolylinerenderer
source_url: 'https://developer.apple.com/documentation/mapkit/mkmultipolylinerenderer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmultipolylinerenderer.json'
content_hash: 'sha256:de34bd6937b869de'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKMultiPolylineRenderer

<sub>Class</sub>

A visual representation of multiple polyline overlay objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MKMultiPolylineRenderer
```

## Overview

Use the multipolyline renderer to provide the styling of multiple polylines that you create using [MKMultiPolyline](mkmultipolyline.md).

## Relationships

- **Inherits From**: [MKOverlayPathRenderer](mkoverlaypathrenderer.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a multipolyline renderer

- [- initWithMultiPolyline:](<mkmultipolylinerenderer/init(multipolyline_).md>) — Creates an object that renders a visual representation of multiple polyline objects.

### Accessing the multipolyline object

- [multiPolyline](mkmultipolylinerenderer/multipolyline.md) — An object that represents multiple polyline shapes, each consisting of one or more connected line segments.

## See Also

### Multiple segment lines

- [MKPolyline](mkpolyline.md) — An open polygon overlay consisting of one or more connected line segments.
- [MKGeodesicPolyline](mkgeodesicpolyline.md) — An open polygon overlay consisting of line segments that follow the contours of the Earth to create the shortest path between the specified points.
- [MKMultiPolyline](mkmultipolyline.md) — A collection of multipolyline shapes, each consisting of one or more connected line segments.
- [MKPolylineRenderer](mkpolylinerenderer.md) — A visual representation of any polyline overlay object.
- [MKGradientPolylineRenderer](mkgradientpolylinerenderer.md) — A visual representation of any polyline overlay object with a gradient.
