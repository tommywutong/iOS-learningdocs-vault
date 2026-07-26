---
title: UIGraphicsRendererContext
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigraphicsrenderercontext
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsrenderercontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsrenderercontext.json'
content_hash: 'sha256:f99f7ffbf390e649'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIGraphicsRendererContext

<sub>Class</sub>

The base class for the drawing environments for graphics renderers.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class UIGraphicsRendererContext
```

## Overview

You don’t create instances of [UIGraphicsRendererContext](uigraphicsrenderercontext.md) yourself. Instead, when you use a concrete subclass of [UIGraphicsRenderer](uigraphicsrenderer.md), you are provided an instance of the appropriate [UIGraphicsRendererContext](uigraphicsrenderercontext.md) subclass—either [UIGraphicsImageRendererContext](uigraphicsimagerenderercontext.md) or [UIGraphicsPDFRendererContext](uigraphicspdfrenderercontext.md)—as an argument to a [UIGraphicsDrawingActions](uigraphicsdrawingactions.md) drawing actions block.

[UIGraphicsRendererContext](uigraphicsrenderercontext.md) objects provide high-level drawing methods in addition to access to the underlying Core Graphics context.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [UIGraphicsImageRendererContext](uigraphicsimagerenderercontext.md), [UIGraphicsPDFRendererContext](uigraphicspdfrenderercontext.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Getting the drawing context

- [CGContext](uigraphicsrenderercontext/cgcontext.md) — The underlying Core Graphics context.
- [format](uigraphicsrenderercontext/format.md) — The format used to create the associated graphics renderer.

### Drawing content

- [- strokeRect:](<uigraphicsrenderercontext/stroke(__).md>) — Paints a rectangular path using the currently selected stroke color.
- [- strokeRect:blendMode:](<uigraphicsrenderercontext/stroke(__blendmode_).md>) — Paints a rectangular path using the currently selected stroke color and specified blend mode.
- [- fillRect:blendMode:](<uigraphicsrenderercontext/fill(__blendmode_).md>) — Paints a rectangular area with the currently selected fill color using the supplied blend mode.
- [- fillRect:](<uigraphicsrenderercontext/fill(__).md>) — Paints a rectangular area with the currently selected fill color.

### Applying a clipping rectangle

- [- clipToRect:](<uigraphicsrenderercontext/clip(to_).md>) — Sets the clipping mask for the drawing context to the specified rectangle.

## See Also

### Graphics contexts

- [UIGraphicsRenderer](uigraphicsrenderer.md) — An abstract base class for creating graphics renderers.
- [UIGraphicsRendererFormat](uigraphicsrendererformat.md) — A set of drawing attributes that represents the configuration of a graphics renderer context.
- [UIGraphicsImageRenderer](uigraphicsimagerenderer.md) — A graphics renderer for creating Core Graphics-backed images.
- [UIGraphicsImageRendererContext](uigraphicsimagerenderercontext.md) — The drawing environment for an image renderer.
- [UIGraphicsImageRendererFormat](uigraphicsimagerendererformat.md) — A set of drawing attributes that represents the configuration of an image renderer context.
- [UIGraphicsPDFRenderer](uigraphicspdfrenderer.md) — A graphics renderer for creating PDFs.
- [UIGraphicsPDFRendererContext](uigraphicspdfrenderercontext.md) — The drawing environment for a PDF renderer.
- [UIGraphicsPDFRendererFormat](uigraphicspdfrendererformat.md) — A set of drawing attributes that represents the configuration of a PDF renderer context.
