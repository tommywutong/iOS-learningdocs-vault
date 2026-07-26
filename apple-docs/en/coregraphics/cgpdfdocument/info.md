---
title: info
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpdfdocument/info
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfdocument/info'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfdocument/info.json'
content_hash: 'sha256:7b15778122d9a68e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGPDFDocument](../cgpdfdocument.md)

# info

<sub>Instance Property</sub>

Gets the information dictionary for a PDF document.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var info: CGPDFDictionaryRef? { get }
```

## See Also

### Examining a PDF Document

- [CGPDFDocumentGetCatalog](catalog.md) — Returns the document catalog of a Core Graphics PDF document.
- [CGPDFDocumentGetID](fileidentifier.md) — Gets the file identifier for a PDF document.
- [CGPDFDocumentGetNumberOfPages](numberofpages.md) — Returns the number of pages in a PDF document.
- [CGPDFDocumentGetVersion](<getversion(majorversion_minorversion_).md>) — Returns the major and minor version numbers of a Core Graphics PDF document.
- [CGPDFDocumentGetPage](<page(at_).md>) — Returns a page from a Core Graphics PDF document.
