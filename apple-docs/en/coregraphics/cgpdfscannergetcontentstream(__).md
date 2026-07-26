---
title: 'CGPDFScannerGetContentStream(_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgpdfscannergetcontentstream(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfscannergetcontentstream(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfscannergetcontentstream%28_%3A%29.json'
content_hash: 'sha256:23fc6143af4ebac0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFScannerGetContentStream(_:)

<sub>Function</sub>

Returns the content stream associated with a PDF scanner object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGPDFScannerGetContentStream(_ scanner: CGPDFScannerRef) -> CGPDFContentStreamRef
```

## Parameters

- `scanner` — The scanner object whose content stream you want to obtain.

## Return Value

The content stream associated with `scanner`.

## See Also

### Parsing Content

- [CGPDFScannerScan](<cgpdfscannerscan(__).md>) — Parses the content stream of a PDF scanner object.
