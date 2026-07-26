---
title: MKPolygonRenderer
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkpolygonrenderer
source_url: 'https://developer.apple.com/documentation/mapkit/mkpolygonrenderer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkpolygonrenderer.json'
content_hash: 'sha256:8fa7df7b9fa268c6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKPolygonRenderer

<sub>Class</sub>

The visual representation of a single polygon overlay.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MKPolygonRenderer
```

## Overview

This renderer creates the polygon overlay by first filling the shape and then representing its outline with strokes. You can change the color and other drawing attributes of the polygon by modifying the properties inherited from the parent class.

## Relationships

- **Inherits From**: [MKOverlayPathRenderer](mkoverlaypathrenderer.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a polygon renderer

- [- initWithPolygon:](<mkpolygonrenderer/init(polygon_).md>) — Creates a new renderer that handles drawing for the specified polygon overlay object.

### Accessing the polygon overlay object

- [polygon](mkpolygonrenderer/polygon.md) — The polygon object that contains the information used to draw the overlay’s contents.

### Accessing the stroke

- [strokeStart](mkpolygonrenderer/strokestart.md) — The unit distance along the polygon where the stroke starts.
- [strokeEnd](mkpolygonrenderer/strokeend.md) — The unit distance along the polygon where the stroke ends.

## See Also

### Custom shape overlays

- [MKPolygon](mkpolygon.md) — A closed polygon overlay.
- [MKMultiPolygon](mkmultipolygon.md) — A collection of multiple closed polygon overlays.
- [MKMultiPolygonRenderer](mkmultipolygonrenderer.md) — The visual representation of multiple polygon overlays.
- [MKOverlayPathRenderer](mkoverlaypathrenderer.md) — The visual representation of a path-based overlay.
