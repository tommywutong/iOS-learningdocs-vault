---
title: computeFunction
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcomputepipelinedescriptor/computefunction
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputepipelinedescriptor/computefunction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputepipelinedescriptor/computefunction.json'
content_hash: 'sha256:79d6348114fefe0d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputePipelineDescriptor](../mtlcomputepipelinedescriptor.md)

# computeFunction

<sub>Instance Property</sub>

The compute kernel the pipeline calls.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var computeFunction: (any MTLFunction)? { get set }
```

## Discussion

> [!warning] Warning
> Ensure that this value is non-`nil` before creating a new [MTLComputePipelineState](../mtlcomputepipelinestate.md) with the associated pipeline descriptor instance.

The default value is `nil`.

## See Also

### Configuring the compute execution environment

- [threadGroupSizeIsMultipleOfThreadExecutionWidth](threadgroupsizeismultipleofthreadexecutionwidth.md) — A Boolean value that indicates whether the threadgroup size is always a multiple of the thread execution width.
- [maxTotalThreadsPerThreadgroup](maxtotalthreadsperthreadgroup.md) — A property that limits the number of threads you can dispatch in a threadgroup for the compute function.
- [maxCallStackDepth](maxcallstackdepth.md) — The maximum call stack depth for indirect function calls in compute shaders.
