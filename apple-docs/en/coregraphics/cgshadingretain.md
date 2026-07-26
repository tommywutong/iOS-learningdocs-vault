---
title: CGShadingRetain
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgshadingretain
source_url: 'https://developer.apple.com/documentation/coregraphics/cgshadingretain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgshadingretain.json'
content_hash: 'sha256:643173a1433b2154'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGShadingRetain

<sub>Function</sub>

Increments the retain count of a shading object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern CGShadingRefCGShadingRetain(CGShadingRef shading);
```

## Parameters

- `shading` — The shading object to retain.

## Return Value

The same shading object you passed in as the `shading` parameter.

## Discussion

This function is equivalent to [CFRetain](../corefoundation/cfretain.md), except that it does not cause an error if the `shading` parameter is `NULL`.

## See Also

### Retaining and Releasing Shading Objects

- [CGShadingRelease](cgshadingrelease.md) — Decrements the retain count of a shading object.
