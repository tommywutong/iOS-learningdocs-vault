---
title: MKMultiPolygonRenderer
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmultipolygonrenderer
source_url: 'https://developer.apple.com/documentation/mapkit/mkmultipolygonrenderer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmultipolygonrenderer.json'
content_hash: 'sha256:cdc861fe27faf9b0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKMultiPolygonRenderer

<sub>Class</sub>

The visual representation of multiple polygon overlays.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MKMultiPolygonRenderer
```

## Overview

Use this renderer to provide the style for multiple polygons created using [MKMultiPolygon](mkmultipolygon.md).

## Relationships

- **Inherits From**: [MKOverlayPathRenderer](mkoverlaypathrenderer.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a multipolygon renderer

- [- initWithMultiPolygon:](<mkmultipolygonrenderer/init(multipolygon_).md>) — Creates and returns a renderer that handles drawing for the specified multipolygon overlay object.

### Accessing the multipolygon object

- [multiPolygon](mkmultipolygonrenderer/multipolygon.md) — The multipolygon object that the renderer uses to draw the overlay’s contents.

## See Also

### Custom shape overlays

- [MKPolygon](mkpolygon.md) — A closed polygon overlay.
- [MKPolygonRenderer](mkpolygonrenderer.md) — The visual representation of a single polygon overlay.
- [MKMultiPolygon](mkmultipolygon.md) — A collection of multiple closed polygon overlays.
- [MKOverlayPathRenderer](mkoverlaypathrenderer.md) — The visual representation of a path-based overlay.
