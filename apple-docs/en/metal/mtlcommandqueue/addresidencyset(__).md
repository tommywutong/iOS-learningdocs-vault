---
title: 'addResidencySet(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcommandqueue/addresidencyset(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandqueue/addresidencyset(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandqueue/addresidencyset%28_%3A%29.json'
content_hash: 'sha256:3f8fc1f6ad3b1b9c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandQueue](../mtlcommandqueue.md)

# addResidencySet(_:)

<sub>Instance Method</sub>

Applies a residency set to a queue, which Metal applies to the queue’s command buffers as you commit them.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func addResidencySet(_ residencySet: any MTLResidencySet)
```

## Parameters

- `residencySet` — A residency set that contains resource allocations, such as [MTLBuffer](../mtlbuffer.md), [MTLTexture](../mtltexture.md), and [MTLHeap](../mtlheap.md) instances.

## Discussion

Each command queue can maintain a list of up to 32 different residency sets. See [Simplifying GPU resource management with residency sets](../simplifying-gpu-resource-management-with-residency-sets.md) and [MTLResidencySet](../mtlresidencyset.md) for more information.

## See Also

### Attaching residency sets

- [addResidencySets(_:)](<addresidencysets(__).md>) — Applies multiple residency sets to a queue, which Metal applies to the queue’s command buffers as you commit them.
