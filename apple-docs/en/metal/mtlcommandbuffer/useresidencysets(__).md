---
title: 'useResidencySets(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcommandbuffer/useresidencysets(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffer/useresidencysets(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffer/useresidencysets%28_%3A%29.json'
content_hash: 'sha256:f172fd523f6100df'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBuffer](../mtlcommandbuffer.md)

# useResidencySets(_:)

<sub>Instance Method</sub>

Applies multiple residency sets to a command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func useResidencySets(_ residencySets: [any MTLResidencySet])
```

## Parameters

- `residencySets` — An array of residency sets, each of which contains resource allocations, such as [MTLBuffer](../mtlbuffer.md), [MTLTexture](../mtltexture.md), and [MTLHeap](../mtlheap.md) instances.

## Discussion

Each command buffer can maintain a list of up to 32 different residency sets. See [Simplifying GPU resource management with residency sets](../simplifying-gpu-resource-management-with-residency-sets.md) and [MTLResidencySet](../mtlresidencyset.md) for more information.

## See Also

### Attaching residency sets

- [- useResidencySet:](<useresidencyset(__).md>) — Applies a residency set to a command buffer.
