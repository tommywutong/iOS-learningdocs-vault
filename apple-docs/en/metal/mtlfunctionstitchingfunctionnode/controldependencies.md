---
title: controlDependencies
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfunctionstitchingfunctionnode/controldependencies
source_url: 'https://developer.apple.com/documentation/metal/mtlfunctionstitchingfunctionnode/controldependencies'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunctionstitchingfunctionnode/controldependencies.json'
content_hash: 'sha256:d3b127228f6ed704'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLFunctionStitchingFunctionNode](../mtlfunctionstitchingfunctionnode.md)

# controlDependencies

<sub>Instance Property</sub>

The list of nodes that need to execute before executing the node.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var controlDependencies: [MTLFunctionStitchingFunctionNode] { get set }
```

## Discussion

When a stitched function calls functions that have side effects on their input data, you often need the GPU to execute functions in a specific order. In such cases, use the [controlDependencies](controldependencies.md) property to specify which nodes need to run before executing this node.

## See Also

### Configuring a function node

- [name](name.md) — The name of the function to call.
- [arguments](arguments.md) — An ordered list of the nodes that provide the function’s arguments.
