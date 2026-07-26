---
title: 'CGPDFScannerScan(_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgpdfscannerscan(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfscannerscan(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfscannerscan%28_%3A%29.json'
content_hash: 'sha256:eb478bcfece1ed2c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFScannerScan(_:)

<sub>Function</sub>

Parses the content stream of a PDF scanner object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGPDFScannerScan(_ scanner: CGPDFScannerRef) -> Bool
```

## Parameters

- `scanner` — The scanner object whose content stream you want to parse.

## Return Value

[true](../swift/true.md) if the entire stream is parsed successfully; [false](../swift/false.md) if parsing fails (for example, if the stream data is corrupted).

## Discussion

The function [CGPDFScannerScan](<cgpdfscannerscan(__).md>) parses the PDF content stream associated with the scanner. Each time Core Graphics parses a PDF operator for which you register a callback, Core Graphics invokes your callback.

## See Also

### Parsing Content

- [CGPDFScannerGetContentStream](<cgpdfscannergetcontentstream(__).md>) — Returns the content stream associated with a PDF scanner object.
