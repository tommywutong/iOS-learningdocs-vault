---
title: UIGraphicsRendererFormat
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigraphicsrendererformat
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsrendererformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsrendererformat.json'
content_hash: 'sha256:29dd3b7e786070ca'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIGraphicsRendererFormat

<sub>Class</sub>

A set of drawing attributes that represents the configuration of a graphics renderer context.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class UIGraphicsRendererFormat
```

## Overview

Create a [UIGraphicsRendererFormat](uigraphicsrendererformat.md) object, or one of its subclasses ([UIGraphicsImageRendererFormat](uigraphicsimagerendererformat.md) and [UIGraphicsPDFRendererFormat](uigraphicspdfrendererformat.md)), and use it to construct a graphics renderer by providing the format object as a parameter in a [UIGraphicsRenderer](uigraphicsrenderer.md) subclass intializer.

The graphics renderer uses the format object you provided to configure any context objects ([UIGraphicsRendererContext](uigraphicsrenderercontext.md)) it creates as part of the rendering process.

If you use a graphics renderer initializer that doesn’t require a format argument, the renderer creates a format object using the [+ defaultFormat](<uigraphicsrendererformat/default().md>) class method.

The renderer format object contains properties that represent the immutable aspects of the renderer’s configuration. This means that repeated uses of a single graphics renderer object will always use the same format object.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [UIGraphicsImageRendererFormat](uigraphicsimagerendererformat.md), [UIGraphicsPDFRendererFormat](uigraphicspdfrendererformat.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a format

- [+ defaultFormat](<uigraphicsrendererformat/default().md>) — Returns a format that represents the highest fidelity that the current device supports.
- [+ preferredFormat](<uigraphicsrendererformat/preferred().md>) — Returns the most suitable format for the main screen’s current configuration.

### Getting the bounds

- [bounds](uigraphicsrendererformat/bounds.md) — The bounds of the graphics context.

## See Also

### Graphics contexts

- [UIGraphicsRenderer](uigraphicsrenderer.md) — An abstract base class for creating graphics renderers.
- [UIGraphicsRendererContext](uigraphicsrenderercontext.md) — The base class for the drawing environments for graphics renderers.
- [UIGraphicsImageRenderer](uigraphicsimagerenderer.md) — A graphics renderer for creating Core Graphics-backed images.
- [UIGraphicsImageRendererContext](uigraphicsimagerenderercontext.md) — The drawing environment for an image renderer.
- [UIGraphicsImageRendererFormat](uigraphicsimagerendererformat.md) — A set of drawing attributes that represents the configuration of an image renderer context.
- [UIGraphicsPDFRenderer](uigraphicspdfrenderer.md) — A graphics renderer for creating PDFs.
- [UIGraphicsPDFRendererContext](uigraphicspdfrenderercontext.md) — The drawing environment for a PDF renderer.
- [UIGraphicsPDFRendererFormat](uigraphicspdfrendererformat.md) — A set of drawing attributes that represents the configuration of a PDF renderer context.
