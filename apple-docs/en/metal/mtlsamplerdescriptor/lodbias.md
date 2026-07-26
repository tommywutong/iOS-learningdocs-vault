---
title: lodBias
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlsamplerdescriptor/lodbias
source_url: 'https://developer.apple.com/documentation/metal/mtlsamplerdescriptor/lodbias'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlsamplerdescriptor/lodbias.json'
content_hash: 'sha256:886b04ea37f5c0a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLSamplerDescriptor](../mtlsamplerdescriptor.md)

# lodBias

<sub>Instance Property</sub>

Sets the level-of-detail (lod) bias when sampling from a texture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var lodBias: Float { get set }
```

## Discussion

The property’s default value is `0.0f`. The precision format is `S4.6`, and the range is `[-16.0, 15.999]`.
