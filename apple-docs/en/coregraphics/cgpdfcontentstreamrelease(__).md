---
title: 'CGPDFContentStreamRelease(_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgpdfcontentstreamrelease(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfcontentstreamrelease(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfcontentstreamrelease%28_%3A%29.json'
content_hash: 'sha256:e718f786d23a35c1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFContentStreamRelease(_:)

<sub>Function</sub>

Decrements the retain count of a PDF content stream object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGPDFContentStreamRelease(_ cs: CGPDFContentStreamRef)
```

## Parameters

- `cs` — A PDF content stream.

## See Also

### Retaining and Releasing a PDF Content Stream Object

- [CGPDFContentStreamRetain](<cgpdfcontentstreamretain(__).md>) — Increments the retain count of a PDF content stream object.
