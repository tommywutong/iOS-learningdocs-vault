---
title: fragmentAdditionalBinaryFunctions
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpipelinefunctionsdescriptor/fragmentadditionalbinaryfunctions
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinefunctionsdescriptor/fragmentadditionalbinaryfunctions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinefunctionsdescriptor/fragmentadditionalbinaryfunctions.json'
content_hash: 'sha256:c63468266c53bbce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineFunctionsDescriptor](../mtlrenderpipelinefunctionsdescriptor.md)

# fragmentAdditionalBinaryFunctions

<sub>Instance Property</sub>

The fragment functions to add to the render pipeline.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var fragmentAdditionalBinaryFunctions: [any MTLFunction]? { get set }
```

## See Also

### Configuring the descriptor’s functions

- [vertexAdditionalBinaryFunctions](vertexadditionalbinaryfunctions.md) — The vertex functions to add to the render pipeline.
- [tileAdditionalBinaryFunctions](tileadditionalbinaryfunctions.md) — The tile functions to add to the render pipeline.
