---
title: UIGraphicsImageRendererContext
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigraphicsimagerenderercontext
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsimagerenderercontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsimagerenderercontext.json'
content_hash: 'sha256:9858dadb89acd591'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIGraphicsImageRendererContext

<sub>Class</sub>

The drawing environment for an image renderer.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class UIGraphicsImageRendererContext
```

## Overview

When using the [UIGraphicsImageRenderer](uigraphicsimagerenderer.md) drawing methods, you must pass a block of type [DrawingActions](uigraphicsimagerenderer/drawingactions.md) as an argument, which provides a [UIGraphicsImageRendererContext](uigraphicsimagerenderercontext.md) instance as an argument. Use the context object to access high-level drawing functions and the underlying Core Graphics context.

> [!note] Note
> `UIGraphicsImageRendererContext` inherits much of its functionality from its abstract superclass [UIGraphicsRendererContext](uigraphicsrenderercontext.md).

To learn how to use a `UIGraphicsImageRendererContext` object in combination with an image renderer, see [Creating a graphics image renderer](uigraphicsimagerenderer.md#Creating-a-graphics-image-renderer).

## Relationships

- **Inherits From**: [UIGraphicsRendererContext](uigraphicsrenderercontext.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the image

- [currentImage](uigraphicsimagerenderercontext/currentimage.md) — The current state of the drawing context, expressed as an object that manages image data in your app.

### Getting the image drawing actions

- [DrawingActions](uigraphicsimagerenderer/drawingactions.md) — A closure for drawing an image.

## See Also

### Graphics contexts

- [UIGraphicsRenderer](uigraphicsrenderer.md) — An abstract base class for creating graphics renderers.
- [UIGraphicsRendererContext](uigraphicsrenderercontext.md) — The base class for the drawing environments for graphics renderers.
- [UIGraphicsRendererFormat](uigraphicsrendererformat.md) — A set of drawing attributes that represents the configuration of a graphics renderer context.
- [UIGraphicsImageRenderer](uigraphicsimagerenderer.md) — A graphics renderer for creating Core Graphics-backed images.
- [UIGraphicsImageRendererFormat](uigraphicsimagerendererformat.md) — A set of drawing attributes that represents the configuration of an image renderer context.
- [UIGraphicsPDFRenderer](uigraphicspdfrenderer.md) — A graphics renderer for creating PDFs.
- [UIGraphicsPDFRendererContext](uigraphicspdfrenderercontext.md) — The drawing environment for a PDF renderer.
- [UIGraphicsPDFRendererFormat](uigraphicspdfrendererformat.md) — A set of drawing attributes that represents the configuration of a PDF renderer context.
