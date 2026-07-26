---
title: maxTotalThreadsPerThreadgroup
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcomputepipelinestate/maxtotalthreadsperthreadgroup
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputepipelinestate/maxtotalthreadsperthreadgroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputepipelinestate/maxtotalthreadsperthreadgroup.json'
content_hash: 'sha256:1c16b51dc2b922ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputePipelineState](../mtlcomputepipelinestate.md)

# maxTotalThreadsPerThreadgroup

<sub>Instance Property</sub>

The maximum number of threads in a threadgroup that you can dispatch to the pipeline.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var maxTotalThreadsPerThreadgroup: Int { get }
```

## Discussion

When you create a compute pipeline state, it calculates the maximum number of threads available on the device. This value never changes, but may be different for different pipeline objects.

See [Creating threads and threadgroups](../creating-threads-and-threadgroups.md) and [Calculating threadgroup and grid sizes](../calculating-threadgroup-and-grid-sizes.md) for more information on aligning data, thread width, and threadgroup size.

## See Also

### Checking threadgroup attributes

- [threadExecutionWidth](threadexecutionwidth.md) — The number of threads that the GPU executes simultaneously.
- [staticThreadgroupMemoryLength](staticthreadgroupmemorylength.md) — The length, in bytes, of statically allocated threadgroup memory.
