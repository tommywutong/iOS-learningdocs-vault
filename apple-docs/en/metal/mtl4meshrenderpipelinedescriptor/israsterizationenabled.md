---
title: isRasterizationEnabled
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4meshrenderpipelinedescriptor/israsterizationenabled
source_url: 'https://developer.apple.com/documentation/metal/mtl4meshrenderpipelinedescriptor/israsterizationenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4meshrenderpipelinedescriptor/israsterizationenabled.json'
content_hash: 'sha256:1c784dafe47e9cf9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4MeshRenderPipelineDescriptor](../mtl4meshrenderpipelinedescriptor.md)

# isRasterizationEnabled

<sub>Instance Property</sub>

Determines whether the pipeline rasterizes primitives.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isRasterizationEnabled: Bool { get set }
```

## Discussion

By default, this value is [true](../../swift/true.md), specifying that this pipeline rasterizes primitives. Set this property to [false](../../swift/false.md) when you don’t provide a fragment shader function via function [fragmentFunctionDescriptor](fragmentfunctiondescriptor.md).
