---
title: 'setMeshBytes(_:length:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setmeshbytes(_:length:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setmeshbytes(_:length:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setmeshbytes%28_%3Alength%3Aindex%3A%29.json'
content_hash: 'sha256:af706fb658b32ab5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setMeshBytes(_:length:index:)

<sub>Instance Method</sub>

Creates a buffer from bytes and assigns it to an entry in the mesh shader argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setMeshBytes(_ bytes: UnsafeRawPointer, length: Int, index: Int)
```

## Parameters

- `bytes` — A pointer to argument data the method copies to an [MTLBuffer](../mtlbuffer.md) and assigns to an entry in the mesh shader argument table for buffers.

- `length` — The number of bytes the method copies from the `bytes` pointer.

- `index` — An integer that represents the entry in the mesh shader argument table for buffers that stores a record of the [MTLBuffer](../mtlbuffer.md) the method creates from `bytes`.

## Discussion

The method is equivalent to creating an [MTLBuffer](../mtlbuffer.md) instance that contains the same data as `bytes` and calling the [- setMeshBuffer:offset:atIndex:](<setmeshbuffer(__offset_index_).md>) method. However, this method avoids the overhead of creating a buffer to store your data; instead, Metal manages the data.

> [!important] Important
> Only call this method for single-use data that’s smaller than 4 KB.

For data that’s more than 4 KB, create an [MTLBuffer](../mtlbuffer.md) instance and pass it to [- setMeshBufferOffset:atIndex:](<setmeshbufferoffset(__index_).md>).

## See Also

### Assigning buffers for mesh shaders

- [- setMeshBuffer:offset:atIndex:](<setmeshbuffer(__offset_index_).md>) — Assigns a buffer to an entry in the mesh shader argument table.
- [setMeshBuffers(_:offsets:range:)](<setmeshbuffers(__offsets_range_).md>) — Assigns multiple buffers to a range of entries in the mesh shader argument table.
- [- setMeshBufferOffset:atIndex:](<setmeshbufferoffset(__index_).md>) — Updates an entry in the mesh shader argument table with a new location within the entry’s current buffer.
