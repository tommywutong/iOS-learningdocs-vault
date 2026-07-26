---
title: CGShading
framework: Core Graphics
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgshading
source_url: 'https://developer.apple.com/documentation/coregraphics/cgshading'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgshading.json'
content_hash: 'sha256:8a4e6a5a6e892834'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGShading

<sub>Class</sub>

A definition for a smooth transition between colors, controlled by a custom function you provide, for drawing radial and axial gradient fills.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CGShading
```

## Overview

Shading means to fill using a smooth transition between colors across an area. You create a shading using a custom function with a [CGFunction](cgfunction.md) instance. To paint with a Core Graphics shading, you call [CGContextDrawShading](<cgcontext/drawshading(__).md>). This function fills the current clipping path using the specified color gradient, calling your parametric function repeatedly as it draws.

An alternative to using a `CGShading` instance is to use the [CGGradient](cggradient.md) type. For applications that run in macOS 10.5 and later, `CGGradient` objects are much simpler to use.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating Shading Objects

- [CGShadingCreateAxial](<cgshading/init(axialspace_start_end_function_extendstart_extendend_).md>) — Creates a shading object to use for axial shading.
- [CGShadingCreateRadial](<cgshading/init(radialspace_start_startradius_end_endradius_function_extendstart_extendend_).md>) — Creates a shading object to use for radial shading.

### Working with Core Foundation Types

- [CGShadingGetTypeID](cgshading/typeid.md) — Returns the Core Foundation type identifier for Core Graphics shading objects.

### Initializers

- [CGShadingCreateAxialWithContentHeadroom](<cgshading/init(axialheadroom_space_start_end_function_extendstart_extendend_).md>)
- [CGShadingCreateRadialWithContentHeadroom](<cgshading/init(radialheadroom_space_start_startradius_end_endradius_function_extendstart_extendend_).md>)

### Instance Properties

- [CGShadingGetContentHeadroom](cgshading/contentheadroom.md)

## See Also

### Related Documentation

- [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)

### Utility and Support Classes

- [CGDataConsumer](cgdataconsumer.md) — An abstraction for data-writing tasks that eliminates the need to manage a raw memory buffer.
- [CGDataProvider](cgdataprovider.md) — An abstraction for data-reading tasks that eliminates the need to manage a raw memory buffer.
- [CGGradient](cggradient.md) — A definition for a smooth transition between colors for drawing radial and axial gradient fills.
- [CGFunction](cgfunction.md) — A general facility for defining and using callback functions.
- [CGPattern](cgpattern.md) — A 2D pattern to be used for drawing graphics paths.
