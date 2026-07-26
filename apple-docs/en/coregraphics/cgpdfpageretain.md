---
title: CGPDFPageRetain
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpdfpageretain
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfpageretain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfpageretain.json'
content_hash: 'sha256:9baa796d39616ab3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFPageRetain

<sub>Function</sub>

Increments the retain count of a PDF page.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern CGPDFPageRefCGPDFPageRetain(CGPDFPageRef page);
```

## Parameters

- `page` — A PDF page.

## Return Value

The same page you passed in as the `page` parameter.

## Discussion

This function is equivalent to [CFRetain](../corefoundation/cfretain.md), except that it does not cause an error if the `page` parameter is `NULL`.

## See Also

### Retaining and Releasing a PDF Page

- [CGPDFPageRelease](cgpdfpagerelease.md) — Decrements the retain count of a PDF page.
