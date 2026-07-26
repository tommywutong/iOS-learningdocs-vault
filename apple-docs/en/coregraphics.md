---
title: Core Graphics
framework: Core Graphics
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics
source_url: 'https://developer.apple.com/documentation/coregraphics'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics.json'
content_hash: 'sha256:e5a8688fa890ca40'
translated: false
---

> Navigation: [Technologies](technologies.md)

# Core Graphics

<sub>Framework</sub>

Harness the power of Quartz technology to perform lightweight 2D rendering with high-fidelity output. Handle path-based drawing, antialiased rendering, gradients, images, color management, PDF documents, and more.

## Overview

The Core Graphics framework is based on the Quartz advanced drawing engine. It provides low-level, lightweight 2D rendering with unmatched output fidelity. You use this framework to handle path-based drawing, transformations, color management, offscreen rendering, patterns, gradients and shadings, image data management, image creation, and image masking, as well as PDF document creation, display, and parsing.

In macOS, Core Graphics also includes services for working with display hardware, low-level user input events, and the windowing system.

## Topics

### Geometric Data Types

- [CGFloat](corefoundation/cgfloat-swift.struct.md) — The basic type for floating-point scalar values in Core Graphics and related frameworks.
- [CGPoint](corefoundation/cgpoint.md)
- [CGSize](corefoundation/cgsize.md) — A structure that contains width and height values.
- [CGRect](corefoundation/cgrect.md)
- [CGVector](corefoundation/cgvector.md) — A structure that contains a two-dimensional vector.
- [CGAffineTransform](corefoundation/cgaffinetransform.md)

### 2D Drawing

- [CGContext](coregraphics/cgcontext.md) — A Quartz 2D drawing environment.
- [CGImage](coregraphics/cgimage.md) — A bitmap image or image mask.
- [CGPath](coregraphics/cgpath.md) — An immutable graphics path: a mathematical description of shapes or lines to be drawn in a graphics context.
- [CGMutablePath](coregraphics/cgmutablepath.md) — A mutable graphics path: a mathematical description of shapes or lines to be drawn in a graphics context.
- [CGLayer](coregraphics/cglayer.md) — An offscreen context for reusing content drawn with Core Graphics.

### Colors and Fonts

- [CGColor](coregraphics/cgcolor.md) — A set of components that define a color, with a color space specifying how to interpret them.
- [CGColorConversionInfo](coregraphics/cgcolorconversioninfo.md) — An object that describes how to convert between color spaces for use by other system services.
- [CGColorSpace](coregraphics/cgcolorspace.md) — A profile that specifies how to interpret a color value for display.
- [CGFont](coregraphics/cgfont.md) — A set of character glyphs and layout information for drawing text.

### Working with PDF Documents

- [CGPDFDocument](coregraphics/cgpdfdocument.md) — A document that contains PDF (Portable Document Format) drawing information.

### Utility and Support Classes

- [CGDataConsumer](coregraphics/cgdataconsumer.md) — An abstraction for data-writing tasks that eliminates the need to manage a raw memory buffer.
- [CGDataProvider](coregraphics/cgdataprovider.md) — An abstraction for data-reading tasks that eliminates the need to manage a raw memory buffer.
- [CGShading](coregraphics/cgshading.md) — A definition for a smooth transition between colors, controlled by a custom function you provide, for drawing radial and axial gradient fills.
- [CGGradient](coregraphics/cggradient.md) — A definition for a smooth transition between colors for drawing radial and axial gradient fills.
- [CGFunction](coregraphics/cgfunction.md) — A general facility for defining and using callback functions.
- [CGPattern](coregraphics/cgpattern.md) — A 2D pattern to be used for drawing graphics paths.

### Services

- [Quartz Display Services](coregraphics/quartz-display-services.md) — Provides direct access to features in the macOS window server for configuring and controlling display hardware.
- [Quartz Event Services](coregraphics/quartz-event-services.md) — Provides features for managing _event taps_—filters for observing and altering the stream of low-level user input events in macOS.
- [Quartz Window Services](coregraphics/quartz-window-services.md) — Provides information about the windows managed by the macOS window server.

### Reference

- [Core Graphics Structures](coregraphics/core-graphics-structures.md)
- [Core Graphics Enumerations](coregraphics/core-graphics-enumerations.md)
- [Core Graphics Constants](coregraphics/core-graphics-constants.md)
- [Core Graphics Functions](coregraphics/core-graphics-functions.md)
- [Core Graphics Data Types](coregraphics/core-graphics-data-types.md)

### Classes

- [CGRenderingBufferProvider](coregraphics/cgrenderingbufferprovider.md)

### Structures

- [CGBitmapParameters](coregraphics/cgbitmapparameters-4v8wo.md)
- [CGColorModel](coregraphics/cgcolormodel.md)
- [CGContentInfo](coregraphics/cgcontentinfo.md)

### Enumerations

- [CGBitmapLayout](coregraphics/cgbitmaplayout.md)
- [CGComponent](coregraphics/cgcomponent.md)
- [CGContentToneMappingInfo](coregraphics/cgcontenttonemappinginfo-swift.enum.md)
- [CGImageComponentInfo](coregraphics/cgimagecomponentinfo.md)

## See Also

### Related Documentation

- [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)
