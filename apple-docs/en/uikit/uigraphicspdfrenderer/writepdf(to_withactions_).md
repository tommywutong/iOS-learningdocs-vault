---
title: 'writePDF(to:withActions:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigraphicspdfrenderer/writepdf(to:withactions:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicspdfrenderer/writepdf(to:withactions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicspdfrenderer/writepdf%28to%3Awithactions%3A%29.json'
content_hash: 'sha256:13596c96a0d227c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGraphicsPDFRenderer](../uigraphicspdfrenderer.md)

# writePDF(to:withActions:)

<sub>Instance Method</sub>

Creates a PDF from a set of drawing instructions and saves it to a specified URL.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func writePDF(to url: URL, withActions actions: (UIGraphicsPDFRendererContext) -> Void) throws
```

## Parameters

- `url` — The URL where the complete PDF file is saved.

- `actions` — A [DrawingActions](drawingactions.md) closure that, when invoked by the renderer, executes a set of drawing instructions to create the output PDF.

## Discussion

You provide a set of drawing instructions as the block argument to this method, and the method attempts to write the resulting PDF to the supplied URL.

You can call this method repeatedly to create multiple PDFs, each of which has identical dimensions and format.

## See Also

### Managing the PDF data

- [- PDFDataWithActions:](<pdfdata(actions_).md>) — Creates a PDF from a set of drawing instructions and returns it as a data object.
- [DrawingActions](drawingactions.md) — A closure for drawing PDF content.
