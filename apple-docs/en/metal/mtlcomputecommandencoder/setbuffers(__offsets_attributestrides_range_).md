---
title: 'setBuffers(_:offsets:attributeStrides:range:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcomputecommandencoder/setbuffers(_:offsets:attributestrides:range:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/setbuffers(_:offsets:attributestrides:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputecommandencoder/setbuffers%28_%3Aoffsets%3Aattributestrides%3Arange%3A%29.json'
content_hash: 'sha256:9ab5cfaa868f9f2a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md)

# setBuffers(_:offsets:attributeStrides:range:)

<sub>Instance Method</sub>

Binds multiple buffers with data in stride to the buffer argument table at once, allowing compute kernels to access their data on the GPU.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setBuffers(_ buffers: [(any MTLBuffer)?], offsets: [Int], attributeStrides: [Int], range: Range<Int>)
```

## Parameters

- `buffers` — The [MTLBuffer](../mtlbuffer.md) instances to bind to the buffer argument table.

- `offsets` — An array of offsets, each of which specifies where the data begins, in bytes, from the start of its corresponding buffer.

- `attributeStrides` — An array of strides, each of which specifies the number of bytes between the start of one element and the start of the next for its corresponding buffer.

- `range` — The argument table indicies to bind each of the `buffers` to, in the order they appear.

## Discussion

> [!important] Important
> This method requires that the length of `buffers`, `offsets`, and `attributeStrides` are all equal to the length of `range`.

For buffers binding to an argument using the `device` address space, align the offset to the data type’s size. The maximum size for an offset is `16` bytes.

For buffers in the `constant` address space, the minimum alignment depends on the hardware running your app. See the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) for information on each Apple GPU family.

Rebinding an already bound buffer causes a Metal error.

## See Also

### Binding buffers

- [- setBuffer:offset:atIndex:](<setbuffer(__offset_index_).md>) — Binds a buffer to the buffer argument table, allowing compute kernels to access its data on the GPU.
- [- setBuffer:offset:attributeStride:atIndex:](<setbuffer(__offset_attributestride_index_).md>) — Binds a buffer with a stride to the buffer argument table, allowing compute kernels to access its data on the GPU.
- [setBuffers(_:offsets:range:)](<setbuffers(__offsets_range_).md>) — Binds multiple buffers to the buffer argument table at once, allowing compute kernels to access their data on the GPU.
- [- setBufferOffset:atIndex:](<setbufferoffset(__index_).md>) — Changes where the data begins in a buffer already bound to the buffer argument table.
- [- setBufferOffset:attributeStride:atIndex:](<setbufferoffset(offset_attributestride_index_).md>) — Changes where the data begins and the distance between adjacent elements in a buffer already bound to the buffer argument table.
