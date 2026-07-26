---
title: fragmentArguments
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（16.0 起废弃）, iPadOS 8.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.11+（13.0 起废弃）, tvOS（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtlrenderpipelinereflection/fragmentarguments
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinereflection/fragmentarguments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinereflection/fragmentarguments.json'
content_hash: 'sha256:224fefb1ff79346b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineReflection](../mtlrenderpipelinereflection.md)

# fragmentArguments

<sub>Instance Property</sub>

An array of argument instances, each of which represent a parameter of the pipeline state’s fragment shader.

> [!warning] Deprecated
> Use [fragmentBindings](fragmentbindings.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var fragmentArguments: [MTLArgument]? { get }
```

## Discussion

The [MTLArgument](../mtlargument.md) elements in the array are in the same order as the fragment shader’s declaration signature.

## See Also

### Deprecated

- [vertexArguments](vertexarguments.md) — An array of argument instances, each of which represent a parameter of the pipeline state’s vertex shader. _(deprecated)_
- [tileArguments](tilearguments.md) — An array of argument instances, each of which represent a parameter of the pipeline state’s tile shader. _(deprecated)_
