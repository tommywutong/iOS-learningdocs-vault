---
title: 'setAddress(_:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4argumenttable/setaddress(_:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4argumenttable/setaddress(_:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4argumenttable/setaddress%28_%3Aindex%3A%29.json'
content_hash: 'sha256:ee64d44d91d5065d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4ArgumentTable](../mtl4argumenttable.md)

# setAddress(_:index:)

<sub>Instance Method</sub>

Binds a GPU address to a buffer binding slot.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setAddress(_ gpuAddress: MTLGPUAddress, index bindingIndex: Int)
```

## Parameters

- `gpuAddress` — The GPU address of a [MTLBuffer](../mtlbuffer.md) to set.

- `bindingIndex` — A valid binding index in the buffer binding range. It is an error for this value to match or exceed the value of property [maxBufferBindCount](../mtl4argumenttabledescriptor/maxbufferbindcount.md) on the descriptor from which you created this argument table.
