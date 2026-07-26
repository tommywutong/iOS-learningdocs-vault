---
title: binaryLinkedFunctions
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4pipelinestagedynamiclinkingdescriptor/binarylinkedfunctions
source_url: 'https://developer.apple.com/documentation/metal/mtl4pipelinestagedynamiclinkingdescriptor/binarylinkedfunctions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4pipelinestagedynamiclinkingdescriptor/binarylinkedfunctions.json'
content_hash: 'sha256:4fd2149011dc6db3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4PipelineStageDynamicLinkingDescriptor](../mtl4pipelinestagedynamiclinkingdescriptor.md)

# binaryLinkedFunctions

<sub>Instance Property</sub>

Provides the array of binary functions to link.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var binaryLinkedFunctions: [any MTL4BinaryFunction]? { get set }
```

## Discussion

Binary functions are shader functions that you compile from Metal IR to machine code ahead of time using instances of [MTL4Compiler](../mtl4compiler.md).
