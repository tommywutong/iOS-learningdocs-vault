---
title: objectThreadExecutionWidth
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpipelinestate/objectthreadexecutionwidth
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinestate/objectthreadexecutionwidth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinestate/objectthreadexecutionwidth.json'
content_hash: 'sha256:2d812d2a0850dba8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineState](../mtlrenderpipelinestate.md)

# objectThreadExecutionWidth

<sub>Instance Property</sub>

The number of threads the render pass applies to a SIMD group for an object shader.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var objectThreadExecutionWidth: Int { get }
```

## Discussion

You can access the value of this property in your shader code by adding an integer parameter with the `[[threads_per_simdgroup]]` attribute. For more information about this attribute, see the [Metal Shading Language Specification (PDF)](https://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf).

## See Also

### Checking object shader memory requirements

- [maxTotalThreadsPerObjectThreadgroup](maxtotalthreadsperobjectthreadgroup.md) — The largest number of threads the pipeline state can have in a single object shader threadgroup.
