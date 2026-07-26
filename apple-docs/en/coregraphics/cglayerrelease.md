---
title: CGLayerRelease
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cglayerrelease
source_url: 'https://developer.apple.com/documentation/coregraphics/cglayerrelease'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cglayerrelease.json'
content_hash: 'sha256:7a849d2208a5e742'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGLayerRelease

<sub>Function</sub>

Decrements the retain count of a layer object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void CGLayerRelease(CGLayerRef layer);
```

## Parameters

- `layer` — The layer to release.

## Discussion

This function is equivalent to calling [CFRelease](../corefoundation/cfrelease.md) except that it does not crash if the `layer` parameter is `null`.

## See Also

### Retaining and Releasing Color Objects

- [CGLayerRetain](cglayerretain.md) — Increments the retain count of a layer object.
