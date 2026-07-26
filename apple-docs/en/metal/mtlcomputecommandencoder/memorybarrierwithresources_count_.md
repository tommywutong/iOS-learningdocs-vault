---
title: 'memoryBarrierWithResources:count:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcomputecommandencoder/memorybarrierwithresources:count:'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/memorybarrierwithresources:count:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputecommandencoder/memorybarrierwithresources%3Acount%3A.json'
content_hash: 'sha256:325fcc81d3042e1b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md)

# memoryBarrierWithResources:count:

<sub>Instance Method</sub>

Creates a memory barrier that enforces the order of write and read operations for specific resources.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) memoryBarrierWithResources:(id<MTLResource> const[]) resources count:(NSUInteger) count;
```

## Parameters

- `resources` — A C array of [MTLResource](../mtlresource.md) instances the barrier applies to.

- `count` — The number of resources in the array.

## Discussion

Memory barriers ensure the relevant passes finish updating resources before starting the stages of subsequent commands that depend on those resources.

To determine whether a GPU supports memory barriers, see the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf).

## See Also

### Preventing resource access conflicts

- [- waitForFence:](<waitforfence(__).md>) — Encodes a command that instructs the GPU to pause the compute pass until another pass updates a fence.
- [- updateFence:](<updatefence(__).md>) — Encodes a command that instructs the GPU to update a fence after the compute pass completes.
- [- memoryBarrierWithScope:](<memorybarrier(scope_).md>) — Creates a memory barrier that enforces the order of write and read operations for specific resource types.
