---
title: MKOverlayPathRenderer
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkoverlaypathrenderer
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlaypathrenderer.json'
content_hash: 'sha256:bf104f8f0fdd310b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKOverlayPathRenderer

<sub>Class</sub>

The visual representation of a path-based overlay.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MKOverlayPathRenderer
```

## Overview

Use this renderer when a [CGPath](../coregraphics/cgpath.md) object defines your overlay’s shape. By default, this renderer fills the overlay’s shape and represents the strokes of the path using its current attributes.

You can use this class as-is or subclass it to define additional drawing behaviors. If you subclass it, override the [- createPath](<mkoverlaypathrenderer/createpath().md>) method and use that method to build the appropriate path object. To change the path, invalidate it and recreate the path using the new data your subclass obtains.

## Relationships

- **Inherits From**: [MKOverlayRenderer](mkoverlayrenderer.md)

- **Inherited By**: [MKCircleRenderer](mkcirclerenderer.md), [MKMultiPolygonRenderer](mkmultipolygonrenderer.md), [MKMultiPolylineRenderer](mkmultipolylinerenderer.md), [MKPolygonRenderer](mkpolygonrenderer.md), [MKPolylineRenderer](mkpolylinerenderer.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating and managing the path

- [path](mkoverlaypathrenderer/path.md) — The path representing the overlay’s shape.
- [- createPath](<mkoverlaypathrenderer/createpath().md>) — Creates the path for the overlay.
- [- invalidatePath](<mkoverlaypathrenderer/invalidatepath().md>) — Updates the path associated with the overlay renderer.

### Accessing the drawing attributes

- [fillColor](mkoverlaypathrenderer/fillcolor.md) — The fill color to use for the path.
- [strokeColor](mkoverlaypathrenderer/strokecolor.md) — The stroke color to use for the path.
- [lineWidth](mkoverlaypathrenderer/linewidth.md) — The stroke width to use for the path.
- [lineJoin](mkoverlaypathrenderer/linejoin.md) — The line join style to apply to the corners of the path.
- [lineCap](mkoverlaypathrenderer/linecap.md) — The line cap style to apply to the open ends of the path.
- [miterLimit](mkoverlaypathrenderer/miterlimit.md) — The limiting value that helps avoid spikes at junctions between connected line segments.
- [lineDashPhase](mkoverlaypathrenderer/linedashphase.md) — The offset (in points) at which to start drawing the dash pattern.
- [lineDashPattern](mkoverlaypathrenderer/linedashpattern.md) — An array of numbers specifying the dash pattern to use for the path.

### Drawing the path

- [- applyStrokePropertiesToContext:atZoomScale:](<mkoverlaypathrenderer/applystrokeproperties(to_atzoomscale_).md>) — Applies the renderer’s stroke-related drawing properties to the specified graphics context.
- [- applyFillPropertiesToContext:atZoomScale:](<mkoverlaypathrenderer/applyfillproperties(to_atzoomscale_).md>) — Applies the receiver’s fill-related drawing properties to the specified graphics context.
- [- strokePath:inContext:](<mkoverlaypathrenderer/strokepath(__in_).md>) — Draws a line along the specified path.
- [- fillPath:inContext:](<mkoverlaypathrenderer/fillpath(__in_).md>) — Fills the area that the specified path encloses.
- [shouldRasterize](mkoverlaypathrenderer/shouldrasterize.md) — A Boolean value that determines whether the overlay path renderer renders the overlay as a bitmap before compositing.

## See Also

### Custom shape overlays

- [MKPolygon](mkpolygon.md) — A closed polygon overlay.
- [MKPolygonRenderer](mkpolygonrenderer.md) — The visual representation of a single polygon overlay.
- [MKMultiPolygon](mkmultipolygon.md) — A collection of multiple closed polygon overlays.
- [MKMultiPolygonRenderer](mkmultipolygonrenderer.md) — The visual representation of multiple polygon overlays.
