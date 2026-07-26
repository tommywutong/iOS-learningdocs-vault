---
title: 'setTileBytes(_:length:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/settilebytes(_:length:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/settilebytes(_:length:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/settilebytes%28_%3Alength%3Aindex%3A%29.json'
content_hash: 'sha256:c44aa021d54ee114'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setTileBytes(_:length:index:)

<sub>Instance Method</sub>

Creates a buffer from bytes and assigns it to an entry in the tile shader argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setTileBytes(_ bytes: UnsafeRawPointer, length: Int, index: Int)
```

## Parameters

- `bytes` — A pointer to argument data the method copies to an [MTLBuffer](../mtlbuffer.md) and assigns to an entry in the tile shader argument table for buffers.

- `length` — The number of bytes the method copies from the `bytes` pointer.

- `index` — An integer that represents the entry in the tile shader argument table for buffers that stores a record of the [MTLBuffer](../mtlbuffer.md) the method creates from `bytes`.

## Discussion

The method is equivalent to creating an [MTLBuffer](../mtlbuffer.md) instance that contains the same data as `bytes` and calling the [- setTileBuffer:offset:atIndex:](<settilebuffer(__offset_index_).md>) method. However, this method avoids the overhead of creating a buffer to store your data; instead, Metal manages the data.

> [!important] Important
> Only call this method for single-use data that’s smaller than 4 KB.

For data that’s more than 4 KB, create an [MTLBuffer](../mtlbuffer.md) instance and pass it to [- setTileBuffer:offset:atIndex:](<settilebuffer(__offset_index_).md>).

By default, the buffer at each index is `nil`.

## See Also

### Assigning buffers

- [- setTileBuffer:offset:atIndex:](<settilebuffer(__offset_index_).md>) — Assigns a buffer to an entry in the tile shader argument table.
- [setTileBuffers(_:offsets:range:)](<settilebuffers(__offsets_range_).md>) — Assigns multiple buffers to a range of entries in the tile shader argument table.
- [- setTileBufferOffset:atIndex:](<settilebufferoffset(__index_).md>) — Updates an entry in the tile shader argument table with a new location within the entry’s current buffer.
