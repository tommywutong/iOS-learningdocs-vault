---
title: unspecialized
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcolorwritemask/unspecialized
source_url: 'https://developer.apple.com/documentation/metal/mtlcolorwritemask/unspecialized'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcolorwritemask/unspecialized.json'
content_hash: 'sha256:1003ca76516369cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLColorWriteMask](../mtlcolorwritemask.md)

# unspecialized

<sub>Type Property</sub>

Defers assigning the color write mask.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var unspecialized: MTLColorWriteMask { get }
```

## Discussion

Until you specialize this value in the pipeline state, it behaves as `MTLColorWriteMaskAll`.
