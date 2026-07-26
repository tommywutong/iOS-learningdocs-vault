---
title: supportAddingFragmentBinaryFunctions
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpipelinedescriptor/supportaddingfragmentbinaryfunctions
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/supportaddingfragmentbinaryfunctions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinedescriptor/supportaddingfragmentbinaryfunctions.json'
content_hash: 'sha256:e1b5346825b4de7b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineDescriptor](../mtlrenderpipelinedescriptor.md)

# supportAddingFragmentBinaryFunctions

<sub>Instance Property</sub>

A Boolean value that indicates whether you can use the pipeline to create new pipelines by adding binary functions to the fragment shader’s callable functions list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var supportAddingFragmentBinaryFunctions: Bool { get set }
```

## See Also

### Specifying precompiled shader binaries

- [supportAddingVertexBinaryFunctions](supportaddingvertexbinaryfunctions.md) — A Boolean value that indicates whether you can use the pipeline to create new pipelines by adding binary functions to the vertex shader’s callable functions list.
- [binaryArchives](binaryarchives.md) — An array of binary archives to search for precompiled versions of the shader.
