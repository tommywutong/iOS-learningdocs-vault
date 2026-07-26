---
title: 'setMeshBufferOffset(_:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setmeshbufferoffset(_:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setmeshbufferoffset(_:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setmeshbufferoffset%28_%3Aindex%3A%29.json'
content_hash: 'sha256:77056ca4b1b8e902'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setMeshBufferOffset(_:index:)

<sub>Instance Method</sub>

Updates an entry in the mesh shader argument table with a new location within the entry’s current buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setMeshBufferOffset(_ offset: Int, index: Int)
```

## Parameters

- `offset` — An integer that represents the location, in bytes, from the start of `buffer` where the mesh shader argument data begins. See the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) to check for offset alignment requirements for buffers in `device` and `constant` address space.

- `index` — An integer that represents the entry in the mesh shader argument table for buffers that already stores a record of an [MTLBuffer](../mtlbuffer.md).

## Discussion

The command this method encodes changes the offset for a mesh buffer that already has a previous assignment from one of your earlier commands.

For more information, see:

- [- setMeshBuffer:offset:atIndex:](<setmeshbuffer(__offset_index_).md>)
- [setMeshBuffers(_:offsets:range:)](<setmeshbuffers(__offsets_range_).md>) (Swift)
- [setMeshBuffers:offsets:withRange:](setmeshbuffers_offsets_withrange_.md) (Objective-C)

The command can also adjust the offset for an entry that you previously set with the [- setMeshBytes:length:atIndex:](<setmeshbytes(__length_index_).md>) method.

> [!tip] Tip
> If you’re only updating an offset, this method is typically more efficient than rebinding a buffer or byte block with the methods above.

## See Also

### Assigning buffers for mesh shaders

- [- setMeshBuffer:offset:atIndex:](<setmeshbuffer(__offset_index_).md>) — Assigns a buffer to an entry in the mesh shader argument table.
- [setMeshBuffers(_:offsets:range:)](<setmeshbuffers(__offsets_range_).md>) — Assigns multiple buffers to a range of entries in the mesh shader argument table.
- [- setMeshBytes:length:atIndex:](<setmeshbytes(__length_index_).md>) — Creates a buffer from bytes and assigns it to an entry in the mesh shader argument table.
