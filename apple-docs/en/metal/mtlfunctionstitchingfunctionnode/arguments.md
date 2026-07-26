---
title: arguments
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfunctionstitchingfunctionnode/arguments
source_url: 'https://developer.apple.com/documentation/metal/mtlfunctionstitchingfunctionnode/arguments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunctionstitchingfunctionnode/arguments.json'
content_hash: 'sha256:a485a2f020134ba7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLFunctionStitchingFunctionNode](../mtlfunctionstitchingfunctionnode.md)

# arguments

<sub>Instance Property</sub>

An ordered list of the nodes that provide the function’s arguments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var arguments: [any MTLFunctionStitchingNode] { get set }
```

## Discussion

Each node’s output data types needs to match the input data type of the matching argument.

## See Also

### Configuring a function node

- [name](name.md) — The name of the function to call.
- [controlDependencies](controldependencies.md) — The list of nodes that need to execute before executing the node.
