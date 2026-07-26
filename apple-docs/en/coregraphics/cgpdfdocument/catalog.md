---
title: catalog
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpdfdocument/catalog
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfdocument/catalog'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfdocument/catalog.json'
content_hash: 'sha256:2198f07a09ec108e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGPDFDocument](../cgpdfdocument.md)

# catalog

<sub>Instance Property</sub>

Returns the document catalog of a Core Graphics PDF document.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var catalog: CGPDFDictionaryRef? { get }
```

## Discussion

The entries in a PDF document catalog recursively describe the contents of the PDF document. You can access the contents of a PDF document catalog by calling the function [CGPDFDocumentGetCatalog](catalog.md). For information on accessing PDF metadata, see [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066).

## See Also

### Examining a PDF Document

- [CGPDFDocumentGetID](fileidentifier.md) — Gets the file identifier for a PDF document.
- [CGPDFDocumentGetInfo](info.md) — Gets the information dictionary for a PDF document.
- [CGPDFDocumentGetNumberOfPages](numberofpages.md) — Returns the number of pages in a PDF document.
- [CGPDFDocumentGetVersion](<getversion(majorversion_minorversion_).md>) — Returns the major and minor version numbers of a Core Graphics PDF document.
- [CGPDFDocumentGetPage](<page(at_).md>) — Returns a page from a Core Graphics PDF document.
