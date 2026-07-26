---
title: 'addResidencySets(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4commandqueue/addresidencysets(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4commandqueue/addresidencysets(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4commandqueue/addresidencysets%28_%3A%29.json'
content_hash: 'sha256:8f1b9e50e8361db6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CommandQueue](../mtl4commandqueue.md)

# addResidencySets(_:)

<sub>Instance Method</sub>

Applies multiple residency sets to a queue, which Metal applies to the queue’s command buffers as you commit them.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func addResidencySets(_ residencySets: [any MTLResidencySet])
```

## Parameters

- `residencySets` — An array of residency sets, each of which contains resource allocations, such as [MTLBuffer](../mtlbuffer.md), [MTLTexture](../mtltexture.md), and [MTLHeap](../mtlheap.md) instances.

## Discussion

Each command queue can maintain a list of up to 32 different residency sets. See [Simplifying GPU resource management with residency sets](../simplifying-gpu-resource-management-with-residency-sets.md) and [MTLResidencySet](../mtlresidencyset.md) for more information.
