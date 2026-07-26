---
title: CGPDFDocumentRelease
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpdfdocumentrelease
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfdocumentrelease'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfdocumentrelease.json'
content_hash: 'sha256:e393509fe0c87d2b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFDocumentRelease

<sub>Function</sub>

Decrements the retain count of a PDF document.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void CGPDFDocumentRelease(CGPDFDocumentRef document);
```

## Parameters

- `document` — The PDF document to release.

## Discussion

This function is equivalent to [CFRelease](../corefoundation/cfrelease.md), except that it does not cause an error if the `document` parameter is `NULL`.

## See Also

### Retaining and Releasing PDF Documents

- [CGPDFDocumentRetain](cgpdfdocumentretain.md) — Increments the retain count of a Core Graphics PDF document.
