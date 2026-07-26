---
title: tileBindings
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpipelinereflection/tilebindings
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinereflection/tilebindings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinereflection/tilebindings.json'
content_hash: 'sha256:f0b6787ad4192df1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineReflection](../mtlrenderpipelinereflection.md)

# tileBindings

<sub>Instance Property</sub>

An array of binding instances, each of which represents a parameter of the pipeline state’s tile shader.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var tileBindings: [any MTLBinding] { get }
```

## Discussion

The [MTLBinding](../mtlbinding.md) elements in the array are in the same order as the tile shader’s declaration signature.

## See Also

### Inspecting a shader’s parameter

- [fragmentBindings](fragmentbindings.md) — An array of binding instances, each of which represents a parameter of the pipeline state’s fragment shader.
- [meshBindings](meshbindings.md) — An array of binding instances, each of which represents a parameter of the pipeline state’s mesh shader.
- [objectBindings](objectbindings.md) — An array of binding instances, each of which represents a parameter of the pipeline state’s object shader.
- [vertexBindings](vertexbindings.md) — An array of binding instances, each of which represents a parameter of the pipeline state’s vertex shader.
