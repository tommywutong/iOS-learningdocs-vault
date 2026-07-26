---
title: CGPDFPageRelease
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpdfpagerelease
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfpagerelease'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfpagerelease.json'
content_hash: 'sha256:8313c084110211fe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFPageRelease

<sub>Function</sub>

Decrements the retain count of a PDF page.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void CGPDFPageRelease(CGPDFPageRef page);
```

## Parameters

- `page` — A PDF page.

## Discussion

This function is equivalent to [CFRelease](../corefoundation/cfrelease.md), except that it does not cause an error if the `page` parameter is `NULL`.

## See Also

### Retaining and Releasing a PDF Page

- [CGPDFPageRetain](cgpdfpageretain.md) — Increments the retain count of a PDF page.
