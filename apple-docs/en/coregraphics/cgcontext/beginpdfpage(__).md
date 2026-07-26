---
title: 'beginPDFPage(_:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/beginpdfpage(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/beginpdfpage(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/beginpdfpage%28_%3A%29.json'
content_hash: 'sha256:0b34988528cc2550'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# beginPDFPage(_:)

<sub>Instance Method</sub>

Begins a new page in a PDF graphics context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func beginPDFPage(_ pageInfo: CFDictionary?)
```

## Parameters

- `pageInfo` — A dictionary that contains key-value pairs that define the page properties.

## Discussion

You must call the function [CGPDFContextEndPage](<endpdfpage().md>) to signal the end of the page.

## See Also

### Managing a PDF Graphics Context

- [CGPDFContextEndPage](<endpdfpage().md>) — Ends the current page in the PDF graphics context.
- [CGPDFContextAddDestinationAtPoint](<adddestination(__at_).md>) — Sets a destination to jump to when a point in the current page of a PDF graphics context is clicked.
- [CGPDFContextSetDestinationForRect](<setdestination(__for_).md>) — Sets a destination to jump to when a rectangle in the current PDF page is clicked.
- [CGPDFContextSetURLForRect](<seturl(__for_).md>) — Sets the URL associated with a rectangle in a PDF graphics context.
- [CGPDFContextAddDocumentMetadata](<adddocumentmetadata(__).md>) — Associates custom metadata with the PDF document.
- [CGPDFContextClose](<closepdf().md>) — Closes a PDF document.
