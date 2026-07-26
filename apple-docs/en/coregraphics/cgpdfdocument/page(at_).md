---
title: 'page(at:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgpdfdocument/page(at:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfdocument/page(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfdocument/page%28at%3A%29.json'
content_hash: 'sha256:e786f1d325a5a0c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGPDFDocument](../cgpdfdocument.md)

# page(at:)

<sub>Instance Method</sub>

Returns a page from a Core Graphics PDF document.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func page(at pageNumber: Int) -> CGPDFPage?
```

## Parameters

- `pageNumber` — The number of the page requested.

## Return Value

Return the PDF page corresponding to the specified page number, or `NULL` if no such page exists in the document. Pages are numbered starting at 1.

## See Also

### Examining a PDF Document

- [CGPDFDocumentGetCatalog](catalog.md) — Returns the document catalog of a Core Graphics PDF document.
- [CGPDFDocumentGetID](fileidentifier.md) — Gets the file identifier for a PDF document.
- [CGPDFDocumentGetInfo](info.md) — Gets the information dictionary for a PDF document.
- [CGPDFDocumentGetNumberOfPages](numberofpages.md) — Returns the number of pages in a PDF document.
- [CGPDFDocumentGetVersion](<getversion(majorversion_minorversion_).md>) — Returns the major and minor version numbers of a Core Graphics PDF document.
