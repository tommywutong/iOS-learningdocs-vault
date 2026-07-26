---
title: 'setMeshBuffers:offsets:withRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setmeshbuffers:offsets:withrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setmeshbuffers:offsets:withrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setmeshbuffers%3Aoffsets%3Awithrange%3A.json'
content_hash: 'sha256:23d85800a736e9ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setMeshBuffers:offsets:withRange:

<sub>Instance Method</sub>

Assigns multiple buffers to a range of entries in the mesh shader argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setMeshBuffers:(id<MTLBuffer> const[]) buffers offsets:(const NSUInteger[]) offsets withRange:(NSRange) range;
```

## Parameters

- `buffers` — A pointer to a C array of [MTLBuffer](../mtlbuffer.md) instances the command assigns to entries in the mesh shader argument table for buffers.

- `offsets` — A pointer to a C array of unsigned integers. Each element represents the location, in bytes, from the start of the corresponding [MTLBuffer](../mtlbuffer.md) element in `buffers` where the mesh shader argument data begins. See the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) to check for offset alignment requirements for buffers in `device` and `constant` address space.

- `range` — A span of integers that represent the entries in the mesh shader argument table for buffers. Each entry stores a record of the corresponding element in `buffers` and `offsets`.

## Discussion

By default, the texture at each index is `nil`.

> [!note] Note
> The Swift version of this method is [setMeshBuffers(_:offsets:range:)](<setmeshbuffers(__offsets_range_).md>).

## See Also

### Assigning buffers for mesh shaders

- [- setMeshBuffer:offset:atIndex:](<setmeshbuffer(__offset_index_).md>) — Assigns a buffer to an entry in the mesh shader argument table.
- [- setMeshBytes:length:atIndex:](<setmeshbytes(__length_index_).md>) — Creates a buffer from bytes and assigns it to an entry in the mesh shader argument table.
- [- setMeshBufferOffset:atIndex:](<setmeshbufferoffset(__index_).md>) — Updates an entry in the mesh shader argument table with a new location within the entry’s current buffer.
