---
title: fragmentLinkedFunctions
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpipelinedescriptor/fragmentlinkedfunctions
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/fragmentlinkedfunctions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinedescriptor/fragmentlinkedfunctions.json'
content_hash: 'sha256:c28fcda34d92b239'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineDescriptor](../mtlrenderpipelinedescriptor.md)

# fragmentLinkedFunctions

<sub>Instance Property</sub>

Functions that you can specify as function arguments for the fragment shader when encoding commands that use the pipeline.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@NSCopying var fragmentLinkedFunctions: MTLLinkedFunctions! { get set }
```

## See Also

### Specifying callable functions for the pipeline

- [vertexLinkedFunctions](vertexlinkedfunctions.md) — Functions that you can specify as function arguments for the vertex shader when encoding commands that use the pipeline.
