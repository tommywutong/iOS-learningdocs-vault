---
title: 'setBufferOffset(_:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.3+, iPadOS 8.3+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcomputecommandencoder/setbufferoffset(_:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/setbufferoffset(_:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputecommandencoder/setbufferoffset%28_%3Aindex%3A%29.json'
content_hash: 'sha256:5a016a28e3fffb50'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md)

# setBufferOffset(_:index:)

<sub>Instance Method</sub>

Changes where the data begins in a buffer already bound to the buffer argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setBufferOffset(_ offset: Int, index: Int)
```

## Parameters

- `offset` — Where the data to bind begins, in bytes, from the start of the bound buffer.

- `index` — The argument table entry to change.

## Discussion

Prefer calling this method to unbinding and then rebinding data.

For buffers binding to an argument using the `device` address space, align the offset to the data type’s size. The maximum size for an offset is `16` bytes.

For buffers in the `constant` address space, the minimum alignment depends on the hardware running your app. See the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) for information on each Apple GPU family.

## See Also

### Binding buffers

- [- setBuffer:offset:atIndex:](<setbuffer(__offset_index_).md>) — Binds a buffer to the buffer argument table, allowing compute kernels to access its data on the GPU.
- [- setBuffer:offset:attributeStride:atIndex:](<setbuffer(__offset_attributestride_index_).md>) — Binds a buffer with a stride to the buffer argument table, allowing compute kernels to access its data on the GPU.
- [setBuffers(_:offsets:range:)](<setbuffers(__offsets_range_).md>) — Binds multiple buffers to the buffer argument table at once, allowing compute kernels to access their data on the GPU.
- [setBuffers(_:offsets:attributeStrides:range:)](<setbuffers(__offsets_attributestrides_range_).md>) — Binds multiple buffers with data in stride to the buffer argument table at once, allowing compute kernels to access their data on the GPU.
- [- setBufferOffset:attributeStride:atIndex:](<setbufferoffset(offset_attributestride_index_).md>) — Changes where the data begins and the distance between adjacent elements in a buffer already bound to the buffer argument table.
