---
title: MKGradientPolylineRenderer
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkgradientpolylinerenderer
source_url: 'https://developer.apple.com/documentation/mapkit/mkgradientpolylinerenderer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkgradientpolylinerenderer.json'
content_hash: 'sha256:59c33fdedad429e6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKGradientPolylineRenderer

<sub>Class</sub>

A visual representation of any polyline overlay object with a gradient.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MKGradientPolylineRenderer
```

## Overview

This renderer only applies a stroke to the line; it doesn’t fill it. Set the gradients with [setColors:atLocations:](mkgradientpolylinerenderer/setcolors_atlocations_.md) and pair colors to locations that MapKit represents as unit distance values along the distance of the polyline. Don’t subclass `MKGradientPolylineRenderer`. Use the class as-is.

The gradient displays itself along the direction of the line.

## Relationships

- **Inherits From**: [MKPolylineRenderer](mkpolylinerenderer.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Accessing the gradient colors

- [setColors(_:locations:)](<mkgradientpolylinerenderer/setcolors(__locations_)-3xrou.md>) — Sets the iOS colors and corresponding unit distance values to create gradients.
- [setColors(_:locations:)](<mkgradientpolylinerenderer/setcolors(__locations_)-1tuft.md>) — Sets the macOS colors and corresponding unit distance values to create gradients.
- [colors](mkgradientpolylinerenderer/colors.md) — An array that represents the gradient’s color transition points.
- [locations](mkgradientpolylinerenderer/locations-7k6qz.md) — An array of location indexes that correspond to their respective colors.

## See Also

### Multiple segment lines

- [MKPolyline](mkpolyline.md) — An open polygon overlay consisting of one or more connected line segments.
- [MKGeodesicPolyline](mkgeodesicpolyline.md) — An open polygon overlay consisting of line segments that follow the contours of the Earth to create the shortest path between the specified points.
- [MKMultiPolyline](mkmultipolyline.md) — A collection of multipolyline shapes, each consisting of one or more connected line segments.
- [MKPolylineRenderer](mkpolylinerenderer.md) — A visual representation of any polyline overlay object.
- [MKMultiPolylineRenderer](mkmultipolylinerenderer.md) — A visual representation of multiple polyline overlay objects.
