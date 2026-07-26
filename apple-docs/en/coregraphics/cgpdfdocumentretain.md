---
title: CGPDFDocumentRetain
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpdfdocumentretain
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfdocumentretain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfdocumentretain.json'
content_hash: 'sha256:16830b097401b897'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFDocumentRetain

<sub>Function</sub>

Increments the retain count of a Core Graphics PDF document.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern CGPDFDocumentRefCGPDFDocumentRetain(CGPDFDocumentRef document);
```

## Parameters

- `document` — The PDF document to retain.

## Return Value

The same document you passed in as the `document` parameter.

## Discussion

This function is equivalent to [CFRetain](../corefoundation/cfretain.md), except that it does not cause an error if the `document` parameter is `NULL`.

## See Also

### Retaining and Releasing PDF Documents

- [CGPDFDocumentRelease](cgpdfdocumentrelease.md) — Decrements the retain count of a PDF document.
