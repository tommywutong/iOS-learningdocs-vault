---
title: closePDF()
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcontext/closepdf()
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/closepdf()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/closepdf%28%29.json'
content_hash: 'sha256:e264683589d7a6bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# closePDF()

<sub>Instance Method</sub>

Closes a PDF document.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func closePDF()
```

## Discussion

After closing the context, all pending data is written to the context destination, and the PDF file is completed. No additional data can be written to the destination context after the PDF document is closed.

## See Also

### Managing a PDF Graphics Context

- [CGPDFContextBeginPage](<beginpdfpage(__).md>) — Begins a new page in a PDF graphics context.
- [CGPDFContextEndPage](<endpdfpage().md>) — Ends the current page in the PDF graphics context.
- [CGPDFContextAddDestinationAtPoint](<adddestination(__at_).md>) — Sets a destination to jump to when a point in the current page of a PDF graphics context is clicked.
- [CGPDFContextSetDestinationForRect](<setdestination(__for_).md>) — Sets a destination to jump to when a rectangle in the current PDF page is clicked.
- [CGPDFContextSetURLForRect](<seturl(__for_).md>) — Sets the URL associated with a rectangle in a PDF graphics context.
- [CGPDFContextAddDocumentMetadata](<adddocumentmetadata(__).md>) — Associates custom metadata with the PDF document.
