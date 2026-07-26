---
title: 'setFragmentBufferOffset(_:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.3+, iPadOS 8.3+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setfragmentbufferoffset(_:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setfragmentbufferoffset(_:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setfragmentbufferoffset%28_%3Aindex%3A%29.json'
content_hash: 'sha256:766ae95dad6901f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setFragmentBufferOffset(_:index:)

<sub>Instance Method</sub>

Updates an entry in the fragment shader argument table with a new location within the entry’s current buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setFragmentBufferOffset(_ offset: Int, index: Int)
```

## Parameters

- `offset` — An integer that represents the location, in bytes, from the start of `buffer` where the fragment shader argument data begins. See the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) to check for offset alignment requirements for buffers in `device` and `constant` address space.

- `index` — An integer that represents the entry in the fragment shader argument table for buffers that already stores a record of an [MTLBuffer](../mtlbuffer.md).

## Discussion

The command this method encodes changes the offset for a fragment buffer that already has a previous assignment from one of your earlier commands.

For more information, see:

- [- setFragmentBuffer:offset:atIndex:](<setfragmentbuffer(__offset_index_).md>)
- [setFragmentBuffers(_:offsets:range:)](<setfragmentbuffers(__offsets_range_).md>) (Swift)
- [setFragmentBuffers:offsets:withRange:](setfragmentbuffers_offsets_withrange_.md) (Objective-C)

The command can also adjust the offset for an entry that you previously set with the [- setFragmentBytes:length:atIndex:](<setfragmentbytes(__length_index_).md>) method.

> [!tip] Tip
> If you’re only updating an offset, this method is typically more efficient than rebinding a buffer or byte block with the methods above.

By default, the buffer at each index is `nil`.

## See Also

### Assigning buffers

- [- setFragmentBuffer:offset:atIndex:](<setfragmentbuffer(__offset_index_).md>) — Assigns a buffer to an entry in the fragment shader argument table.
- [setFragmentBuffers(_:offsets:range:)](<setfragmentbuffers(__offsets_range_).md>) — Assigns multiple buffers to a range of entries in the fragment shader argument table.
- [- setFragmentBytes:length:atIndex:](<setfragmentbytes(__length_index_).md>) — Creates a buffer from bytes and assigns it to an entry in the fragment shader argument table.
