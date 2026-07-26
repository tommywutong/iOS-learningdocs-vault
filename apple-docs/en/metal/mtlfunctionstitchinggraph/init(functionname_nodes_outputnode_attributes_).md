---
title: 'init(functionName:nodes:outputNode:attributes:)'
framework: Metal
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlfunctionstitchinggraph/init(functionname:nodes:outputnode:attributes:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlfunctionstitchinggraph/init(functionname:nodes:outputnode:attributes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunctionstitchinggraph/init%28functionname%3Anodes%3Aoutputnode%3Aattributes%3A%29.json'
content_hash: 'sha256:f152569d36165437'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLFunctionStitchingGraph](../mtlfunctionstitchinggraph.md)

# init(functionName:nodes:outputNode:attributes:)

<sub>Initializer</sub>

Creates a description of a new function call graph.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(functionName: String, nodes: [MTLFunctionStitchingFunctionNode], outputNode: MTLFunctionStitchingFunctionNode?, attributes: [any MTLFunctionStitchingAttribute])
```

## Parameters

- `functionName` — The name of the new function.

- `nodes` — The nodes in the function’s call graph.

- `outputNode` — The node whose output is the output of the new stitched function.

- `attributes` — A list of attributes used to generate the new stitched function.
