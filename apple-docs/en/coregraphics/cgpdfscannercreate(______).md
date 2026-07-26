---
title: 'CGPDFScannerCreate(_:_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgpdfscannercreate(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfscannercreate(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfscannercreate%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:e18f8f89d0c5f02e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFScannerCreate(_:_:_:)

<sub>Function</sub>

Creates a PDF scanner.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGPDFScannerCreate(_ cs: CGPDFContentStreamRef, _ table: CGPDFOperatorTableRef?, _ info: UnsafeMutableRawPointer?) -> CGPDFScannerRef
```

## Parameters

- `cs` — A PDF content stream object. (See [CGPDFContentStream](cgpdfcontentstream.md).)

- `table` — A table of callbacks for the PDF operators you want to handle.

- `info` — A pointer to data you want passed to your callback function. (See [CGPDFOperatorTable](cgpdfoperatortable.md).)

## Return Value

A PDF scanner object. In Objective-C, you’re responsible for releasing this object by calling the function [CGPDFScannerRelease](<cgpdfscannerrelease(__).md>).

## Discussion

When you want to parse the contents of the PDF stream, call the function [CGPDFScannerScan](<cgpdfscannerscan(__).md>).
