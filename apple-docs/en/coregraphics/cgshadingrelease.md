---
title: CGShadingRelease
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgshadingrelease
source_url: 'https://developer.apple.com/documentation/coregraphics/cgshadingrelease'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgshadingrelease.json'
content_hash: 'sha256:a2f0d831e31627f3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGShadingRelease

<sub>Function</sub>

Decrements the retain count of a shading object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void CGShadingRelease(CGShadingRef shading);
```

## Parameters

- `shading` — The shading object to release.

## Discussion

This function is equivalent to [CFRelease](../corefoundation/cfrelease.md), except that it does not cause an error if the `shading` parameter is `NULL`.

## See Also

### Retaining and Releasing Shading Objects

- [CGShadingRetain](cgshadingretain.md) — Increments the retain count of a shading object.
