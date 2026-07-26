---
title: 'CGPDFContentStreamRetain(_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgpdfcontentstreamretain(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfcontentstreamretain(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfcontentstreamretain%28_%3A%29.json'
content_hash: 'sha256:62d55e80286086bf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFContentStreamRetain(_:)

<sub>Function</sub>

Increments the retain count of a PDF content stream object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGPDFContentStreamRetain(_ cs: CGPDFContentStreamRef) -> CGPDFContentStreamRef
```

## Parameters

- `cs` — A PDF content stream object.

## Return Value

The same PDF content stream you passed in as the `cs` parameter.

## See Also

### Retaining and Releasing a PDF Content Stream Object

- [CGPDFContentStreamRelease](<cgpdfcontentstreamrelease(__).md>) — Decrements the retain count of a PDF content stream object.
