---
title: nodes
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfunctionstitchinggraph/nodes
source_url: 'https://developer.apple.com/documentation/metal/mtlfunctionstitchinggraph/nodes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunctionstitchinggraph/nodes.json'
content_hash: 'sha256:a2f7f99bcde11592'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLFunctionStitchingGraph](../mtlfunctionstitchinggraph.md)

# nodes

<sub>Instance Property</sub>

The nodes in the function’s call graph.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var nodes: [MTLFunctionStitchingFunctionNode] { get set }
```

## See Also

### Configuring a function graph

- [functionName](functionname.md) — The name of the new stitched function.
- [outputNode](outputnode.md) — The node with the output that’s the output of the new stitched function.
- [attributes](attributes.md) — A list of attributes to configure how the Metal device object generates the new stitched function.
