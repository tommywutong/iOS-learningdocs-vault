---
title: 'useResidencySet(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcommandbuffer/useresidencyset(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffer/useresidencyset(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffer/useresidencyset%28_%3A%29.json'
content_hash: 'sha256:e3f5286db6166ab6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBuffer](../mtlcommandbuffer.md)

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

## See Also

### Attaching residency sets

- [useResidencySets(_:)](<useresidencysets(__).md>) — Applies multiple residency sets to a command buffer.
