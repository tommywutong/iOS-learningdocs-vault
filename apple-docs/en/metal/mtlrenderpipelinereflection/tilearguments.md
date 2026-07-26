---
title: tileArguments
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+（16.0 起废弃）, iPadOS 11.0+（16.0 起废弃）, Mac Catalyst 14.0+（16.0 起废弃）, macOS 11.0+（13.0 起废弃）, tvOS 14.5+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtlrenderpipelinereflection/tilearguments
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinereflection/tilearguments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinereflection/tilearguments.json'
content_hash: 'sha256:4b9fbf1c291f281b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineReflection](../mtlrenderpipelinereflection.md)

# tileArguments

<sub>Instance Property</sub>

An array of argument instances, each of which represent a parameter of the pipeline state’s tile shader.

> [!warning] Deprecated
> Use [tileBindings](tilebindings.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var tileArguments: [MTLArgument]? { get }
```

## Discussion

The [MTLArgument](../mtlargument.md) elements in the array are in the same order as the tile shader’s declaration signature.

## See Also

### Deprecated

- [vertexArguments](vertexarguments.md) — An array of argument instances, each of which represent a parameter of the pipeline state’s vertex shader. _(deprecated)_
- [fragmentArguments](fragmentarguments.md) — An array of argument instances, each of which represent a parameter of the pipeline state’s fragment shader. _(deprecated)_
