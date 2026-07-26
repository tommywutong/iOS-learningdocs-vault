---
title: resourceAlias
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4visibilityoptions/resourcealias
source_url: 'https://developer.apple.com/documentation/metal/mtl4visibilityoptions/resourcealias'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4visibilityoptions/resourcealias.json'
content_hash: 'sha256:d240d9f58dc687e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4VisibilityOptions](../mtl4visibilityoptions.md)

# resourceAlias

<sub>Type Property</sub>

Flushes caches to ensure that aliased virtual addresses are memory consistent.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var resourceAlias: MTL4VisibilityOptions { get }
```

## Discussion

On some systems this may be the GPU+CPU (system) memory coherence point and on other systems it may be the GPU (device) memory coherence point.
