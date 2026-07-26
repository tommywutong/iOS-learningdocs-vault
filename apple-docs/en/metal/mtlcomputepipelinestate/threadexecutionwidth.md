---
title: threadExecutionWidth
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcomputepipelinestate/threadexecutionwidth
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputepipelinestate/threadexecutionwidth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputepipelinestate/threadexecutionwidth.json'
content_hash: 'sha256:fb05c07b143b4472'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputePipelineState](../mtlcomputepipelinestate.md)

# threadExecutionWidth

<sub>Instance Property</sub>

The number of threads that the GPU executes simultaneously.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var threadExecutionWidth: Int { get }
```

## Discussion

For better performance, when dispatching a compute command, make the number of threads in the threadgroup a multiple of `threadExecutionWidth`.

See [Creating threads and threadgroups](../creating-threads-and-threadgroups.md) and [Calculating threadgroup and grid sizes](../calculating-threadgroup-and-grid-sizes.md) for more information on aligning data, thread width, and threadgroup size.

## See Also

### Checking threadgroup attributes

- [maxTotalThreadsPerThreadgroup](maxtotalthreadsperthreadgroup.md) — The maximum number of threads in a threadgroup that you can dispatch to the pipeline.
- [staticThreadgroupMemoryLength](staticthreadgroupmemorylength.md) — The length, in bytes, of statically allocated threadgroup memory.
