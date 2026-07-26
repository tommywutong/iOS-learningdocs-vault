---
title: name
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfunctionstitchingfunctionnode/name
source_url: 'https://developer.apple.com/documentation/metal/mtlfunctionstitchingfunctionnode/name'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunctionstitchingfunctionnode/name.json'
content_hash: 'sha256:17ff163198f4f37f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLFunctionStitchingFunctionNode](../mtlfunctionstitchingfunctionnode.md)

# name

<sub>Instance Property</sub>

The name of the function to call.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var name: String { get set }
```

## Discussion

The name needs to match one of the functions in the stitched library descriptor’s [functions](../mtlstitchedlibrarydescriptor/functions.md) property.

## See Also

### Configuring a function node

- [arguments](arguments.md) — An ordered list of the nodes that provide the function’s arguments.
- [controlDependencies](controldependencies.md) — The list of nodes that need to execute before executing the node.
