---
title: 'useResidencySet(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4commandbuffer/useresidencyset(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4commandbuffer/useresidencyset(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4commandbuffer/useresidencyset%28_%3A%29.json'
content_hash: 'sha256:2d0bb3d85f7d288d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CommandBuffer](../mtl4commandbuffer.md)

# useResidencySet(_:)

<sub>Instance Method</sub>

Applies a residency set to a command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func useResidencySet(_ residencySet: any MTLResidencySet)
```

## Parameters

- `residencySet` — A residency set that contains resource allocations, such as [MTLBuffer](../mtlbuffer.md), [MTLTexture](../mtltexture.md), and [MTLHeap](../mtlheap.md) instances.

## Discussion

Each command buffer can maintain a list of up to 32 different residency sets. See [Simplifying GPU resource management with residency sets](../simplifying-gpu-resource-management-with-residency-sets.md) and [MTLResidencySet](../mtlresidencyset.md) for more information.
