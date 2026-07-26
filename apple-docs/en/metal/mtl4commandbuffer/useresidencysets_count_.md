---
title: 'useResidencySets:count:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4commandbuffer/useresidencysets:count:'
source_url: 'https://developer.apple.com/documentation/metal/mtl4commandbuffer/useresidencysets:count:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4commandbuffer/useresidencysets%3Acount%3A.json'
content_hash: 'sha256:4ea5b1ba53150719'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CommandBuffer](../mtl4commandbuffer.md)

# useResidencySets:count:

<sub>Instance Method</sub>

Applies multiple residency sets to a command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) useResidencySets:(id<MTLResidencySet> const[]) residencySets count:(NSUInteger) count;
```

## Parameters

- `residencySets` — A C array of residency sets, each of which contains resource allocations, such as [MTLBuffer](../mtlbuffer.md), [MTLTexture](../mtltexture.md), and [MTLHeap](../mtlheap.md) instances.

- `count` — The number of elements in `residencySets`.

## Discussion

Each command buffer can maintain a list of up to 32 different residency sets. See [Simplifying GPU resource management with residency sets](../simplifying-gpu-resource-management-with-residency-sets.md) and [MTLResidencySet](../mtlresidencyset.md) for more information.
