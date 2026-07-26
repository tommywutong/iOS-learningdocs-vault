---
title: 'setTileBuffer(_:offset:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/settilebuffer(_:offset:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/settilebuffer(_:offset:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/settilebuffer%28_%3Aoffset%3Aindex%3A%29.json'
content_hash: 'sha256:14c9aac2be26650d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setTileBuffer(_:offset:index:)

<sub>Instance Method</sub>

Assigns a buffer to an entry in the tile shader argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setTileBuffer(_ buffer: (any MTLBuffer)?, offset: Int, index: Int)
```

## Parameters

- `buffer` — An [MTLBuffer](../mtlbuffer.md) instance the command assigns to an entry in the tile shader argument table for buffers.

- `offset` — An integer that represents the location, in bytes, from the start of `buffer` where the tile shader argument data begins. See the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) to check for offset alignment requirements for buffers in `device` and `constant` address space.

- `index` — An integer that represents the entry in the tile shader argument table for buffers that stores a record of `buffer` and `offset`.

## Discussion

By default, the buffer at each index is `nil`.

## See Also

### Assigning buffers

- [setTileBuffers(_:offsets:range:)](<settilebuffers(__offsets_range_).md>) — Assigns multiple buffers to a range of entries in the tile shader argument table.
- [- setTileBytes:length:atIndex:](<settilebytes(__length_index_).md>) — Creates a buffer from bytes and assigns it to an entry in the tile shader argument table.
- [- setTileBufferOffset:atIndex:](<settilebufferoffset(__index_).md>) — Updates an entry in the tile shader argument table with a new location within the entry’s current buffer.
