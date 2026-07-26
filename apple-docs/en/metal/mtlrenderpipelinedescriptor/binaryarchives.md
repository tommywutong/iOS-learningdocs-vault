---
title: binaryArchives
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpipelinedescriptor/binaryarchives
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/binaryarchives'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinedescriptor/binaryarchives.json'
content_hash: 'sha256:3b2fc6ddf2b15e3c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineDescriptor](../mtlrenderpipelinedescriptor.md)

# binaryArchives

<sub>Instance Property</sub>

An array of binary archives to search for precompiled versions of the shader.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var binaryArchives: [any MTLBinaryArchive]? { get set }
```

## See Also

### Specifying precompiled shader binaries

- [supportAddingVertexBinaryFunctions](supportaddingvertexbinaryfunctions.md) — A Boolean value that indicates whether you can use the pipeline to create new pipelines by adding binary functions to the vertex shader’s callable functions list.
- [supportAddingFragmentBinaryFunctions](supportaddingfragmentbinaryfunctions.md) — A Boolean value that indicates whether you can use the pipeline to create new pipelines by adding binary functions to the fragment shader’s callable functions list.
