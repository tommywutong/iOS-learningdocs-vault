---
title: MKMultiPoint
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmultipoint
source_url: 'https://developer.apple.com/documentation/mapkit/mkmultipoint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmultipoint.json'
content_hash: 'sha256:9f283284892587b4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKMultiPoint

<sub>Class</sub>

An abstract class that defines the common behavior that open and closed polygon overlays share.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class MKMultiPoint
```

## Overview

Don’t create instances of this class directly. Instead, create instances of the [MKPolygon](mkpolygon.md) or [MKPolyline](mkpolyline.md) classes. However, you can use the methods and property of this class to access information about the specific points associated with the line or polygon.

## Relationships

- **Inherits From**: [MKShape](mkshape.md)

- **Inherited By**: [MKPolygon](mkpolygon.md), [MKPolyline](mkpolyline.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [MKAnnotation](mkannotation.md), [MKGeoJSONObject](mkgeojsonobject.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Accessing the points in the shape

- [- points](<mkmultipoint/points().md>) — Returns an array of map points associated with the shape.
- [pointCount](mkmultipoint/pointcount.md) — The number of points associated with the shape.
- [- locationAtPointIndex:](<mkmultipoint/location(atpointindex_).md>) — Translates a point index into a unit distance along the shape.
- [locations(at:)](<mkmultipoint/locations(at_).md>) — Translates a point index set into a unit distance along the shape.

### Getting coordinate values

- [- getCoordinates:range:](<mkmultipoint/getcoordinates(__range_).md>) — Retrieves one or more points associated with the shape and converts them to coordinate values.

## See Also

### Shared behavior

- [MKOverlay](mkoverlay.md) — An interface for associating content with a specific map region.
- [MKOverlayRenderer](mkoverlayrenderer.md) — The shared infrastructure for drawing overlays on the map surface.
- [MKShape](mkshape.md) — An abstract class that defines the basic properties for all shape-based overlay objects.
- [MKPlacemark](mkplacemark.md) — A user-friendly description of a location on the map. _(deprecated)_
