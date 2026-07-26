---
title: isSparse
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltexture/issparse
source_url: 'https://developer.apple.com/documentation/metal/mtltexture/issparse'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltexture/issparse.json'
content_hash: 'sha256:67b51b53bca85e0f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTexture](../mtltexture.md)

# isSparse

<sub>Instance Property</sub>

A Boolean value that indicates whether this is a sparse texture.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isSparse: Bool { get }
```

<sub>Mac Catalyst, macOS</sub>

```swift
optional var isSparse: Bool { get }
```

## See Also

### Querying sparse properties

- [firstMipmapInTail](firstmipmapintail.md) — The index of the first mipmap in the tail.
- [tailSizeInBytes](tailsizeinbytes.md) — The size of the sparse texture tail, in bytes.
