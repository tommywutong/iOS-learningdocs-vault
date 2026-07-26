---
title: CGPattern
framework: Core Graphics
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpattern
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpattern'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpattern.json'
content_hash: 'sha256:02b1e91daa7656fd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPattern

<sub>Class</sub>

A 2D pattern to be used for drawing graphics paths.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CGPattern
```

## Overview

Core Graphics tiles the pattern cell for you, based on parameters you specify when you call [CGPatternCreate](<cgpattern/init(info_bounds_matrix_xstep_ystep_tiling_iscolored_callbacks_).md>).

To create a dashed line, see [CGContextSetLineDash](cgcontextsetlinedash.md).

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating a Pattern

- [CGPatternCreate](<cgpattern/init(info_bounds_matrix_xstep_ystep_tiling_iscolored_callbacks_).md>) — Creates a pattern object.

### Callbacks

- [CGPatternCallbacks](cgpatterncallbacks.md) — A structure that holds a version and two callback functions for drawing a custom pattern.
- [CGPatternDrawPatternCallback](cgpatterndrawpatterncallback.md) — Draws a pattern cell.
- [CGPatternReleaseInfoCallback](cgpatternreleaseinfocallback.md) — Release private data or resources associated with the pattern.

### Constants

- [CGPatternTiling](cgpatterntiling.md) — Different methods for rendering a tiled pattern.

### Working with Core Foundation Types

- [CGPatternGetTypeID](cgpattern/typeid.md) — Returns the type identifier for Core Graphics patterns.

## See Also

### Related Documentation

- [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)

### Utility and Support Classes

- [CGDataConsumer](cgdataconsumer.md) — An abstraction for data-writing tasks that eliminates the need to manage a raw memory buffer.
- [CGDataProvider](cgdataprovider.md) — An abstraction for data-reading tasks that eliminates the need to manage a raw memory buffer.
- [CGShading](cgshading.md) — A definition for a smooth transition between colors, controlled by a custom function you provide, for drawing radial and axial gradient fills.
- [CGGradient](cggradient.md) — A definition for a smooth transition between colors for drawing radial and axial gradient fills.
- [CGFunction](cgfunction.md) — A general facility for defining and using callback functions.
