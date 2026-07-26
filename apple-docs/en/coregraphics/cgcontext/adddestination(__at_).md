---
title: 'addDestination(_:at:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/adddestination(_:at:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/adddestination(_:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/adddestination%28_%3Aat%3A%29.json'
content_hash: 'sha256:a25fb7f0beeb6a4b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# addDestination(_:at:)

<sub>Instance Method</sub>

Sets a destination to jump to when a point in the current page of a PDF graphics context is clicked.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addDestination(_ name: CFString, at point: CGPoint)
```

## Parameters

- `name` — A destination name.

- `point` — A location in the current page of the PDF graphics context.

## See Also

### Managing a PDF Graphics Context

- [CGPDFContextBeginPage](<beginpdfpage(__).md>) — Begins a new page in a PDF graphics context.
- [CGPDFContextEndPage](<endpdfpage().md>) — Ends the current page in the PDF graphics context.
- [CGPDFContextSetDestinationForRect](<setdestination(__for_).md>) — Sets a destination to jump to when a rectangle in the current PDF page is clicked.
- [CGPDFContextSetURLForRect](<seturl(__for_).md>) — Sets the URL associated with a rectangle in a PDF graphics context.
- [CGPDFContextAddDocumentMetadata](<adddocumentmetadata(__).md>) — Associates custom metadata with the PDF document.
- [CGPDFContextClose](<closepdf().md>) — Closes a PDF document.
