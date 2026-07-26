---
title: 'getVersion(majorVersion:minorVersion:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgpdfdocument/getversion(majorversion:minorversion:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfdocument/getversion(majorversion:minorversion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfdocument/getversion%28majorversion%3Aminorversion%3A%29.json'
content_hash: 'sha256:8f69291df4f2f4b9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGPDFDocument](../cgpdfdocument.md)

# getVersion(majorVersion:minorVersion:)

<sub>Instance Method</sub>

Returns the major and minor version numbers of a Core Graphics PDF document.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getVersion(majorVersion: UnsafeMutablePointer<Int32>, minorVersion: UnsafeMutablePointer<Int32>)
```

## Parameters

- `majorVersion` — On return, contains the major version number of the document.

- `minorVersion` — On return, contains the minor version number of the document.

## Discussion

On return, the values of the `majorVersion` and `minorVersion` parameters are set to the major and minor version numbers of the document respectively.

## See Also

### Examining a PDF Document

- [CGPDFDocumentGetCatalog](catalog.md) — Returns the document catalog of a Core Graphics PDF document.
- [CGPDFDocumentGetID](fileidentifier.md) — Gets the file identifier for a PDF document.
- [CGPDFDocumentGetInfo](info.md) — Gets the information dictionary for a PDF document.
- [CGPDFDocumentGetNumberOfPages](numberofpages.md) — Returns the number of pages in a PDF document.
- [CGPDFDocumentGetPage](<page(at_).md>) — Returns a page from a Core Graphics PDF document.
