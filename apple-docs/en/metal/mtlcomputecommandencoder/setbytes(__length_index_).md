---
title: 'setBytes(_:length:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.3+, iPadOS 8.3+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcomputecommandencoder/setbytes(_:length:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/setbytes(_:length:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputecommandencoder/setbytes%28_%3Alength%3Aindex%3A%29.json'
content_hash: 'sha256:f43fa79305ab0f8c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md)

# setBytes(_:length:index:)

<sub>Instance Method</sub>

Copies data directly to the GPU to populate an entry in the buffer argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setBytes(_ bytes: UnsafeRawPointer, length: Int, index: Int)
```

## Parameters

- `bytes` — A pointer to where the data to copy starts.

- `length` — The number of bytes to copy.

- `index` — The index the data binds to in the argument table.

## Discussion

> [!important] Important
> This method only works for data smaller than 4 kilobytes that doesn’t persist. Create an [MTLBuffer](../mtlbuffer.md) instance if your data exceeds 4 KB, needs to persist on the GPU, or you access results on the CPU.

This method allows Metal to copy data efficiently onto the GPU without the need for your own buffer. Binding data directly can improve performance, especially when making many small allocations.

## See Also

### Binding raw bytes

- [- setBytes:length:attributeStride:atIndex:](<setbytes(__length_attributestride_index_).md>) — Copies data with a given stride directly to the GPU to populate an entry in the buffer argument table.
