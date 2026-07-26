---
title: requiredThreadsPerThreadgroup
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4computepipelinedescriptor/requiredthreadsperthreadgroup
source_url: 'https://developer.apple.com/documentation/metal/mtl4computepipelinedescriptor/requiredthreadsperthreadgroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4computepipelinedescriptor/requiredthreadsperthreadgroup.json'
content_hash: 'sha256:dcfc016d4f0dc331'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4ComputePipelineDescriptor](../mtl4computepipelinedescriptor.md)

# requiredThreadsPerThreadgroup

<sub>Instance Property</sub>

The required number of threads per threadgroup for compute dispatches.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var requiredThreadsPerThreadgroup: MTLSize { get set }
```

## Discussion

When you set this value, you are responsible for ensuring that the `threadsPerThreadgroup` argument of any compute dispatch matches it.

Setting this property is optional, except in cases where the pipeline uses _CooperativeTensors_.

This property’s default value is `0`, which disables its effect.
