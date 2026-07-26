---
title: 'addDocumentMetadata(_:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/adddocumentmetadata(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/adddocumentmetadata(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/adddocumentmetadata%28_%3A%29.json'
content_hash: 'sha256:8d103bd1ae083bef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# addDocumentMetadata(_:)

<sub>Instance Method</sub>

Associates custom metadata with the PDF document.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addDocumentMetadata(_ metadata: CFData?)
```

## Parameters

- `metadata` — A stream of XML data that is formatted according to the Extensible Metadata Platform, as described in section 10.2.2., “Metadata Streams”, of the PDF 1.7 specification.

## See Also

### Managing a PDF Graphics Context

- [CGPDFContextBeginPage](<beginpdfpage(__).md>) — Begins a new page in a PDF graphics context.
- [CGPDFContextEndPage](<endpdfpage().md>) — Ends the current page in the PDF graphics context.
- [CGPDFContextAddDestinationAtPoint](<adddestination(__at_).md>) — Sets a destination to jump to when a point in the current page of a PDF graphics context is clicked.
- [CGPDFContextSetDestinationForRect](<setdestination(__for_).md>) — Sets a destination to jump to when a rectangle in the current PDF page is clicked.
- [CGPDFContextSetURLForRect](<seturl(__for_).md>) — Sets the URL associated with a rectangle in a PDF graphics context.
- [CGPDFContextClose](<closepdf().md>) — Closes a PDF document.
