---
title: MKShape
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkshape
source_url: 'https://developer.apple.com/documentation/mapkit/mkshape'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkshape.json'
content_hash: 'sha256:bf59c59f743361cc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKShape

<sub>Class</sub>

An abstract class that defines the basic properties for all shape-based overlay objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class MKShape
```

## Overview

You can’t instantiate this class directly; use a subclass instead. Subclasses are responsible for defining the geometry of the shape and providing an appropriate value for the coordinate property they inherit from the [MKAnnotation](mkannotation.md) protocol.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [MKCircle](mkcircle.md), [MKMultiPoint](mkmultipoint.md), [MKMultiPolygon](mkmultipolygon.md), [MKMultiPolyline](mkmultipolyline.md), [MKPointAnnotation](mkpointannotation.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [MKAnnotation](mkannotation.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Accessing the shape attributes

- [title](mkshape/title.md) — The title of the shape annotation.
- [subtitle](mkshape/subtitle.md) — The subtitle of the shape annotation.

## See Also

### Shared behavior

- [MKOverlay](mkoverlay.md) — An interface for associating content with a specific map region.
- [MKOverlayRenderer](mkoverlayrenderer.md) — The shared infrastructure for drawing overlays on the map surface.
- [MKMultiPoint](mkmultipoint.md) — An abstract class that defines the common behavior that open and closed polygon overlays share.
- [MKPlacemark](mkplacemark.md) — A user-friendly description of a location on the map. _(deprecated)_
