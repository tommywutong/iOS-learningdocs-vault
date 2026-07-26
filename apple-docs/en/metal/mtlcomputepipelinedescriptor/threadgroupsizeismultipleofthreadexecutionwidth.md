---
title: threadGroupSizeIsMultipleOfThreadExecutionWidth
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcomputepipelinedescriptor/threadgroupsizeismultipleofthreadexecutionwidth
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputepipelinedescriptor/threadgroupsizeismultipleofthreadexecutionwidth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputepipelinedescriptor/threadgroupsizeismultipleofthreadexecutionwidth.json'
content_hash: 'sha256:ff0ab760231d3379'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputePipelineDescriptor](../mtlcomputepipelinedescriptor.md)

# threadGroupSizeIsMultipleOfThreadExecutionWidth

<sub>Instance Property</sub>

A Boolean value that indicates whether the threadgroup size is always a multiple of the thread execution width.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var threadGroupSizeIsMultipleOfThreadExecutionWidth: Bool { get set }
```

## Discussion

> [!warning] Warning
> When this configuration value is `true` and the threadgroup size isn’t a multiple of thread execution width, the compute pass’s execution results are undefined.

If you can guarantee that the threadgroup size used by all compute commands in this pipeline is a multiple of [threadExecutionWidth](../mtlcomputepipelinestate/threadexecutionwidth.md), set this property to `true` to take advantage of additional Metal optimizations.

The default value is `false`.

## See Also

### Configuring the compute execution environment

- [computeFunction](computefunction.md) — The compute kernel the pipeline calls.
- [maxTotalThreadsPerThreadgroup](maxtotalthreadsperthreadgroup.md) — A property that limits the number of threads you can dispatch in a threadgroup for the compute function.
- [maxCallStackDepth](maxcallstackdepth.md) — The maximum call stack depth for indirect function calls in compute shaders.
