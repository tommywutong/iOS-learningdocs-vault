---
title: UIGraphicsImageRendererFormat
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigraphicsimagerendererformat
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsimagerendererformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsimagerendererformat.json'
content_hash: 'sha256:e22e172a81437f90'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIGraphicsImageRendererFormat

<sub>Class</sub>

A set of drawing attributes that represents the configuration of an image renderer context.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class UIGraphicsImageRendererFormat
```

## Overview

Use an instance of [UIGraphicsImageRendererFormat](uigraphicsimagerendererformat.md) to initialize a [UIGraphicsImageRenderer](uigraphicsimagerenderer.md) object with nondefault attributes.

The image renderer format object contains properties that determine the attributes of the underlying Core Graphics contexts that the image renderer creates. Use the [+ defaultFormat](<uigraphicsrendererformat/default().md>) class method to create an image renderer format instance optimized for the current device.

## Relationships

- **Inherits From**: [UIGraphicsRendererFormat](uigraphicsrendererformat.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating the renderer

- [+ formatForTraitCollection:](<uigraphicsimagerendererformat/init(for_).md>) — Creates the most suitable format for rendering on a device with the specified traits.

### Configuring the renderer attributes

- [opaque](uigraphicsimagerendererformat/opaque.md) — A Boolean value that indicates whether the underlying Core Graphics context has an alpha channel.
- [scale](uigraphicsimagerendererformat/scale.md) — The display scale of the image renderer context.
- [preferredRange](uigraphicsimagerendererformat/preferredrange.md) — The preferred color range of the image renderer context.
- [Range](uigraphicsimagerendererformat/range.md) — Constants that specify the color range of the image renderer context.
- [prefersExtendedRange](uigraphicsimagerendererformat/prefersextendedrange.md) — A Boolean value that specifies whether the bitmap context uses extended color. _(deprecated)_

### Initializers

- [init(forTraitCollection:)](<uigraphicsimagerendererformat/init(fortraitcollection_).md>)

### Instance Properties

- [supportsHighDynamicRange](uigraphicsimagerendererformat/supportshighdynamicrange.md)

## See Also

### Graphics contexts

- [UIGraphicsRenderer](uigraphicsrenderer.md) — An abstract base class for creating graphics renderers.
- [UIGraphicsRendererContext](uigraphicsrenderercontext.md) — The base class for the drawing environments for graphics renderers.
- [UIGraphicsRendererFormat](uigraphicsrendererformat.md) — A set of drawing attributes that represents the configuration of a graphics renderer context.
- [UIGraphicsImageRenderer](uigraphicsimagerenderer.md) — A graphics renderer for creating Core Graphics-backed images.
- [UIGraphicsImageRendererContext](uigraphicsimagerenderercontext.md) — The drawing environment for an image renderer.
- [UIGraphicsPDFRenderer](uigraphicspdfrenderer.md) — A graphics renderer for creating PDFs.
- [UIGraphicsPDFRendererContext](uigraphicspdfrenderercontext.md) — The drawing environment for a PDF renderer.
- [UIGraphicsPDFRendererFormat](uigraphicspdfrendererformat.md) — A set of drawing attributes that represents the configuration of a PDF renderer context.
