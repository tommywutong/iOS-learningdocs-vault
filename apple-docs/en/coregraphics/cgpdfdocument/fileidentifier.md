---
title: fileIdentifier
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpdfdocument/fileidentifier
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfdocument/fileidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfdocument/fileidentifier.json'
content_hash: 'sha256:35280d8ec1ba078d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGPDFDocument](../cgpdfdocument.md)

# fileIdentifier

<sub>Instance Property</sub>

Gets the file identifier for a PDF document.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var fileIdentifier: CGPDFArrayRef? { get }
```

## Discussion

A PDF file identifier is defined in the PDF specification as an array of two strings, the first of which is a permanent identifier that doesn’t change even when the file is updated. The second string changes each time the file is updated. For more information, see _PDF Reference: Version 1.3 (Second Edition)_, Adobe Systems Incorporated.

## See Also

### Examining a PDF Document

- [CGPDFDocumentGetCatalog](catalog.md) — Returns the document catalog of a Core Graphics PDF document.
- [CGPDFDocumentGetInfo](info.md) — Gets the information dictionary for a PDF document.
- [CGPDFDocumentGetNumberOfPages](numberofpages.md) — Returns the number of pages in a PDF document.
- [CGPDFDocumentGetVersion](<getversion(majorversion_minorversion_).md>) — Returns the major and minor version numbers of a Core Graphics PDF document.
- [CGPDFDocumentGetPage](<page(at_).md>) — Returns a page from a Core Graphics PDF document.
