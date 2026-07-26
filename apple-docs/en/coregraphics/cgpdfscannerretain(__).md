---
title: 'CGPDFScannerRetain(_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgpdfscannerretain(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfscannerretain(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfscannerretain%28_%3A%29.json'
content_hash: 'sha256:f621bbee5193ae9e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFScannerRetain(_:)

<sub>Function</sub>

Increments the retain count of a scanner object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGPDFScannerRetain(_ scanner: CGPDFScannerRef) -> CGPDFScannerRef
```

## Parameters

- `scanner` — The scanner object to retain.

## Return Value

The same scanner object passed to the function in the `scanner` parameter.

## See Also

### Retaining and Releasing PDF Scanner Objects

- [CGPDFScannerRelease](<cgpdfscannerrelease(__).md>) — Decrements the retain count of a scanner object.
