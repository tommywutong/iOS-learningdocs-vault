---
title: objectBindings
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpipelinereflection/objectbindings
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinereflection/objectbindings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinereflection/objectbindings.json'
content_hash: 'sha256:55bf2b09361e9329'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineReflection](../mtlrenderpipelinereflection.md)

# objectBindings

<sub>Instance Property</sub>

An array of binding instances, each of which represents a parameter of the pipeline state’s object shader.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var objectBindings: [any MTLBinding] { get }
```

## Discussion

The [MTLBinding](../mtlbinding.md) elements in the array are in the same order as the object shader’s declaration signature.

## See Also

### Inspecting a shader’s parameter

- [fragmentBindings](fragmentbindings.md) — An array of binding instances, each of which represents a parameter of the pipeline state’s fragment shader.
- [meshBindings](meshbindings.md) — An array of binding instances, each of which represents a parameter of the pipeline state’s mesh shader.
- [tileBindings](tilebindings.md) — An array of binding instances, each of which represents a parameter of the pipeline state’s tile shader.
- [vertexBindings](vertexbindings.md) — An array of binding instances, each of which represents a parameter of the pipeline state’s vertex shader.
