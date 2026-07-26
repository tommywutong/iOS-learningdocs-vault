---
title: 'setBytes(_:length:attributeStride:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcomputecommandencoder/setbytes(_:length:attributestride:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/setbytes(_:length:attributestride:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputecommandencoder/setbytes%28_%3Alength%3Aattributestride%3Aindex%3A%29.json'
content_hash: 'sha256:56b535638bc4fcb9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md)

# setBytes(_:length:attributeStride:index:)

<sub>Instance Method</sub>

Copies data with a given stride directly to the GPU to populate an entry in the buffer argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setBytes(_ bytes: UnsafeRawPointer, length: Int, attributeStride stride: Int, index: Int)
```

## Parameters

- `bytes` — A pointer to the memory where the data to copy starts.

- `length` — The number of bytes to copy.

- `stride` — The number of bytes between the start of one element and the start of the next.

- `index` — The index the data binds to in the argument table.

## Discussion

> [!important] Important
> This method only works for data smaller than 4 kilobytes that doesn’t persist. Create an [MTLBuffer](../mtlbuffer.md) instance if your data exceeds 4 KB, needs to persist on the GPU, or you access results on the CPU.

This method allows Metal to copy data directly onto the GPU, rather than creating a new [MTLBuffer](../mtlbuffer.md) instance and binding it. Binding data directly can improve performance, especially when making many small allocations.

## See Also

### Binding raw bytes

- [- setBytes:length:atIndex:](<setbytes(__length_index_).md>) — Copies data directly to the GPU to populate an entry in the buffer argument table.
