---
title: MKMultiPolygon
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmultipolygon
source_url: 'https://developer.apple.com/documentation/mapkit/mkmultipolygon'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmultipolygon.json'
content_hash: 'sha256:706eabd586beed9f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKMultiPolygon

<sub>Class</sub>

A collection of multiple closed polygon overlays.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class MKMultiPolygon
```

## Overview

Use a [MKMultiPolygon](mkmultipolygon.md) when you have multiple distinct polygon shapes that you intend to render using the same style.

## Relationships

- **Inherits From**: [MKShape](mkshape.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [MKAnnotation](mkannotation.md), [MKGeoJSONObject](mkgeojsonobject.md), [MKOverlay](mkoverlay.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a multipolygon

- [- initWithPolygons:](<mkmultipolygon/init(__).md>) — Creates a multipolygon object using the provided polygons.

### Accessing polygons

- [polygons](mkmultipolygon/polygons.md) — An array containing the polygons that make up the multipolygon object.

### Initializers

- [init(polygons:)](<mkmultipolygon/init(polygons_).md>)

## See Also

### Custom shape overlays

- [MKPolygon](mkpolygon.md) — A closed polygon overlay.
- [MKPolygonRenderer](mkpolygonrenderer.md) — The visual representation of a single polygon overlay.
- [MKMultiPolygonRenderer](mkmultipolygonrenderer.md) — The visual representation of multiple polygon overlays.
- [MKOverlayPathRenderer](mkoverlaypathrenderer.md) — The visual representation of a path-based overlay.
