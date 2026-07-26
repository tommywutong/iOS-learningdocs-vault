---
title: 'setBuffers:offsets:attributeStrides:withRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcomputecommandencoder/setbuffers:offsets:attributestrides:withrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/setbuffers:offsets:attributestrides:withrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputecommandencoder/setbuffers%3Aoffsets%3Aattributestrides%3Awithrange%3A.json'
content_hash: 'sha256:a84dfcb7e8c32076'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md)

# setBuffers:offsets:attributeStrides:withRange:

<sub>Instance Method</sub>

Binds multiple buffers with data in stride to the buffer argument table at once, allowing compute kernels to access their data on the GPU.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setBuffers:(id<MTLBuffer> const[]) buffers offsets:(const NSUInteger[]) offsets attributeStrides:(const NSUInteger[]) strides withRange:(NSRange) range;
```

## Parameters

- `buffers` — The [MTLBuffer](../mtlbuffer.md) instances to bind to the buffer argument table.

- `offsets` — An array of offsets, each of which specifies where the data begins, in bytes, from the start of its corresponding buffer.

- `strides` — An array of strides, each of which specifies the number of bytes between the start of one element and the start of the next for its corresponding buffer.

- `range` — The argument table indices to bind each of the `buffers` to, in the order they appear.

## Discussion

> [!important] Important
> This method requires that the length of `buffers`, `offsets`, and `strides` are all equal to the length of `range`.

For buffers binding to an argument using the `device` address space, align the offset to the data type’s size. The maximum size for an offset is `16` bytes.

For buffers in the `constant` address space, the minimum alignment depends on the hardware running your app. See the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) for information on each Apple GPU family.

Rebinding an already bound buffer causes a Metal error.

## See Also

### Binding buffers

- [- setBuffer:offset:atIndex:](<setbuffer(__offset_index_).md>) — Binds a buffer to the buffer argument table, allowing compute kernels to access its data on the GPU.
- [- setBuffer:offset:attributeStride:atIndex:](<setbuffer(__offset_attributestride_index_).md>) — Binds a buffer with a stride to the buffer argument table, allowing compute kernels to access its data on the GPU.
- [setBuffers:offsets:withRange:](setbuffers_offsets_withrange_.md) — Binds multiple buffers to the buffer argument table at once, allowing compute kernels to access their data on the GPU.
- [- setBufferOffset:atIndex:](<setbufferoffset(__index_).md>) — Changes where the data begins in a buffer already bound to the buffer argument table.
- [- setBufferOffset:attributeStride:atIndex:](<setbufferoffset(offset_attributestride_index_).md>) — Changes where the data begins and the distance between adjacent elements in a buffer already bound to the buffer argument table.
