---
title: CGPDFOperatorCallback
framework: Core Graphics
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpdfoperatorcallback
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfoperatorcallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfoperatorcallback.json'
content_hash: 'sha256:5d440b8bebb8f4da'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFOperatorCallback

<sub>Type Alias</sub>

Performs custom processing for PDF operators.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CGPDFOperatorCallback = (CGPDFScannerRef, UnsafeMutableRawPointer?) -> Void
```

## Parameters

- `scanner` — A CGPDFScanner object. Core Graphics passes the scanner to your callback function. The scanner contains the PDF content stream that has the PDF operator that corresponds to this callback.

- `info` — A pointer to data passed to the callback.

## Discussion

Your callback function takes any action that’s appropriate for your application. For example, if you want to count the number of inline images in a PDF but ignore the image data, you would set a callback for the `EI` operator. In your callback you would increment a counter for each call.
