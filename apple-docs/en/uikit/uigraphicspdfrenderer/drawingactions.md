---
title: UIGraphicsPDFRenderer.DrawingActions
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigraphicspdfrenderer/drawingactions
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicspdfrenderer/drawingactions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicspdfrenderer/drawingactions.json'
content_hash: 'sha256:ad85283c2bd126ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGraphicsPDFRenderer](../uigraphicspdfrenderer.md)

# UIGraphicsPDFRenderer.DrawingActions

<sub>Type Alias</sub>

A closure for drawing PDF content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
typealias DrawingActions = (UIGraphicsPDFRendererContext) -> Void
```

## Discussion

`UIGraphicsPDFDrawingActions` defines a block type that takes a [UIGraphicsPDFRendererContext](../uigraphicspdfrenderercontext.md) object as an argument and has no return value.

You provide a block of this type as an argument to the PDF drawing methods on [UIGraphicsPDFRenderer](../uigraphicspdfrenderer.md). Your block should use the provided PDF renderer context to perform the drawing operations you want the renderer to execute.

See [Creating a PDF with a PDF renderer](../uigraphicspdfrenderer.md#Creating-a-PDF-with-a-PDF-renderer) for an example use of a `UIGraphicsPDFDrawingActions` block.

## See Also

### Managing the PDF data

- [- PDFDataWithActions:](<pdfdata(actions_).md>) — Creates a PDF from a set of drawing instructions and returns it as a data object.
- [- writePDFToURL:withActions:error:](<writepdf(to_withactions_).md>) — Creates a PDF from a set of drawing instructions and saves it to a specified URL.
