---
title: 'setTileBuffers:offsets:withRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.5+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/settilebuffers:offsets:withrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/settilebuffers:offsets:withrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/settilebuffers%3Aoffsets%3Awithrange%3A.json'
content_hash: 'sha256:0571c7c9f5a05c9b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setTileBuffers:offsets:withRange:

<sub>Instance Method</sub>

Assigns multiple buffers to a range of entries in the tile shader argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setTileBuffers:(id<MTLBuffer> const[]) buffers offsets:(const NSUInteger[]) offsets withRange:(NSRange) range;
```

## Parameters

- `buffers` — A pointer to a C array of [MTLBuffer](../mtlbuffer.md) instances the command assigns to entries in the tile shader argument table for buffers.

- `offsets` — A pointer to a C array of unsigned integers. Each element represents the location, in bytes, from the start of the corresponding [MTLBuffer](../mtlbuffer.md) element in `buffers` where the tile shader argument data begins. See the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) to check for offset alignment requirements for buffers in `device` and `constant` address space.

- `range` — A span of integers that represent the entries in the tile shader argument table for buffers. Each entry stores a record of the corresponding element in `buffers` and `offsets`.

## Discussion

By default, the buffer at each index is `nil`.

> [!note] Note
> The Swift version of this method is [setTileBuffers(_:offsets:range:)](<settilebuffers(__offsets_range_).md>).

## See Also

### Assigning buffers

- [- setTileBuffer:offset:atIndex:](<settilebuffer(__offset_index_).md>) — Assigns a buffer to an entry in the tile shader argument table.
- [- setTileBytes:length:atIndex:](<settilebytes(__length_index_).md>) — Creates a buffer from bytes and assigns it to an entry in the tile shader argument table.
- [- setTileBufferOffset:atIndex:](<settilebufferoffset(__index_).md>) — Updates an entry in the tile shader argument table with a new location within the entry’s current buffer.
