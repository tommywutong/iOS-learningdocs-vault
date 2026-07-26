---
title: CGLayerRetain
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cglayerretain
source_url: 'https://developer.apple.com/documentation/coregraphics/cglayerretain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cglayerretain.json'
content_hash: 'sha256:7076b4e075065adb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGLayerRetain

<sub>Function</sub>

Increments the retain count of a layer object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern CGLayerRefCGLayerRetain(CGLayerRef layer);
```

## Parameters

- `layer` — The layer to retain.

## Return Value

The same layer you passed in as the `layer` parameter.

## Discussion

This function is equivalent to calling [CFRetain](../corefoundation/cfretain.md) except that it does not crash if the `layer` parameter is `null`.

## See Also

### Retaining and Releasing Color Objects

- [CGLayerRelease](cglayerrelease.md) — Decrements the retain count of a layer object.
