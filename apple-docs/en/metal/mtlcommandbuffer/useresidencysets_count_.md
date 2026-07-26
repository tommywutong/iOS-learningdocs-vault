---
title: 'useResidencySets:count:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcommandbuffer/useresidencysets:count:'
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffer/useresidencysets:count:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffer/useresidencysets%3Acount%3A.json'
content_hash: 'sha256:b4bcab897b653838'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBuffer](../mtlcommandbuffer.md)

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

## See Also

### Attaching residency sets

- [- useResidencySet:](<useresidencyset(__).md>) — Applies a residency set to a command buffer.
