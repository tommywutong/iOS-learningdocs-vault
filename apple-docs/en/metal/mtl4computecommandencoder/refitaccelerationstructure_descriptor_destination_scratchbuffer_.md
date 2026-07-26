---
title: 'refitAccelerationStructure:descriptor:destination:scratchBuffer:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4computecommandencoder/refitaccelerationstructure:descriptor:destination:scratchbuffer:'
source_url: 'https://developer.apple.com/documentation/metal/mtl4computecommandencoder/refitaccelerationstructure:descriptor:destination:scratchbuffer:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4computecommandencoder/refitaccelerationstructure%3Adescriptor%3Adestination%3Ascratchbuffer%3A.json'
content_hash: 'sha256:1da48026b9a67f0e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4ComputeCommandEncoder](../mtl4computecommandencoder.md)

# refitAccelerationStructure:descriptor:destination:scratchBuffer:

<sub>Instance Method</sub>

Encodes an acceleration structure refit into the command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) refitAccelerationStructure:(id<MTLAccelerationStructure>) sourceAccelerationStructure descriptor:(MTL4AccelerationStructureDescriptor *) descriptor destination:(id<MTLAccelerationStructure>) destinationAccelerationStructure scratchBuffer:(MTL4BufferRange) scratchBuffer;
```

## Parameters

- `sourceAccelerationStructure` — Acceleration structure to refit.

- `descriptor` — A descriptor for the acceleration structure to refit.

- `destinationAccelerationStructure` — Acceleration structure to store the refit result into. If `destinationAccelerationStructure` is `nil`, Metal performs an in-place refit operation of the `sourceAccelerationStructure`.

- `scratchBuffer` — Scratch buffer Metal can use while refitting the acceleration structure. Metal may overwrite the contents of this buffer, and you should consider them “undefined” after the refit operation starts and completes.

## Discussion

You refit an acceleration structure to update it when the geometry it references changes. This operation is typically much faster than rebuilding the acceleration structure from scratch. The trade off is that after you refit the acceleration structure, its quality, as well as the performance of any subsequent ray tracing operation degrades, depending on how much the geometry changes.

After certain operations, refitting an acceleration structure may not be possible, for example, after adding or removing geometry.

When you refit an acceleration structure, you can do so in place, by specifying the same source and destination acceleration structures, or by providing a `nil` destination acceleration structure. If the source and destination acceleration structures aren’t the same, then you are responsible for ensuring they don’t overlap in memory.

Typically, the destination acceleration structure is at least as large as the source acceleration structure, except in cases where you compact the source acceleration structure. In this case, you need to allocate the destination acceleration to be at least as large as the compacted size of the source acceleration structure.

The scratch buffer you provide for the refit operation needs to be at least as large as the size that the query [- accelerationStructureSizesWithDescriptor:](<../mtldevice/accelerationstructuresizes(descriptor_).md>) returns. If the size this query returns is zero, you can omit providing a scratch buffer by passing `0` as the address to the `scratchBuffer` parameter.

Use an instance of [MTLResidencySet](../mtlresidencyset.md) to mark residency of the scratch buffer the `scratchBuffer` parameter references, as well as for all the instance and primitive acceleration structures you directly and indirectly reference.

## See Also

### Encoding acceleration structure refit commands

- [- refitAccelerationStructure:descriptor:destination:scratchBuffer:options:](<refit(sourceaccelerationstructure_descriptor_destinationaccelerationstructure_scratchbuffer_options_).md>) — Encodes an acceleration structure refit operation into the command buffer, providing additional options.
