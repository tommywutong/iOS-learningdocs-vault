---
title: firstMipmapInTail
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltexture/firstmipmapintail
source_url: 'https://developer.apple.com/documentation/metal/mtltexture/firstmipmapintail'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltexture/firstmipmapintail.json'
content_hash: 'sha256:8ee9d8d83cc1037a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTexture](../mtltexture.md)

# firstMipmapInTail

<sub>Instance Property</sub>

The index of the first mipmap in the tail.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var firstMipmapInTail: Int { get }
```

<sub>Mac Catalyst, macOS</sub>

```swift
optional var firstMipmapInTail: Int { get }
```

## Discussion

In a sparse texture, the _tail_ is a collection of mipmaps at higher index values that are mapped as a single block of memory. When you map this mipmap into your sparse texture, Metal also maps mipmap levels with larger index values.

## See Also

### Querying sparse properties

- [isSparse](issparse.md) — A Boolean value that indicates whether this is a sparse texture.
- [tailSizeInBytes](tailsizeinbytes.md) — The size of the sparse texture tail, in bytes.
