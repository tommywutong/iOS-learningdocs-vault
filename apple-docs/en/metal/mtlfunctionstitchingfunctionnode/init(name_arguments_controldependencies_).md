---
title: 'init(name:arguments:controlDependencies:)'
framework: Metal
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlfunctionstitchingfunctionnode/init(name:arguments:controldependencies:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlfunctionstitchingfunctionnode/init(name:arguments:controldependencies:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunctionstitchingfunctionnode/init%28name%3Aarguments%3Acontroldependencies%3A%29.json'
content_hash: 'sha256:86ca5a3e720f9819'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLFunctionStitchingFunctionNode](../mtlfunctionstitchingfunctionnode.md)

# init(name:arguments:controlDependencies:)

<sub>Initializer</sub>

Creates a new function node.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(name: String, arguments: [any MTLFunctionStitchingNode], controlDependencies: [MTLFunctionStitchingFunctionNode])
```

## Parameters

- `name` — The name of the function to call.

- `arguments` — An ordered list of the nodes that provide the function’s arguments.

- `controlDependencies` — The list of nodes that need to run before executing this node.
