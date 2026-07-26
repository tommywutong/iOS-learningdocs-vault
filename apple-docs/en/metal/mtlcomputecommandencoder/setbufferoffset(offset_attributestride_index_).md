---
title: 'setBufferOffset(offset:attributeStride:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcomputecommandencoder/setbufferoffset(offset:attributestride:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/setbufferoffset(offset:attributestride:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputecommandencoder/setbufferoffset%28offset%3Aattributestride%3Aindex%3A%29.json'
content_hash: 'sha256:80a35b4c8dbd8680'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md)

# setBufferOffset(offset:attributeStride:index:)

<sub>Instance Method</sub>

Changes where the data begins and the distance between adjacent elements in a buffer already bound to the buffer argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setBufferOffset(offset: Int, attributeStride stride: Int, index: Int)
```

## Parameters

- `offset` — Where the data to bind begins, in bytes, from the start of the bound buffer.

- `stride` — The number of bytes between the start of one element and the start of the next.

- `index` — The index of the buffer to change in the argument table.

## Discussion

> [!important] Important
> Only call this method when the buffer is part of [stageInputDescriptor](../mtlcomputepipelinedescriptor/stageinputdescriptor.md) and has its stride set to [MTLBufferLayoutStrideDynamic](../mtlbufferlayoutstridedynamic.md).

_ _Prefer calling this method to unbinding and then rebinding data.

For buffers binding to an argument using the `device` address space, align the offset to the data type’s size. The maximum size for an offset is `16` bytes.

For buffers in the `constant` address space, the minimum alignment depends on the hardware running your app. See the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) for information on each Apple GPU family.

## See Also

### Binding buffers

- [- setBuffer:offset:atIndex:](<setbuffer(__offset_index_).md>) — Binds a buffer to the buffer argument table, allowing compute kernels to access its data on the GPU.
- [- setBuffer:offset:attributeStride:atIndex:](<setbuffer(__offset_attributestride_index_).md>) — Binds a buffer with a stride to the buffer argument table, allowing compute kernels to access its data on the GPU.
- [setBuffers(_:offsets:range:)](<setbuffers(__offsets_range_).md>) — Binds multiple buffers to the buffer argument table at once, allowing compute kernels to access their data on the GPU.
- [setBuffers(_:offsets:attributeStrides:range:)](<setbuffers(__offsets_attributestrides_range_).md>) — Binds multiple buffers with data in stride to the buffer argument table at once, allowing compute kernels to access their data on the GPU.
- [- setBufferOffset:atIndex:](<setbufferoffset(__index_).md>) — Changes where the data begins in a buffer already bound to the buffer argument table.
