---
title: maxCallStackDepth
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcomputepipelinedescriptor/maxcallstackdepth
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputepipelinedescriptor/maxcallstackdepth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputepipelinedescriptor/maxcallstackdepth.json'
content_hash: 'sha256:b60568575ce14c44'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputePipelineDescriptor](../mtlcomputepipelinedescriptor.md)

# maxCallStackDepth

<sub>Instance Property</sub>

The maximum call stack depth for indirect function calls in compute shaders.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var maxCallStackDepth: Int { get set }
```

## Discussion

The property’s default value is `1`. Change its value if you use recursive functions in your compute pass.

The maximum call stack depth applies only to indirect function calls in your shader, and affects the upper bound of stack memory for each thread. Indirect function calls include those to visible functions, intersection functions, and to dynamic libraries.

> [!tip] Tip
> To avoid a runtime performance impact, keep this value as small as possible because the framework reserves a large call stack.

## See Also

### Configuring the compute execution environment

- [computeFunction](computefunction.md) — The compute kernel the pipeline calls.
- [threadGroupSizeIsMultipleOfThreadExecutionWidth](threadgroupsizeismultipleofthreadexecutionwidth.md) — A Boolean value that indicates whether the threadgroup size is always a multiple of the thread execution width.
- [maxTotalThreadsPerThreadgroup](maxtotalthreadsperthreadgroup.md) — A property that limits the number of threads you can dispatch in a threadgroup for the compute function.
