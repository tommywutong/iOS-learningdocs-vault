---
title: 'setTileBuffers(_:offsets:range:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.5+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/settilebuffers(_:offsets:range:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/settilebuffers(_:offsets:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/settilebuffers%28_%3Aoffsets%3Arange%3A%29.json'
content_hash: 'sha256:02bfd70dbadc529a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setTileBuffers(_:offsets:range:)

<sub>Instance Method</sub>

Assigns multiple buffers to a range of entries in the tile shader argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setTileBuffers(_ buffers: [(any MTLBuffer)?], offsets: [Int], range: Range<Int>)
```

## Parameters

- `buffers` — An array of [MTLBuffer](../mtlbuffer.md) instances the command assigns to entries in the tile shader argument table for buffers.

- `offsets` — An array of integers. Each element represents the location, in bytes, from the start of the corresponding [MTLBuffer](../mtlbuffer.md) element in `buffers` where the tile shader argument data begins. See the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) to check for offset alignment requirements for buffers in `device` and `constant` address space.

- `range` — A span of integers that represent the entries in the tile shader argument table for buffers. Each entry stores a record of the corresponding element in `buffers` and `offsets`.

## Discussion

By default, the buffer at each index is `nil`.

> [!note] Note
> The Objective-C version of this method is [setTileBuffers:offsets:withRange:](settilebuffers_offsets_withrange_.md).

## See Also

### Assigning buffers

- [- setTileBuffer:offset:atIndex:](<settilebuffer(__offset_index_).md>) — Assigns a buffer to an entry in the tile shader argument table.
- [- setTileBytes:length:atIndex:](<settilebytes(__length_index_).md>) — Creates a buffer from bytes and assigns it to an entry in the tile shader argument table.
- [- setTileBufferOffset:atIndex:](<settilebufferoffset(__index_).md>) — Updates an entry in the tile shader argument table with a new location within the entry’s current buffer.
