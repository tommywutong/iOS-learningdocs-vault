---
title: vertexArguments
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（16.0 起废弃）, iPadOS 8.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.11+（13.0 起废弃）, tvOS（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtlrenderpipelinereflection/vertexarguments
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinereflection/vertexarguments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinereflection/vertexarguments.json'
content_hash: 'sha256:0994c2bac2f1a972'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineReflection](../mtlrenderpipelinereflection.md)

# vertexArguments

<sub>Instance Property</sub>

An array of argument instances, each of which represent a parameter of the pipeline state’s vertex shader.

> [!warning] Deprecated
> Use [vertexBindings](vertexbindings.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var vertexArguments: [MTLArgument]? { get }
```

## Discussion

The [MTLArgument](../mtlargument.md) elements in the array are in the same order as the vertex shader’s declaration signature.

## See Also

### Deprecated

- [fragmentArguments](fragmentarguments.md) — An array of argument instances, each of which represent a parameter of the pipeline state’s fragment shader. _(deprecated)_
- [tileArguments](tilearguments.md) — An array of argument instances, each of which represent a parameter of the pipeline state’s tile shader. _(deprecated)_
