---
title: 'setURL(_:for:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/seturl(_:for:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/seturl(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/seturl%28_%3Afor%3A%29.json'
content_hash: 'sha256:c7e2fa39c62f2f87'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# setURL(_:for:)

<sub>Instance Method</sub>

Sets the URL associated with a rectangle in a PDF graphics context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setURL(_ url: CFURL, for rect: CGRect)
```

## Parameters

- `url` — A URL that specifies the destination of the contents associated with the rectangle.

- `rect` — A rectangle specified in default user space (not device space).

## See Also

### Managing a PDF Graphics Context

- [CGPDFContextBeginPage](<beginpdfpage(__).md>) — Begins a new page in a PDF graphics context.
- [CGPDFContextEndPage](<endpdfpage().md>) — Ends the current page in the PDF graphics context.
- [CGPDFContextAddDestinationAtPoint](<adddestination(__at_).md>) — Sets a destination to jump to when a point in the current page of a PDF graphics context is clicked.
- [CGPDFContextSetDestinationForRect](<setdestination(__for_).md>) — Sets a destination to jump to when a rectangle in the current PDF page is clicked.
- [CGPDFContextAddDocumentMetadata](<adddocumentmetadata(__).md>) — Associates custom metadata with the PDF document.
- [CGPDFContextClose](<closepdf().md>) — Closes a PDF document.
