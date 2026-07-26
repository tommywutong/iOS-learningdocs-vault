---
title: outputNode
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfunctionstitchinggraph/outputnode
source_url: 'https://developer.apple.com/documentation/metal/mtlfunctionstitchinggraph/outputnode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunctionstitchinggraph/outputnode.json'
content_hash: 'sha256:fb1fa5d6a87b8aa4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLFunctionStitchingGraph](../mtlfunctionstitchinggraph.md)

# outputNode

<sub>Instance Property</sub>

The node with the output that’s the output of the new stitched function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var outputNode: MTLFunctionStitchingFunctionNode? { get set }
```

## Discussion

The output type of the node needs to match the result type in the stitched function’s declaration.

## See Also

### Configuring a function graph

- [functionName](functionname.md) — The name of the new stitched function.
- [nodes](nodes.md) — The nodes in the function’s call graph.
- [attributes](attributes.md) — A list of attributes to configure how the Metal device object generates the new stitched function.
