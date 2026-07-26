---
title: 'setObjectBufferOffset(_:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setobjectbufferoffset(_:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setobjectbufferoffset(_:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setobjectbufferoffset%28_%3Aindex%3A%29.json'
content_hash: 'sha256:fce54b66ead67c3f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setObjectBufferOffset(_:index:)

<sub>Instance Method</sub>

Updates an entry in the object shader argument table with a new location within the entry’s current buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setObjectBufferOffset(_ offset: Int, index: Int)
```

## Parameters

- `offset` — An integer that represents the location, in bytes, from the start of `buffer` where the object shader argument data begins. See the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) to check for offset alignment requirements for buffers in `device` and `constant` address space.

- `index` — An integer that represents the entry in the object shader argument table for buffers that already stores a record of an [MTLBuffer](../mtlbuffer.md).

## Discussion

The command this method encodes changes the offset for a mesh buffer that already has a previous assignment from one of your earlier commands.

For more information, see:

- [- setObjectBuffer:offset:atIndex:](<setobjectbuffer(__offset_index_).md>)
- [setObjectBuffers(_:offsets:range:)](<setobjectbuffers(__offsets_range_).md>) (Swift)
- [setObjectBuffers:offsets:withRange:](setobjectbuffers_offsets_withrange_.md) (Objective-C)

The command can also adjust the offset for an entry that you previously set with the [- setObjectBytes:length:atIndex:](<setobjectbytes(__length_index_).md>) method.

> [!tip] Tip
> If you’re only updating an offset, this method is typically more efficient than rebinding a buffer or byte block with the methods above.

## See Also

### Assigning buffers for object shaders

- [- setObjectBuffer:offset:atIndex:](<setobjectbuffer(__offset_index_).md>) — Assigns a buffer to an entry in the object shader argument table.
- [setObjectBuffers(_:offsets:range:)](<setobjectbuffers(__offsets_range_).md>) — Assigns multiple buffers to a range of entries in the object shader argument table.
- [- setObjectBytes:length:atIndex:](<setobjectbytes(__length_index_).md>) — Creates a buffer from bytes and assigns it to an entry in the object shader argument table.
