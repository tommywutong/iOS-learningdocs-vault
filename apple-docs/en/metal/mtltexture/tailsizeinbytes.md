---
title: tailSizeInBytes
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltexture/tailsizeinbytes
source_url: 'https://developer.apple.com/documentation/metal/mtltexture/tailsizeinbytes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltexture/tailsizeinbytes.json'
content_hash: 'sha256:51ff2d22227c2404'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTexture](../mtltexture.md)

# tailSizeInBytes

<sub>Instance Property</sub>

The size of the sparse texture tail, in bytes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var tailSizeInBytes: Int { get }
```

<sub>Mac Catalyst, macOS</sub>

```swift
optional var tailSizeInBytes: Int { get }
```

## See Also

### Querying sparse properties

- [isSparse](issparse.md) — A Boolean value that indicates whether this is a sparse texture.
- [firstMipmapInTail](firstmipmapintail.md) — The index of the first mipmap in the tail.
