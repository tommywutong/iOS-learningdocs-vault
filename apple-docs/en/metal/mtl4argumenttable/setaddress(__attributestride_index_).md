---
title: 'setAddress(_:attributeStride:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4argumenttable/setaddress(_:attributestride:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4argumenttable/setaddress(_:attributestride:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4argumenttable/setaddress%28_%3Aattributestride%3Aindex%3A%29.json'
content_hash: 'sha256:c3bb71bb2825c8b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4ArgumentTable](../mtl4argumenttable.md)

# setAddress(_:attributeStride:index:)

<sub>Instance Method</sub>

Binds a GPU address to a buffer binding slot, providing a dynamic vertex stride.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setAddress(_ gpuAddress: MTLGPUAddress, attributeStride stride: Int, index bindingIndex: Int)
```

## Parameters

- `gpuAddress` — The GPU address of a [MTLBuffer](../mtlbuffer.md) to set.

- `stride` — The stride between attributes in the buffer.

- `bindingIndex` — A valid binding index in the buffer binding range. It is an error for this value to match or exceed the value of property [maxBufferBindCount](../mtl4argumenttabledescriptor/maxbufferbindcount.md) on the descriptor from which you created this argument table.

## Discussion

This method requires that the value of property [supportAttributeStrides](../mtl4argumenttabledescriptor/supportattributestrides.md) on the descriptor from which you created this argument table is true.
