---
title: 'setBuffer(_:offset:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcomputecommandencoder/setbuffer(_:offset:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/setbuffer(_:offset:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputecommandencoder/setbuffer%28_%3Aoffset%3Aindex%3A%29.json'
content_hash: 'sha256:64aa1b7aeacd5147'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md)

# setBuffer(_:offset:index:)

<sub>Instance Method</sub>

Binds a buffer to the buffer argument table, allowing compute kernels to access its data on the GPU.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setBuffer(_ buffer: (any MTLBuffer)?, offset: Int, index: Int)
```

## Parameters

- `buffer` — The [MTLBuffer](../mtlbuffer.md) instance to bind to the argument table.

- `offset` — The number of bytes to skip in the buffer before the first element of data.

- `index` — The index the buffer binds to in the argument table.

## Discussion

For buffers binding to an argument using the `device` address space, align the offset to the data type’s size. The maximum size for an offset is `16` bytes.

For buffers in the `constant` address space, the minimum alignment depends on the hardware running your app. See the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) for information on each Apple GPU family.

Rebinding an already bound buffer causes a Metal error.

## See Also

### Binding buffers

- [- setBuffer:offset:attributeStride:atIndex:](<setbuffer(__offset_attributestride_index_).md>) — Binds a buffer with a stride to the buffer argument table, allowing compute kernels to access its data on the GPU.
- [setBuffers(_:offsets:range:)](<setbuffers(__offsets_range_).md>) — Binds multiple buffers to the buffer argument table at once, allowing compute kernels to access their data on the GPU.
- [setBuffers(_:offsets:attributeStrides:range:)](<setbuffers(__offsets_attributestrides_range_).md>) — Binds multiple buffers with data in stride to the buffer argument table at once, allowing compute kernels to access their data on the GPU.
- [- setBufferOffset:atIndex:](<setbufferoffset(__index_).md>) — Changes where the data begins in a buffer already bound to the buffer argument table.
- [- setBufferOffset:attributeStride:atIndex:](<setbufferoffset(offset_attributestride_index_).md>) — Changes where the data begins and the distance between adjacent elements in a buffer already bound to the buffer argument table.
