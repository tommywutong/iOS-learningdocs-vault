---
title: UIGraphicsPDFRendererContext
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigraphicspdfrenderercontext
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicspdfrenderercontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicspdfrenderercontext.json'
content_hash: 'sha256:351766b92adf146f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIGraphicsPDFRendererContext

<sub>Class</sub>

The drawing environment for a PDF renderer.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class UIGraphicsPDFRendererContext
```

## Overview

When using the [UIGraphicsPDFRenderer](uigraphicspdfrenderer.md) drawing methods, you must pass a block of type [DrawingActions](uigraphicspdfrenderer/drawingactions.md) as an argument, which provides a [UIGraphicsPDFRendererContext](uigraphicspdfrenderercontext.md) instance as an argument. Use the context object to access high-level drawing functions and the underlying Core Graphics context.

> [!note] Note
> [UIGraphicsPDFRendererContext](uigraphicspdfrenderercontext.md) inherits much of its functionality from its abstract superclass [UIGraphicsRendererContext](uigraphicsrenderercontext.md).

To learn how to use a [UIGraphicsPDFRendererContext](uigraphicspdfrenderercontext.md) object in combination with a PDF renderer, see [Creating a graphics PDF renderer](uigraphicspdfrenderer.md#Creating-a-graphics-PDF-renderer).

## Relationships

- **Inherits From**: [UIGraphicsRendererContext](uigraphicsrenderercontext.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Marking new pages

- [- beginPage](<uigraphicspdfrenderercontext/beginpage().md>) — Marks the beginning of a new page in the PDF context and configures it using default values.
- [- beginPageWithBounds:pageInfo:](<uigraphicspdfrenderercontext/beginpage(withbounds_pageinfo_).md>) — Marks the beginning of a new page in the PDF context and configures it using the specified values.

### Getting the PDF bounds

- [pdfContextBounds](uigraphicspdfrenderercontext/pdfcontextbounds.md) — The bounds of the PDF context for the current page.

### Managing destinations

- [- addDestinationWithName:atPoint:](<uigraphicspdfrenderercontext/adddestination(withname_at_).md>) — Creates a named destination point in the current PDF page.
- [- setDestinationWithName:forRect:](<uigraphicspdfrenderercontext/setdestinationwithname(__for_).md>) — Creates a link rectangle in the current page that jumps the PDF viewer to the named destination when clicked.
- [- setURL:forRect:](<uigraphicspdfrenderercontext/seturl(__for_).md>) — Creates a link to an external resource defined by a URL

## See Also

### Graphics contexts

- [UIGraphicsRenderer](uigraphicsrenderer.md) — An abstract base class for creating graphics renderers.
- [UIGraphicsRendererContext](uigraphicsrenderercontext.md) — The base class for the drawing environments for graphics renderers.
- [UIGraphicsRendererFormat](uigraphicsrendererformat.md) — A set of drawing attributes that represents the configuration of a graphics renderer context.
- [UIGraphicsImageRenderer](uigraphicsimagerenderer.md) — A graphics renderer for creating Core Graphics-backed images.
- [UIGraphicsImageRendererContext](uigraphicsimagerenderercontext.md) — The drawing environment for an image renderer.
- [UIGraphicsImageRendererFormat](uigraphicsimagerendererformat.md) — A set of drawing attributes that represents the configuration of an image renderer context.
- [UIGraphicsPDFRenderer](uigraphicspdfrenderer.md) — A graphics renderer for creating PDFs.
- [UIGraphicsPDFRendererFormat](uigraphicspdfrendererformat.md) — A set of drawing attributes that represents the configuration of a PDF renderer context.
