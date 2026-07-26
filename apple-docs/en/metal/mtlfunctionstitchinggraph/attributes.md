---
title: attributes
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfunctionstitchinggraph/attributes
source_url: 'https://developer.apple.com/documentation/metal/mtlfunctionstitchinggraph/attributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunctionstitchinggraph/attributes.json'
content_hash: 'sha256:762c675fce107892'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLFunctionStitchingGraph](../mtlfunctionstitchinggraph.md)

# attributes

<sub>Instance Property</sub>

A list of attributes to configure how the Metal device object generates the new stitched function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var attributes: [any MTLFunctionStitchingAttribute] { get set }
```

## See Also

### Configuring a function graph

- [functionName](functionname.md) — The name of the new stitched function.
- [nodes](nodes.md) — The nodes in the function’s call graph.
- [outputNode](outputnode.md) — The node with the output that’s the output of the new stitched function.
