---
title: 'CGPDFScannerRelease(_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgpdfscannerrelease(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfscannerrelease(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfscannerrelease%28_%3A%29.json'
content_hash: 'sha256:a8b840fc440fe9df'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFScannerRelease(_:)

<sub>Function</sub>

Decrements the retain count of a scanner object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGPDFScannerRelease(_ scanner: CGPDFScannerRef)
```

## Parameters

- `scanner` — The scanner object to release.

## See Also

### Retaining and Releasing PDF Scanner Objects

- [CGPDFScannerRetain](<cgpdfscannerretain(__).md>) — Increments the retain count of a scanner object.
