---
title: 'pdfData(actions:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigraphicspdfrenderer/pdfdata(actions:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicspdfrenderer/pdfdata(actions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicspdfrenderer/pdfdata%28actions%3A%29.json'
content_hash: 'sha256:d3dfb688cac3f8ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGraphicsPDFRenderer](../uigraphicspdfrenderer.md)

# pdfData(actions:)

<sub>Instance Method</sub>

Creates a PDF from a set of drawing instructions and returns it as a data object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func pdfData(actions: (UIGraphicsPDFRendererContext) -> Void) -> Data
```

## Parameters

- `actions` — A [DrawingActions](drawingactions.md) block that, when invoked by the renderer, executes a set of drawing instructions to create the output PDF.

## Return Value

A [Data](../../foundation/data.md) object that contains the encoded PDF.

## Discussion

You provide a set of drawing instructions as the block argument to this method, and the method returns the resulting PDF encoded in a [Data](../../foundation/data.md) object.

You can call this method repeatedly to create multiple PDFs, each of which has identical dimensions and format.

## See Also

### Managing the PDF data

- [- writePDFToURL:withActions:error:](<writepdf(to_withactions_).md>) — Creates a PDF from a set of drawing instructions and saves it to a specified URL.
- [DrawingActions](drawingactions.md) — A closure for drawing PDF content.
