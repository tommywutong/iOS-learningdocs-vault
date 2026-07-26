---
title: MKCircleRenderer
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkcirclerenderer
source_url: 'https://developer.apple.com/documentation/mapkit/mkcirclerenderer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkcirclerenderer.json'
content_hash: 'sha256:e3caa379b703f1df'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKCircleRenderer

<sub>Class</sub>

The visual representation of a circular overlay.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MKCircleRenderer
```

## Overview

This renderer fills and strokes the circular region that the overlay object represents. You can change the color and other drawing attributes of the circle by modifying the properties it inherits from the main class. You typically use this class as-is and don’t subclass it.

You create an instance of this class in your map view delegate’s [- mapView:rendererForOverlay:](<mkmapviewdelegate/mapview(__rendererfor_).md>) method.

## Relationships

- **Inherits From**: [MKOverlayPathRenderer](mkoverlaypathrenderer.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a circle renderer

- [- initWithCircle:](<mkcirclerenderer/init(circle_).md>) — Creates a new overlay view using the specified circle overlay object.

### Accessing the overlay object

- [circle](mkcirclerenderer/circle.md) — The circle overlay object that contains the information for drawing the overlay.

### Accessing the stroke

- [strokeStart](mkcirclerenderer/strokestart.md) — The unit distance along the circle where the stroke starts.
- [strokeEnd](mkcirclerenderer/strokeend.md) — The unit distance along the circle where the stroke ends.

## See Also

### Circular overlays

- [MKCircle](mkcircle.md) — A circular overlay with a configurable radius that you center on a geographic coordinate.
