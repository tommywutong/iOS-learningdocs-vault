---
title: staticThreadgroupMemoryLength
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcomputepipelinestate/staticthreadgroupmemorylength
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputepipelinestate/staticthreadgroupmemorylength'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputepipelinestate/staticthreadgroupmemorylength.json'
content_hash: 'sha256:20b1268dc5192807'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputePipelineState](../mtlcomputepipelinestate.md)

# staticThreadgroupMemoryLength

<sub>Instance Property</sub>

The length, in bytes, of statically allocated threadgroup memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var staticThreadgroupMemoryLength: Int { get }
```

## See Also

### Checking threadgroup attributes

- [maxTotalThreadsPerThreadgroup](maxtotalthreadsperthreadgroup.md) — The maximum number of threads in a threadgroup that you can dispatch to the pipeline.
- [threadExecutionWidth](threadexecutionwidth.md) — The number of threads that the GPU executes simultaneously.
