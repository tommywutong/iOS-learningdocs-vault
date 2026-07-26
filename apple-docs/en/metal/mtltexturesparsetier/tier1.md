---
title: MTLTextureSparseTier.tier1
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltexturesparsetier/tier1
source_url: 'https://developer.apple.com/documentation/metal/mtltexturesparsetier/tier1'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltexturesparsetier/tier1.json'
content_hash: 'sha256:1f4e2e21a253bbc3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTextureSparseTier](../mtltexturesparsetier.md)

# MTLTextureSparseTier.tier1

<sub>Case</sub>

Indicates support for sparse textures tier 1.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case tier1
```

## Discussion

Tier 1 sparse textures allow the following:

- Partial memory backing at sparse tile granularity.
- Defined behavior for accessing an unbacked texture region.
- Shader feedback on texture access to determine memory backing.

An unbacked texture region indicates a region within the texture that doesn’t have memory backing at a given point in time. Accessing an unbacked texture region produces the following results:

- Reading returns zero (transparent black) for pixel formats with an alpha (A) channel.
- Reading return zero in RGB and one in alpha (A) channels (opaque black) otherwise.
- Writing produces no result.
