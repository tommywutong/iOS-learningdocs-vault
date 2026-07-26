---
title: MTLAllocation
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlallocation
source_url: 'https://developer.apple.com/documentation/metal/mtlallocation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlallocation.json'
content_hash: 'sha256:ad28f00229e2d71a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLAllocation

<sub>Protocol</sub>

A memory allocation from a Metal GPU device, such as a memory heap, texture, or data buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLAllocation : NSObjectProtocol
```

## Overview

Types that conform to [MTLAllocation](mtlallocation.md), including [MTLBuffer](mtlbuffer.md), [MTLTexture](mtltexture.md), and [MTLHeap](mtlheap.md), have underlying memory. You make their memory _resident_, or GPU-accessible, by adding an allocation to an [MTLResidencySet](mtlresidencyset.md) or calling the appropriate method of a command encoder.

See [Simplifying GPU resource management with residency sets](simplifying-gpu-resource-management-with-residency-sets.md) for more information.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Inherited By**: [MTL4MachineLearningPipelineState](mtl4machinelearningpipelinestate.md), [MTLAccelerationStructure](mtlaccelerationstructure.md), [MTLBuffer](mtlbuffer.md), [MTLComputePipelineState](mtlcomputepipelinestate.md), [MTLHeap](mtlheap.md), [MTLIndirectCommandBuffer](mtlindirectcommandbuffer.md), [MTLIntersectionFunctionTable](mtlintersectionfunctiontable.md), [MTLRenderPipelineState](mtlrenderpipelinestate.md), [MTLResource](mtlresource.md), [MTLTensor](mtltensor.md), [MTLTexture](mtltexture.md), [MTLVisibleFunctionTable](mtlvisiblefunctiontable.md)

## Topics

### Inspecting an allocation

- [allocatedSize](mtlallocation/allocatedsize.md) — The amount of memory, in byes, a resource consumes, such as for a buffer, texture, or heap.

## See Also

### Common resource functionality

- [MTLGPUAddress](mtlgpuaddress.md) — A 64-bit unsigned integer type appropriate for storing GPU addresses.
- [MTLResource](mtlresource.md) — An allocation of memory accessible to a GPU.
- [MTLResourceOptions](mtlresourceoptions.md) — Optional arguments used to set the behavior of a resource.
- [MTLResourceUsage](mtlresourceusage.md) — Options that describe how a graphics or compute function uses an argument buffer’s resource.
- [MTLResourceID](mtlresourceid.md)
